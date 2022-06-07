import uuid

from django.db import models

from .mixins import SoftDeleteMixin


class FootprintForm(SoftDeleteMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
    )
    type = models.IntegerField(choices=[(0, '糞便'), (1, '腳印'), (2, '爪痕'), (3, '食痕'), (4, '其他')], blank=True, null=True)  # 痕跡類型
    type_desc = models.CharField(max_length=255, blank=True, null=True)  # 痕跡類型描述
    status = models.IntegerField(choices=[(0, '新'), (1, '舊'), (2, '不清楚')])  # 新舊狀態
    status_desc = models.CharField(max_length=255, blank=True, null=True)  # 新舊狀態描述
    image_uploaded = models.BooleanField(default=False)  # 是否上傳圖檔
