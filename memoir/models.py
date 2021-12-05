from django.db import models 
from django.shortcuts import reverse
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from PIL import Image 


class Banner(models.Model):
    image = models.ImageField(upload_to="banner_img/")
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    hire_me_url = models.CharField(max_length=600)
    read_more_url = models.CharField(max_length=600)

    class Meta:
        verbose_name_plural = '1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 1600 or img.width > 1700:
            output_size = (1600, 1700)      
            img.thumbnail(output_size)
            img.save(self.image.path)


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="article_img/")
    date_posted = models.DateTimeField(auto_now_add=True)
    description = RichTextField()
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = '2. Articles'

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.image.url))

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 1100 or img.width > 1300:
            output_size = (1100, 1300)      
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={'slug': self.slug})


class Education(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ongoing_degree = models.CharField(max_length=300)
    ongoing_institute = models.CharField(max_length=400)
    degree = models.CharField(max_length=300)
    institute = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = '3. Education'

    def __str__(self):
        return self.title


class Skill(models.Model):
    skill_name = models.CharField(max_length=200)
    percentage_of_expertise = models.IntegerField()
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '4. Skills'

    def __str__(self):
        return self.skill_name


class Project(models.Model):
    project_name = models.CharField(max_length=300)
    project_url = models.CharField(max_length=500)
    image = models.ImageField(upload_to="project_img/")
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = '5. Projects'

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.image.url))

    def __str__(self):
        return self.project_name

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 1100 or img.width > 1300:
            output_size = (1100, 1300)      
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={'slug': self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = '6. Contacts'

    def __str__(self):
        return self.name  


class SocialMedia(models.Model):
    social_media = models.CharField(max_length=255)
    social_media_url = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = '7. Social media'

    def __str__(self):
        return self.social_media