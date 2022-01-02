class DocumentDisplayStatusConst:
    REPORTED = "已檢舉"
    AUDIT_SCHEDULED = "已排程稽查"
    COMMUNICATION_PERIOD = "陳述意見期"
    WORK_STOPPED = "已勒令停工"
    POWER_OUTING = "已發函斷電"
    POWER_OUTED = "已斷電"
    DEMOLITION_SCHEDULED = "已排程拆除"
    DEMOLISHED = "已拆除"
    WAITING_FOR_NEW_EVIDENCE = "等待新事證"
    IN_PROGRESS = "處理中"
    OPEN = "未處理"

    STATUS_LIST = [REPORTED,
                   AUDIT_SCHEDULED,
                   COMMUNICATION_PERIOD,
                   WORK_STOPPED,
                   POWER_OUTING,
                   DEMOLITION_SCHEDULED,
                   DEMOLISHED,
                   WAITING_FOR_NEW_EVIDENCE]

    STATUS_LIST_ENRICHMENT = STATUS_LIST + [IN_PROGRESS]


class OhshownEventConst:
    TYPE_LIST = [
        ('2-1', '痕跡: 爪痕'),
        ('2-2', '痕跡: 排遺'),
        ('2-3', '痕跡: 植物折痕'),
        ('3', '人熊衝突現場痕跡 - 雞舍'),
        ('4', '人熊衝突現場痕跡 - 果園'),
        ('5', '人熊衝突現場痕跡 - 其他'),
        ('6', '死亡'),
        ('7', '現場目擊 - 不確定'),
        ('8', '現場目擊 - 確定'),
        ('9', '其他')
    ]
