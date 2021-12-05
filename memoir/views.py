from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import DetailView
from .models import Article, Banner, Education, Skill, Project, SocialMedia
from .forms import ContactForm


def home_view(request):
    banners = Banner.objects.all()
    articles = Article.objects.all()
    studies = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    medias = SocialMedia.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.info(request, "Your message is accepted. Thank you.")
            return redirect("/")
    else:
        contact_form = ContactForm()

    context = {
        'banners': banners,
        'articles': articles,
        'studies': studies,
        'skills': skills,
        'projects': projects,
        'contact_form': contact_form,
        'medias': medias
    }
    return render(request, 'index.html', context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

