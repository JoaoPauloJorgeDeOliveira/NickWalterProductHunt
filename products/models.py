from django.db import models
from django.contrib.auth.models import User  # Importing model User that Django already has.


class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d/%m/%Y')

    def __str__(self):  # Now, in admin page, blog title displays 'tile'
        return self.title
