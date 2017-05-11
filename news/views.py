# encoding: utf-8
from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from .models import Article, Feed
from .forms import FeedForm, UserLoginForm
from django.shortcuts import redirect
import datetime, re, unicodedata
from .util import slug_to_practice_area, slugify, feed_update
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import feedparser

# Create your views here.

def update(request):
    feed_updated_list, article_updated_list = feed_update()
    lists = zip(feed_updated_list, article_updated_list)
    for l,s in lists:
        print l
        for i in s:
            print i
    return render(request, 'news/update.html', {'lists': lists})

def test(request):
    return render(request, 'news/test.html', {})

def home(request):
    return render(request, 'news/home.html', {})

def login_view(request):
    try:
        next = request.GET['next']
    except:
        next = '/'
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        try:
            if next:
                return redirect(next)
        except:
            pass
    return render(request, 'news/login.html', {"form":form, "title":title})

def logout_view(request):
    logout(request)
    return redirect(articles)


def articles(request, slug=0):
    if Article.objects.filter(authorSlug=slug):
        articles = Article.objects.all().filter(authorSlug=slug).order_by('-publication_date')
    elif slug_to_practice_area(slug):
        articles = Article.objects.all().filter(practiceArea=slug_to_practice_area(slug)).order_by('-publication_date')
    else:
        articles = Article.objects.all().order_by('-publication_date')
        art_num = len(articles)
        print art_num
    #pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    index = users.number - 1  # edited to something easier without index
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'news/articles.html', {'articles': articles, 'users': users, 'page_range': page_range,})

def feeds_list(request):
    feeds = Feed.objects.all()
    areas = Feed.objects.values('practiceArea').distinct()
    return render(request, 'news/feeds_list.html', {'feeds': feeds, 'areas': areas})

@login_required
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
                try:
                    feed.etag = feedData.etag
                except:
                    pass
                try:
                    feed.modified = feedData.modified_parsed
                except:
                    pass
                feed.save()

                c = 'https?://(.*?)/'

                for entry in feedData.entries:
                    article = Article()
                    try:
                        article.title = entry.title
                    except:
                        article.title = entry.title + "NAME ISSUE!!!!!!!!!!!!"
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
