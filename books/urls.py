from django.urls import path

from books import views

from django.conf.urls import url

app_name = 'books'

urlpatterns = [

    path('create_author/', views.AuthorCreateView.as_view(), name="create_author"),
    path('authors_list/', views.AuthorListView.as_view(), name="authors_list"),
    path('create_book/', views.BookCreateView.as_view(), name="create_book"),
    path('booksbypublisher/<publisher>', views.BookByPublisherView.as_view(), name = 'booksbypublisher'),
    path('publisherdetailview/<pk>/', views.PublisherDetailView.as_view(), name='publisherdetailview'),
    
]