from tortoise import fields, models


class EventEntity(models.Model):
    id = fields.IntField(primary_key=True)
    event_id = fields.CharField(max_length=256)
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)
    status = fields.CharField(max_length=256)
    severity = fields.CharField(max_length=256)
    tool = fields.CharField(max_length=256)
    event_type = fields.CharField(max_length=256)
    description = fields.CharField(max_length=512)
    details = fields.JSONField()

    class Meta:
        table_name = 'event'
