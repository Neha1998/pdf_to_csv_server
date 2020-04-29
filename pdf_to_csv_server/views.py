from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .settings import MEDIA_URL,  BASE_DIR
from .utils import pdf_to_csv
from .forms import PdfForm
import csv
#from .models import Book


class InsensitiveDictReader(csv.DictReader):
    # This class overrides the csv.fieldnames property, which converts all fieldnames without leading and trailing spaces and to lower case.

    @property
    def fieldnames(self):
        return [field.strip().lower() for field in csv.DictReader.fieldnames.fget(self)]

    def next(self):
        return InsensitiveDict(csv.DictReader.next(self))

class InsensitiveDict(dict):
    # This class overrides the __getitem__ method to automatically strip() and lower() the input key

    def __getitem__(self, key):
        return dict.__getitem__(self, key.strip().lower())


def save_data(filename):
        with open(filename) as f:
            reader = InsensitiveDictReader(f)


def upload(request):
    context = {}
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            
            pdf_to_csv(BASE_DIR+MEDIA_URL+name)
            context['url'] = fs.url(name).replace(".pdf",".csv")
            save_data(BASE_DIR+context['url'])
            return render(request, 'index.html', context)
    else:
        form = PdfForm()
    return render(request, 'index.html', {'form': form}, context)