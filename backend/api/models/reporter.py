from django.db import models
from django.contrib.postgres.fields import JSONField

class Reporter():

    id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50, blank=True, null=True) # 聯絡者姓名
    contact_phone = models.CharField (max_length=10, blank=True, null=True) # 聯絡電話
    contact_mail = models.EmailField(max_length=255, blank=True, null=True) # 聯絡信箱

