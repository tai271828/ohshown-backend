from re import M
from django.db import models
from django.contrib.postgres.fields import JSONField

class FootprintForm():

    id = models.AutoField(primary_key=True)
    type = models.IntegerField(choices=[(0, '糞便'), (1, '腳印'), (2, '爪痕'), (3, '食痕'), (4, '其他')], blank=True, null=True) # 痕跡類型
    type_desc = models.CharField(max_length=255, blank=True, null=True) # 痕跡類型描述
    status = models.IntegerField(choices=[(0, '新'), (1, '舊'), (2, '不清楚')]) # 新舊狀態
    status_desc = models.CharField(max_length=255, black=True, null=True) # 新舊狀態描述
    image_uploaded = models.BooleanField(default=0) # 是否上傳圖檔
    comment = models.CharField(max_length=255,blank=True, null=True) # 補充說明

