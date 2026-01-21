import os.path
from django.db import models
import time
from datetime import datetime
from django.urls import reverse
from myproject import settings
from django.shortcuts import get_object_or_404
STATUS_CHOICES = (
  ('d', 'Draft'),
  ('p', 'Published'),
  ('w', 'Withdrawn'),
)