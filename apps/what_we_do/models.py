from django.db import models
from apps.common.mixins.audit import AuditMixin
from parler.models import TranslatableModel, TranslatedFields


class Editions(AuditMixin):
    name = models.CharField(verbose_name="İsim", max_length=300)
    image = models.ImageField(upload_to="img/what_we_do/editions", verbose_name="Resim", null=True, blank=True)
    writer = models.CharField(verbose_name="Yazar", max_length=300)
    year = models.SmallIntegerField(verbose_name="Yıl", null=True, blank=True)
    publisher = models.CharField(verbose_name="Yayın Evi", max_length=300, null=True, blank=True)
    is_publish = models.BooleanField(verbose_name="Yayınlansın mı?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Yayınlar"


class Reports(AuditMixin, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="İsim")
    )
    order = models.SmallIntegerField(verbose_name="Sıra")
    attachment = models.FileField(verbose_name="Ek Dosya", upload_to="img/what_we_do/reports", null=True, blank=True)
    is_publish = models.BooleanField(verbose_name="Yayınlansın mı?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Raporlar"


class Projects(AuditMixin, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="İsim"),
        description=models.CharField(max_length=300, verbose_name="Açıklama")
    )
    order = models.SmallIntegerField(verbose_name="Sıra")
    attachment = models.FileField(verbose_name="Ek Dosya", upload_to="img/what_we_do/reports", null=True, blank=True)
    is_publish = models.BooleanField(verbose_name="Yayınlansın mı?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projeler"
