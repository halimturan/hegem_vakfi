from django.db import models
from apps.common.mixins.audit import AuditMixin
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from autoslug import AutoSlugField


class Images(AuditMixin):
    img = models.ImageField(verbose_name="Resim", upload_to="img/images")

    class Meta:
        verbose_name_plural = "Resimler"


class News(AuditMixin, TranslatableModel):
    """News for main page."""
    translations = TranslatedFields(
        text=RichTextField(verbose_name="Metin"),
        title=RichTextField(verbose_name="Başlık"),
    )
    name = models.CharField(verbose_name="İsim", max_length=300)
    image = models.ImageField(verbose_name="Resim", upload_to="img/news")
    slug = AutoSlugField(always_update=True, populate_from='name', unique=True, verbose_name="Slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Haberler"
