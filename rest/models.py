import uuid
from django.db import models


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField()

    def _str_(self):
        return self.name
