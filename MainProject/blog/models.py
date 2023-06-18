from django.db import models

# Create your models here.

def uploads_url(instance, filename):
    return f'images/{instance.theme}/{filename}'


class Blog(models.Model):
    title = models.CharField(max_length=55)
    theme = models.CharField(max_length=30)
    description = models.TextField()
    all_description = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=35)
    image = models.ImageField(null=True, blank=True, upload_to=uploads_url,
                              height_field='height_field', width_field='width_field' )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:blog_details', args=[self.id])
        # return f'detail/{self.id}'
