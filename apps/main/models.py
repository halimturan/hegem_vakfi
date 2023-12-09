from django.db import models
from apps.common.mixins.audit import AuditMixin, TimeStampMixin
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField


class MainSlider(AuditMixin, TranslatableModel):
    """Slider for main page."""
    alignment_choices = (('sag', 'Sağ'), ('sol', 'Sol'))
    translations = TranslatedFields(
        text=RichTextField(verbose_name="Metin"),
        button_text=models.CharField(max_length=50, verbose_name="Buton Yazısı", null=True, blank=True),
        button_url=models.CharField(max_length=100, verbose_name="URL", null=True, blank=True)
    )
    order = models.SmallIntegerField(verbose_name="Sıra")
    image = models.ImageField(upload_to="img/main_slider", verbose_name="Resim")
    image_alignment = models.CharField(verbose_name="Resim Konumu", max_length=10, choices=alignment_choices)
    name = models.CharField(max_length=100, verbose_name="İsim")
    is_publish = models.BooleanField(verbose_name="Yayınlansın mı?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ana Slider"


class Contact(TimeStampMixin):
    name = models.CharField(max_length=100, verbose_name="İsim")
    email = models.CharField(max_length=100, verbose_name="Email")
    subject = models.CharField(max_length=300, verbose_name="Konu")
    message = models.CharField(max_length=3000, verbose_name="Mesaj")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "İletişim"


class Pages(AuditMixin, TranslatableModel):
    """News for main page."""
    translations = TranslatedFields(
        text=RichTextUploadingField(verbose_name="Metin"),
        title=RichTextField(verbose_name="Başlık"),
    )
    banner_img = models.FileField(verbose_name="Banner Resmi", upload_to="img/pages", null=True, blank=True)
    name = models.CharField(verbose_name="İsim", max_length=300)
    slug = AutoSlugField(always_update=True, populate_from='name', unique=True, verbose_name="Slug")
    is_publish = models.BooleanField(verbose_name="Yayınlansın mı?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sayfalar"
