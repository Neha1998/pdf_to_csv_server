from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .settings import MEDIA_URL,  BASE_DIR
from .utils import pdf_to_csv
#from .forms import BookForm
#from .models import Book


# class Home(TemplateView):
#     template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        
        pdf_to_csv(BASE_DIR+MEDIA_URL+name)
        context['url'] = fs.url(name).replace(".pdf",".csv")
    return render(request, 'index.html', context)

# def upload_book(request):
#     if request.method == 'POST':
#         form = PdfForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = PdfForm()
#     return render(request, 'upload_book.html', {
#         'form': form
#     })