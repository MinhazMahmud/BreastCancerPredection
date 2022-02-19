from django.db import models
from django.db.models.fields import FloatField, IntegerField
from django.contrib.auth.models import User

# Create your models here.


class Dataset(models.Model):
    patient = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    radius_mean = models.FloatField(null= True)
    texture_mean = models.FloatField(null= True)
    perimeter_mean = models.FloatField(null= True)
    area_mean = models.FloatField(null= True)
    smoothness_mean = models.FloatField(null= True)
    compactness_mean = models.FloatField(null= True)
    concavity_mean= models.FloatField(null= True)
    concave_points_mean = models.FloatField(null= True)
    symmetry_mean = models.FloatField(null= True)
    
    radius_se = models.FloatField(null= True)
    perimeter_se  = models.FloatField(null= True)
    area_se = models.FloatField(null= True)
    concave_points_se = models.FloatField(null= True)
    radius_worst = models.FloatField(null= True)
    texture_worst = models.FloatField(null= True)
    perimeter_worst = models.FloatField(null= True)
    area_worst = models.FloatField(null= True)
    smoothness_worst = models.FloatField(null= True)
    compactness_worst = models.FloatField(null= True)   
    concavity_worst = models.FloatField(null= True)
    concave_points_worst = models.FloatField(null= True)
    symmetry_worst = models.FloatField(null= True)
    result = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Prediction(models.Model):
    patient = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    dataset = models.ForeignKey(Dataset,null=True,on_delete=models.SET_NULL)
    result = models.IntegerField(null=True)
    date_predicted = models.DateTimeField(auto_now_add=True, null=True)

