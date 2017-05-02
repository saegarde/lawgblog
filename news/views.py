# encoding: utf-8
from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect
import datetime, re, unicodedata
from .util import slug_to_practice_area, slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import feedparser

# Create your views here.


def home(request):
    return render(request, 'news/home.html', {})

def articles(request, slug=0):
    if Article.objects.filter(authorSlug=slug):
        articles = Article.objects.all().filter(authorSlug=slug)
    elif slug_to_practice_area(slug):
        articles = Article.objects.all().filter(practiceArea=slug_to_practice_area(slug))
    else:
        articles = Article.objects.all().order_by('-publication_date')
#    rows = [articles[x:x+2] for x in range(0, len(articles), 1)]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'news/articles.html', {'articles': articles, 'users': users})

def feeds_list(request):
    feeds = Feed.objects.all()
    areas = Feed.objects.values('practiceArea').distinct()
    return render(request, 'news/feeds_list.html', {'feeds': feeds, 'areas': areas})

def new_feed(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            existingFeed = Feed.objects.filter(url = feed.url)
            if len(existingFeed) == 0:
                feedData = feedparser.parse(feed.url)

            # set some fields
                feed.title = feedData.feed.title
                feed.save()

                c = 'https?://(.*?)/'

                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    try:
                        article.domain = re.findall(c,entry.link)[0]
                    except:
                        article.domain = entry.link
                    if feed.author:
                        article.author = feed.author
                    else:
                        article.author = entry.author
                    article.authorSlug = slugify(article.author)
                    #description script
                    try:
                        remove = re.findall('<p>(The post.*?)</p>', entry.description)[0]
                        article.description = entry.description.replace(remove,'')
                    except:
                        try:
                            remove = re.findall('<p>(The post.*?)</p>', entry.description)[0]
                        except:
                            article.description = entry.description
                        #end descripton script
                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d')
                    article.publication_date = dateString
                    article.feed = feed
                    article.practiceArea = feed.practiceArea
                    article.practiceAreaSlug = feed.practiceArea.replace(" ", "_").lower()
                    article.save()
            return redirect('news/feeds.html')
    else:
        form = FeedForm()
    return render(request, 'news/new_feed.html', {'form': form})
