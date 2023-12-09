from django.shortcuts import render
from apps.announcements.models import Announcements
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def all_announcements(request):
    q = Announcements.objects.filter(is_publish=True).order_by('order')
    if request.user.is_authenticated:
        q = Announcements.objects.all().order_by('order')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(q, 6)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'announcements/announcements.html', context={"announcements": page_obj, "count": q.count()})


def announcements_detail(request, announcements_slug):
    q = Announcements.objects.filter(slug=announcements_slug)
    return render(request, "announcements/announcement_detail.html", context={"announcements": q[0]})
