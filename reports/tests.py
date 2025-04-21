from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Status, Report, Analytic
from django.utils import timezone
from datetime import timedelta
import json

class AnalyticTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.status = Status.objects.create(name='Resolved')
        self.report = Report.objects.create(
            title='Test Report',
            description='Test Description',
            user=self.user,
            category=self.category,
            status=self.status,
            created_at=timezone.now() - timedelta(hours=2),
            resolved_at=timezone.now()
        )
        self.analytic = Analytic.objects.create(
            category=self.category,
            user=self.user,
            average_resolution_time=2.0,
            report_count=1
        )

    def test_analytic_model(self):
        analytic = Analytic.objects.get(category=self.category, user=self.user)
        self.assertEqual(analytic.average_resolution_time, 2.0)
        self.assertEqual(analytic.report_count, 1)

    def test_update_analytics_on_report_save(self):
        new_report = Report.objects.create(
            title='New Report',
            description='New Description',
            user=self.user,
            category=self.category,
            status=self.status,
            created_at=timezone.now() - timedelta(hours=4),
            resolved_at=timezone.now()
        )
        analytic = Analytic.objects.get(category=self.category, user=self.user)
        self.assertEqual(analytic.report_count, 2)
        self.assertAlmostEqual(analytic.average_resolution_time, 3.0, places=1)

class AnalyticAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='Test Category')
        self.status = Status.objects.create(name='Resolved')
        self.report = Report.objects.create(
            title='Test Report',
            description='Test Description',
            user=self.user,
            category=self.category,
            status=self.status,
            created_at=timezone.now() - timedelta(hours=2),
            resolved_at=timezone.now()
        )
        self.analytic = Analytic.objects.create(
            category=self.category,
            user=self.user,
            average_resolution_time=2.0,
            report_count=1
        )

    def test_get_analytics(self):
        response = self.client.get('/api/analytics/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category_name'], 'Test Category')
        self.assertEqual(response.data[0]['user_username'], 'testuser')
        self.assertEqual(response.data[0]['report_count'], 1)

    def test_get_analytics_by_category(self):
        response = self.client.get(f'/api/analytics/?category_id={self.category.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category_name'], 'Test Category')

    def test_get_analytics_by_user(self):
        response = self.client.get(f'/api/analytics/?user_id={self.user.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user_username'], 'testuser')

    def test_analytics_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/analytics/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
