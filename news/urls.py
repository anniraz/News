from django.urls import path
from news.views import *

urlpatterns = [
    path('', News_views.as_view(), name="homepage"),
    path('category/', Show_category.as_view(), name="show_category"),
    path('category/<int:pk>', Category_news.as_view(), name='category_news'),
    path('detail/<int:id>', News_detail.as_view(), name='news_detail'),
    path('POST/', AdminAddForm.as_view(), name='adminForm'),
    path('update/<int:pk>', NewsUpdate.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='news_delete'),
    path('contact_us/', ContactView.as_view(), name='contact_us')
]