from unidecode import unidecode
import re
import feedparser, datetime
from news.models import Article, Feed

def feed_update():
    feed_updated_list = []
    article_updated_list = []
    feeds = Feed.objects.all()
    for feed in feeds:
        try:
            feed_update = feedparser.parse(feed.url, etag=feed.etag)
        except:
            print feed.title, "Does not have an etag!!!!!!!!!!!!!!!!!!"
        title_list = []
        if feed_update.status != 304:
            article_inner = []
            feed_updated_list.append(feed.title)
            feeds = Article.objects.all()
            for i in feeds:
                title_list.append(i.title)
            for entry in feed_update.entries:
                if entry.title not in title_list:
                    article_inner.append(entry.title)
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    c = 'https?://(.*?)/'
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
            article_updated_list.append(article_inner)
            try:
                feed.etag = feed_update.etag
            except:
                pass
            feed.save()
    return feed_updated_list, article_updated_list


def slug_to_practice_area(slug):

    if slug == "trusts_and_estates":
        return "Trusts and Estates"
    elif slug == "criminal":
        return "Criminal Law"
    elif slug == "real_estate":
        return "Real Estate Law"
    elif slug == "tax":
        return "Tax Law"
    elif slug == "family_law":
        return "Family Law"
    elif slug == "personal_injury":
        return "Personal Injury Law"
    elif slug == "litigation":
        return "Litigation"
    elif slug == "labor_law":
        return "Labor and Employment"
    elif slug == "business_law":
        return "Business Law"
    elif slug == "health_law":
        return "Health Care Law"
    else:
        return False


def slugify(s):
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')
    s = re.sub('\W', '', s)
    s = s.replace('_', ' ')
    s = re.sub('\s+', ' ', s)
    s = s.strip()
    s = s.replace(' ', '-')
    return s


'''
Criminal Law
http://rss.justia.com/TampaBayCriminalDefenseLawyerBlogCom
http://rss.justia.com/VSjiCom
http://rss.justia.com/FloridaCriminalLawBlogCom
http://devlaming.com/feed

Family Law
http://www.fladivorcelawblog.com/feed/

Injury Law
http://www.fort-lauderdale-injury-lawyer-blog.com/feed
https://www.searcylaw.com/blog/feed/

Estate Planning
http://www.florida-probate-lawyer.com/probate/feed/

Trusts and Estates
http://www.assetprotectionfl.com/feed/
https://www.ginsbergshulman.com/blog/feed/
http://www.deanmead.com/category/trusts-estates/feed
http://gassmanlaw.com/feed/

Personal Injury Law
http://rss.justia.com/FloridaPersonalInjuryLawyerBlogCom

Tax Law
http://www.deanmead.com/category/tax/feed/
http://rubinontax.floridatax.com/feeds/posts/default

Real Estate Law
http://www.deanmead.com/category/water-law/feed
'''
