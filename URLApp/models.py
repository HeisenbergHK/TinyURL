import secrets
from datetime import timedelta

from django.core.validators import URLValidator, ValidationError
from django.db import models
from django.utils import timezone


class URL(models.Model):
    original_url = models.URLField(max_length=400)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "URL"
        verbose_name_plural = "URLs"

    def __str__(self):
        return f"{self.original_url} ---> {self.short_code}"

    def clean(self):
        validator = URLValidator()
        try:
            validator(self.original_url)
        except ValidationError:
            raise ValidationError({"original_url": "Enter a valid URL"})

    @classmethod
    def generate_short_code(cls, length=6):
        while True:
            code = secrets.token_urlsafe(length)[:length]
            if not cls.objects.filter(short_code=code).exists():
                return code

    @classmethod
    def delete_expired(cls):
        expiration_date = timezone.now() - timedelta(weeks=1)
        cls.objects.filter(created_at__lt=expiration_date).delete()
