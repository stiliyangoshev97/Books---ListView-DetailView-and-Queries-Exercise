from django.shortcuts import render

from django.views.generic import ListView

# from beats_app.models import Beat, Label

from django.shortcuts import get_object_or_404

from django.views.generic.edit import CreateView

from django import forms

# Create your views here.

'''

class LabelListView(ListView):
	model = Label
	context_object_name = 'labels'
	template_name = 'beats_app/labels.html'

class LabelBeatListView(ListView):
	template_name = 'beats_app/beats_by_label.html'

	def get_queryset(self):
		self.label = get_object_or_404(Label, name=self.kwargs['label'])
		return Beat.objects.filter(label = self.label)

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)

		# Add in the label
		context['label'] = self.label
		context['beats'] = Beat.objects.filter(label = self.label)
		return context

class LabelCreateView(CreateView):
	model = Label
	fields = ['name', 'owner']
	template_name = 'beats_app/create_label.html'
	widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control'}),
		'owner': forms.TextInput(attrs={'class': 'form-control'})
		}

	def form_valid(self, form):
		self.object.beat = Beat.objects.all()
		return super().form_valid(form)



 def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



'''