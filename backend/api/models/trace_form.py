from django.db import models

from .mixins import SoftDeleteMixin


class TraceForm(SoftDeleteMixin):
    id = models.AutoField(primary_key=True)
    trace_type = models.IntegerField(choices=[(0, '糞便'), (1, '腳印'), (2, '食痕'), (3, '折枝'),  (4, '爪痕'), (5, '其他')], blank=True, null=True, help_text='痕跡類型')
    trace_type_desc = models.CharField(max_length=255, blank=True, null=True, help_text='痕跡類型描述')
    age_type = models.IntegerField(choices=[(0, '新'), (1, '舊'), (2, '不清楚')], help_text='痕跡新舊類型')
    age_days = models.IntegerField(blank=True, null=True, help_text='痕跡出現時間估計/日')
    image_available = models.BooleanField(default=False, help_text='是否提供影像檔案')
    other_info = models.CharField(max_length=255, blank=True, null=True, help_text='其他補充資訊')
