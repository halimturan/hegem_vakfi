from django.db import models
from apps.common.mixins.audit import AuditMixin
from mptt.models import MPTTModel, TreeForeignKey
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableManager, TranslatableQuerySet
from mptt.managers import TreeManager
from mptt.querysets import TreeQuerySet


class SocialMediaSettings(AuditMixin):
    """Social Media settings are here."""
    twitter = models.CharField(max_length=100, verbose_name="Twitter")
    instagram = models.CharField(max_length=100, verbose_name="Instagram")
    facebook = models.CharField(max_length=100, verbose_name="Facebook")
    whatsapp = models.CharField(max_length=100, verbose_name="Whatsapp")

    class Meta:
        verbose_name_plural = "Sosyal Medya Ayarları"


class SiteSettings(AuditMixin):
    """General settings are here."""
    logo = models.FileField(upload_to="img/site_settings", verbose_name="Logo")
    shortcut = models.FileField(upload_to="img/site_settings", verbose_name="İkon")
    email = models.CharField(max_length=100, verbose_name="Mail")
    phone = models.CharField(max_length=50, verbose_name="Telefon", null=True, blank=True)
    address = models.CharField(max_length=500, verbose_name="Adres")
    google_maps_link = models.CharField(max_length=1000, verbose_name="Google Maps Link")

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Site Ayarları"


class MenuLocation(models.Model):
    """Menu location is here. """
    name = models.CharField(max_length=50, unique=True, verbose_name="İsim")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menü Konumları'


class CategoryQuerySet(TranslatableQuerySet, TreeQuerySet):

    def as_manager(cls):
        # make sure creating managers from querysets works.
        manager = CategoryManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager
    as_manager.queryset_only = True
    as_manager = classmethod(as_manager)


class CategoryManager(TreeManager, TranslatableManager):
    _queryset_class = CategoryQuerySet


class Menu(MPTTModel, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=250, verbose_name='Başlık'),
        link=models.CharField(max_length=200, blank=True, null=True, verbose_name="Link")
    )
    parent = TreeForeignKey("self", null=True, blank=True, related_name="children",
                            on_delete=models.CASCADE, verbose_name='Üst Menü')
    menu_location = models.ForeignKey(MenuLocation, blank=True, on_delete=models.PROTECT, null=True,
                                      verbose_name='Menü Tipi', default="Footer")
    alignment = models.SmallIntegerField(null=True, blank=True, verbose_name='Sıralama')
    target_blank = models.BooleanField(default=False, verbose_name="Yeni sayfada açılsın mı?")
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')
    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menüler'
