from django.shortcuts import render
from apps.news.models import News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def all_news(request):
    q = News.objects.all().order_by('created_at')
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
    return render(request, 'news/news.html', context={"news": page_obj, "count": len(q)})


def news_detail(request, news_slug):
    q = News.objects.filter(slug=news_slug)
    return render(request, "news/news_detail.html", context={"news": q[0]})

