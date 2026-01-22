from django.test import TestCase

# Create your tests here.
import re
lnglat = re.match(r'(\d+\.?\d*),(\d+\.?\d*)', '38,125') # 38,125 / 37.5,125 / 38, 125.2 / 37.225,124.4
if not lnglat: # 정규표현식와 일치하면 true
  print("정규표현식과 일치하지 않음")
else:
  print(lnglat.group(0), lnglat.group(1), lnglat.group(2))