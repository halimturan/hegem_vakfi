from django.db import models
from apps.common.mixins.audit import AuditMixin
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from autoslug import AutoSlugField


class Announcements(AuditMixin, TranslatableModel):
    """Announcements for main page."""
    translations = TranslatedFields(
        text=RichTextField(verbose_name="Metin"),
        title=RichTextField(verbose_name="Başlık"),
    )
    order = models.SmallIntegerField(verbose_name="Sıra")
    file = models.FileField(verbose_name="Dosya", upload_to="announcements/file")
    name = models.CharField(verbose_name="İsim", max_length=300)
    image = models.ImageField(verbose_name="Resim", upload_to="announcements/img")
    slug = AutoSlugField(always_update=True, populate_from='name', unique=True, verbose_name="Slug")
    is_publish = models.BooleanField(verbose_name="Yayınlansın mı?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Duyurular"
