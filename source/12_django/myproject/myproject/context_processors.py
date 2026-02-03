from datetime import datetime
from django.utils import timezone 
def myproject(request):
    # type(timezone.now()) => datatime.datetime
    return {
        #'now':datetime.now().strftime("%Y/%m/%d %p %I:%M:%S"),
        "now":timezone.now(),
        "nowStr":datetime.now().strftime("%Y/%m/%d %p %I:%M:%S")
            .replace("AM", "오전")
            .replace("PM", "오후")
    }