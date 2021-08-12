from django.shortcuts import render

from books.models import Publisher, Book, Author
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404

from books.decorators import allowed_groups

# Create your views here.
# class cannot have decorators, they use mixin
class AuthorCreateView(CreateView):
	model = Author
	fields = ['name']

	template_name = 'books/author_create_form.html'


class AuthorListView(ListView):
	model = Author
	context_object_name = 'authors'
	template_name = 'books/authors_list.html'


class BookCreateView(CreateView):
	model = Book
	fields = ['title', 'publisher', 'authors', 'publication_date']
	template_name = 'books/create_book.html'

class BookByPublisherView(ListView):
	model = Book
	template_name = "books/booksbypublisher.html"

	def get_queryset(self):
		self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
		return Book.objects.filter(publisher = self.publisher)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['publisher'] = self.publisher
		# Filtered books only by publisher name
		context['books'] = Book.objects.filter(publisher = self.publisher)
		return context

class PublisherDetailView(DetailView):
	model = Publisher

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


@allowed_groups(['CRUD_Author'])
def view_authors(request):
	authors = Author.objects.all()

	context = {'authors': authors}

	return render(request, 'books/view_authors.html', context)









