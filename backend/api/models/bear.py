from statistics import mode
from django.db import models
from django.contrib.postgres.fields import JSONField

class Bear():

    id = models.AutoField(primary_key=True)
    form_id = models.OneToOneField('shown_form',on_delete=models.deletion.PROTECT ) # 「目擊黑熊」表單id
    bear_age = models.IntegerField(choices=[(0, '成熊'), (1, '幼熊')], default=0) # 黑熊年齡
    bear_size = models.IntegerField(choices=[(0, '清楚'), (1, '不清楚')]) # 是否回報黑熊大小
    bear_size_number = models.FloatField(blank=True, null=True) # 黑熊體型大小
    bear_sex = models.IntegerField(choices=[(0, '公'), (1, '母'), (2, '不清楚')]) # 黑熊性別
    bear_feature = models.CharField(blank=True, max_length=50, null=True) # 黑熊特徵
