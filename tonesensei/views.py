# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.response import TemplateResponse
from django.urls import reverse_lazy

from tonesensei.models import Characters

#Create view
class ViewChar(ListView):
    query_results = Characters.objects.all

class ViewChar2(DetailView):
    model = Characters

class CharCreate(CreateView):
    model = Characters
    fields = ['languageCharacter', 'answer']
#    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Characters
    fields = ['languageCharacter', 'answer']
#    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Characters
#    success_url = reverse_lazy('book_list')    


def index(request):
#    data = Characters.objects.all()
    return TemplateResponse(request, 'tones/index.html',{"test":"hello"})
