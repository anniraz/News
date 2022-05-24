from django.shortcuts import get_object_or_404, redirect, render
from django.urls import is_valid_path, reverse_lazy
from news.forms import AdminForm, ContactForm
from news.models import News, Category, SocialSidebar, Tags
import datetime
from django.views import generic
from django.db.models import Q
from services.send_email import send_email

class NewsDelete(generic.DeleteView):
    model=News
    template_name='include/news_delete.html'
    success_url='/'
    success_url=reverse_lazy('homepage')

    

class NewsUpdate(generic.UpdateView):
    model=News
    template_name='include/adminForm.html'
    form_class = AdminForm

class Show_category(generic.ListView):
    model=Category
    template_name='include/category.html'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_all']=News.objects.all()
        context['tags']=Tags.objects.all()
        context['category_all']=Category.objects.all()
        return context


class News_views(generic.ListView):
    model=News
    template_name='include/main.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_slider']=News.objects.all()[:3]
        context['world_news_slider']=News.objects.filter(category__name='Мировые новости')[:4]
        context['category_all']=Category.objects.all()[:4]
        context['now']=datetime.datetime.now()
        context['tags']=Tags.objects.all()
        context['news_all']=News.objects.all()
        context['social']=SocialSidebar.objects.all()
        return context
    

    # def form_valid(self,request):
    #     word = request.GET.get('search_word')
    #     news_all = News.objects.filter(Q(title__icontains=word))
    #     return self.form_valid(news_all)


class News_detail(generic.DetailView):
    model=News
    template_name='include/news_detail.html'
    pk_url_kwarg='id'
    context_object_name='news_all'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_all']=Category.objects.all()
        context['tags']=Tags.objects.all()
        context['social']=SocialSidebar.objects.all()



        # context['news_all']=News.objects.all()
        return context



# class Category_news(generic.DetailView):
#     model=Category
#     template_name='include/category.html'
#     # pk_url_kwarg='id'
#     # context_object_name='news_all'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category_all']=Category.objects.all()
#         context['news_all']=News.objects.all()
#         context['tags']=Tags.objects.all()
#         context['social']=SocialSidebar.objects.all()


#         return context

    # def get_queryset(self):
    #     return News.objects.filter(category__id=self.kwargs['id'])


class Category_news(generic.DetailView):
    model=Category
    template_name='include/category.html'
    # pk_url_kwarg='id' 
    context_object_name='category_all'

  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_all']=Category.objects.all()
        context['news_all']=News.objects.all()
        context['tags']=Tags.objects.all()
        context['social']=SocialSidebar.objects.all()
        return context


class AdminAddForm(generic.CreateView):
    form_class=AdminForm
    template_name='include/adminForm.html'
    success_url=reverse_lazy('homepage')

    # form=AdminForm()

    # def get_context_data(self,*,object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form']=self.form
    #     return context

class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'include/contact_us.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        send_email(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['subject'],
                form.cleaned_data['message']
                )
        return super().form_valid(form)



# def contact_us(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             send_email(
#                 form.cleaned_data['name'],
#                 form.cleaned_data['email'],
#                 form.cleaned_data['subject'],
#                 form.cleaned_data['message']
#                 )
            
#     else:
#         form = ContactForm()
#     return render(request, 'include/contact_us.html', {'form': form})  



# def adminAddForm(request):
#     if request.method == 'POST':
#         form = AdminForm(request.POST, request.FILES)
       
#         if form.is_valid():
#             # print(form.cleaned_data)
#                 form.save()
#                 return redirect('homepage')
        
#     else:
#         form = AdminForm()

#     return render(request, 'include/adminForm.html', {'form':form})




# def news_views(request):

#     if 'search_button' in request.GET:
#         word = request.GET.get('search_word')
#         news_all = News.objects.filter(Q(title__icontains=word))
#         return render(request, 'include/main.html', {'news_slider': news_all})
#     else:
#         news_all = News.objects.all()[:4]
#         news_slider = News.objects.all()[:3]

#         world_news_slider = News.objects.filter(category__name='Мировые новости')[:4]
#         category_all = Category.objects.all()[:4]
#         now= datetime.datetime.now()
#         tags=Tags.objects.all()

#         context = {
#             'news_all':news_all,
#             'news_slider':news_slider,
#             'world_news_slider':world_news_slider,
#             'category_all':category_all, 
#             'now':now,
#             'tags':tags
            
#         }
#     return render(request, 'include/main.html', context)









