from celery import shared_task
from .models import Doctor
import time

@shared_task
def adding():
	time.sleep(5)
	doc = Doctor(name=f"test")
	doc.save()
	print(doc.name)
	# return doc.result
