from django.db import models

# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    practiceArea = models.CharField(max_length=100)
    author = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    etag = models.CharField(max_length=50)
    modified = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.title


practice_area_choices = (

    ("Trusts and Estates", "Trusts and Estates"),
    ("Criminal Law", "Criminal Law"),
    ("Real Estate Law", "Real Estate Law"),
    ("Tax Law", "Tax Law"),
    ("Family Law", "Family Law"),
    ("Personal Injury Law", "Personal Injury Law"),
    ("Labor and Employment Law", "Labor and Employment Law"),
    ("Business Law", "Business Law"),
)

class Article(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    authorSlug = models.CharField(max_length=200)
    url = models.URLField()
    domain = models.URLField()
    practiceArea = models.CharField(max_length=30, choices = practice_area_choices)
    practiceAreaSlug = models.CharField(max_length=30)
    description = models.TextField()
    publication_date = models.DateField()


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
