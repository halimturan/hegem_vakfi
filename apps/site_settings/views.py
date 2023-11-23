from apps.site_settings.models import SocialMediaSettings, SiteSettings, Menu


def context(request):
    if 'super/user' in request.path:
        return {}
    header_menu = Menu.objects.filter(menu_location__name="navbar")
    footer_menu = Menu.objects.filter(menu_location__name="footer")
    social_media_settings = SocialMediaSettings.objects.last()
    site_settings = SiteSettings.objects.last()
    return {
        "social_media_settings": social_media_settings,
        "site_settings": site_settings,
        "header_menu": header_menu,
        "footer_menu": footer_menu
    }
