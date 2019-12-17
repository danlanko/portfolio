from django.shortcuts import render_to_response
from models import Blog_Categorie,Blog,Portfolio_Categorie,Portfolio,Testimonial,Technologies, Studying
from update_site.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from Serializers import Update_SiteSerializer

# Create your views here.
class Update_SiteViewset(viewsets.ModelViewSet):

    queryset = Blog.objects.all().order_by('date')
    serializer_class = Update_SiteSerializer

def homepage(request):
    tech = Technologies.objects.all()
    study = Studying.objects.all()
    work_cat = Portfolio_Categorie.objects.all()
    work = Portfolio.objects.all()
    all_blog = Blog.objects.all()
    list_blog = list(all_blog)
    testi = Testimonial.objects.all()
    lengh_test = len(testi)
    study_lenght = len(study)
    lenght_blog =len(all_blog)
    latest_blog1 = list(list_blog[:-lenght_blog-1:-1])
    latest_blog = latest_blog1[:4]

    form = ContactForm(request.POST)

    return render_to_response('index.html',{'tech':tech,'study':study,'study_lenght':study_lenght,'work_cat':work_cat,
                                            'work':work,'testimonial':testi,'form':form,'latest_blog':latest_blog,'lengh_test':lengh_test,'lenght_blog':lenght_blog})

def blog_single(request,blog_id):
    all_blog = Blog.objects.filter(id=blog_id)
    blog_cat = Blog_Categorie.objects.all()
    return render_to_response('blog_single.html',{'blog': all_blog,'blog_cat':blog_cat})

def blog(request):
    blog_cat = Blog_Categorie.objects.all()
    all_blog = Blog.objects.all()
    lenght_blog = len(all_blog)
    list_blog = list(all_blog)
    latest_blog = list_blog[:-lenght_blog - 1:-1]

    page = request.GET.get('page')
    paginator = Paginator(latest_blog, 16)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    return render_to_response('blog.html',{'blog':all_blog,'blog_cat':blog_cat,'blog_p':blog})

def category_blog(request,cat_id):
    blog_cat = Blog_Categorie.objects.all()
    filter_cat = Blog.objects.filter(category_id=cat_id)
    blog_cat_image = Blog_Categorie.objects.filter(id=cat_id)
    lenght_blog = len(filter_cat)
    list_blog = list(filter_cat)
    latest_blog = list_blog[:-lenght_blog -1:-1]

    page = request.GET.get('page')
    paginator = Paginator(latest_blog, 16)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)


    return render_to_response('category_blog.html', {'blog': latest_blog,'blog_cat':blog_cat,'blog_cat_image':blog_cat_image,'blog_p':blog})

def base(request):
    blog_cat = Blog_Categorie.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render_to_response('base.html',{'form': form,'blog_cat':blog_cat})
        else:
            pass
    else:
        form = ContactForm
        return render_to_response('base.html', {'form': form,'blog_cat':blog_cat,})





