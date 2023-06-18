from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse
from blog.forms import BlogCreateForm
from django.core.paginator import Paginator

# Create your views here.



def home_page(request):
    return render(request, 'index.html')


def aboutPage(request):
    return render(request, 'about.html')


def aboutUsPage(request):
    return render(request, 'about_us.html')


def blogPage(request):
    return render(request, 'blog.html')


def bloglist(request):
    objects = Blog.objects.all()
    paginator = Paginator(objects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'blog': objects,
        'page_obj': page_obj
    }
    return render(request, 'blog.html', context)


def blog_detail(request, id):
    try:
        instance = get_object_or_404(Blog, id=id)
    except Exception:
        return redirect('blog:main_blog')
    #uniq_url = reverse('blog:blog_details', args=[id])

    return render(request, 'detail_blog.html', {'obj':instance})


def blog_create(request):
    if request.method == 'POST':
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:main_blog')
    else:
        form = BlogCreateForm()
    return render(request, 'form_AddArticle.html', {'form': form})