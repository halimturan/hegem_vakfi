from apps.site_settings.models import SocialMediaSettings, SiteSettings, Menu


def context(request):
    if 'super/user' in request.path:
        return {}
    header_menu = Menu.objects.filter(menu_location__name="navbar").order_by('alignment')
    footer_menu = Menu.objects.filter(menu_location__name="footer").order_by('alignment')
    social_media_settings = SocialMediaSettings.objects.last()
    site_settings = SiteSettings.objects.last()
    return {
        "social_media_settings": social_media_settings,
        "site_settings": site_settings,
        "header_menu": header_menu,
        "footer_menu": footer_menu
    }
