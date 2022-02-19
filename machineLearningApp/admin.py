from machineLearningApp.models import Dataset
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Prediction)