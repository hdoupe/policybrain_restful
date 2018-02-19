from django.db import models

# Create your models here.
import uuid as uuid_lib

from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class ModelInput(models.Model):
    input_specs = models.TextField(blank=True, null=False)
    specs = JSONField(default=None, blank=True, null=True)
    errors_warnings = JSONField(default=None, blank=True, null=True)

class ModelResult(models.Model):
    results = JSONField(default=None, blank=True, null=True)

class ModelMeta(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    slug = models.SlugField(unique=True)
    creation_date = models.DateTimeField(auto_now=True)
    model_input = models.ForeignKey(ModelInput, default=None)
    model_result = models.ForeignKey(ModelResult, default=None)
