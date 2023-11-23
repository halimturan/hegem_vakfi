from django.shortcuts import render
from apps.what_we_do.models import Editions, Projects, Reports
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def editions(request):
    q = Editions.objects.all().order_by('year')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(q, 9)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'what_we_do/editions.html', context={"editions": page_obj})


def projects(request):
    q = Projects.objects.all().order_by('order')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(q, 9)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'what_we_do/projects.html', context={"projects": page_obj})


def reports(request):
    q = Reports.objects.all().order_by('order')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(q, 9)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'what_we_do/reports.html', context={"reports": page_obj, "count": len(q)})
