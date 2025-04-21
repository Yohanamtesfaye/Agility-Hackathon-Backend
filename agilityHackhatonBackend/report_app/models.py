from django.db import models
import uuid

# Create your models here.
road_severity=(
    (1,"mild"),
    (2,"moderate"),
    (3,"severe")
)

class Report(models.Model):
    id=models.UUIDField(unique=True,primary_key=True,default=uuid.uuid4)
    # user_id=models.ForeignKey() // awaiting user model
    # category_id=models.ForeignKey()
    description=models.TextField()
    severity=models.IntegerField(choices=road_severity,default=1)
    latitude=models.DecimalField(max_digits=9, decimal_places=6)
    longitude=models.DecimalField(max_digits=9, decimal_places=6)
    image_url=models.URLField()
    # status=models.ForeignKey()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description
