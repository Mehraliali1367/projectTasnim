from celery import shared_task
from .models import Images
import time
from kavenegar import *


@shared_task
def send_sms_quiz():
    records = Images.objects.filter(status_sms=True,parttake_suggestion__isnull=True)
    for record in records:
        api = KavenegarAPI(
            '4C6A7A6F556F6A68766F444466794278494C3738383433727239755636732B4831786E2B7653516C376C493D')
        params = {
            'receptor': record.user.tel,
            'token': record.user.slug,
            'template': 'vote'
        }
        response = api.verify_lookup(params)
        if response[0].get('cost')>10:
         record_update=Images.objects.filter(id=record.id)
         record_update.update(msgId_sms=response[0].get('messageid'))
         record_update.update(cost_sms=record.cost_sms+response[0].get('cost'))
         record_update.update(parttake_suggestion=True)
