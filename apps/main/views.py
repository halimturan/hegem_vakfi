from django.shortcuts import render
from apps.main.models import MainSlider, Pages
from apps.news.models import News
from apps.what_we_do.models import Editions, Projects, Reports
from apps.main.forms import ContactForm


def index(request):
    main_slider = MainSlider.objects.all().order_by('order')
    news = News.objects.all().order_by('-created_at')[:3]
    editions = Editions.objects.filter(is_publish=True)
    projects = Projects.objects.filter(is_publish=True)
    reports = Reports.objects.filter(is_publish=True)
    context = {
        "main_slider": main_slider,
        "news": news,
        "editions": editions.count(),
        "projects": projects.count(),
        "reports": reports.count()
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    return render(request, "contact.html")


def pages(request, slug):
    q = Pages.objects.filter(slug=slug, is_publish=True)
    if request.user.is_authenticated:
        q = Pages.objects.filter(slug=slug)
    return render(request, 'pages.html', context={"page": q})
