from django.db import models


class AuthorManager(models.Manager):
    pass


class Author(models.Model):
    objects = AuthorManager()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class BookManager(models.Manager):
    pass


class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, related_name='authors')

    def __unicode__(self):
        return self.title


class Login(models.Model):
        username=models.CharField(max_length=30)
        password=models.CharField(max_length=30)


from django.db import models





class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField( max_length=100)
    style = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)