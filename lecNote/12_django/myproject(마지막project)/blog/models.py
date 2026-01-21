from django.db import models
import re
from django.forms import ValidationError
from django.utils import timezone
# Create your models here.

REGION_CHOICE = (
  ("Europe","유럽"),
  ("Asia", "아시아"),
  ("Oceania","오세아니아"),
  ("America","아메리카"),
)
def lnglat_validator(value):
  if not re.match(r'(\d+\.?\d*),(\d+\.?\d*)', value):
    raise ValidationError('Invalid LngLat. ex:38, 128')
  
