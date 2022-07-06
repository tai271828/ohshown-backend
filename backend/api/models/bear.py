from django.db import models

from .mixins import SoftDeleteMixin


class Bear(SoftDeleteMixin):
    id = models.AutoField(primary_key=True)
    bear_age = models.IntegerField(choices=[(0, '成熊'), (1, '幼熊'), (3, '不清楚')], default=0, help_text='黑熊年齡')
    bear_size = models.IntegerField(choices=[(0, '10-30cm'), (1, '30-50cm'), (2, '50-70cm'), (3, '70-100cm'), (4, '100-150cm'), (5, '>150cm'), (6, '不清楚')], help_text='黑熊體型大小')
    bear_sex = models.IntegerField(choices=[(0, '公'), (1, '母'), (2, '不清楚')], help_text='黑熊性別')
    bear_feature = models.CharField(blank=True, max_length=255, null=True, help_text='黑熊特徵')
