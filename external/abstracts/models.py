from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid.uuid4,
                          help_text="Identity of a object")
    is_active = models.BooleanField(default=True,
                                    blank=True,
                                    null=True,
                                    help_text="Activity of the object")
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="when item is created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="when item is updated"
    )

    objects = models.Manager()

    class Meta:
        abstract = True
