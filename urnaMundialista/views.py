# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from urnaMundialista.models import Jugadores
from django.core.urlresolvers import reverse_lazy

# Create your views here.
@login_required
def base(request):
    return render(request , "base.html")

def jugador_list(request):
    jugador_list = Jugador.objects.all()
    context = {'object_list': jugador_list}
    template_name='urnaMundialista/jugadores_detail.html'
    return render(request,'urnaMundialista/jugadores_list.html', context)

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class JugadorListView(LoginRequiredMixin, ListView):
    model = Jugadores

class JugadorDetailView(LoginRequiredMixin, DetailView):
    model = Jugadores

class JugadorUpdate(UpdateView):
 login_required = True
 model = Jugadores
 fields = '__all__'

class JugadorCreate(CreateView):
 login_required = True
 model = Jugadores
 fields = '__all__'

class JugadorDelete(DeleteView):
 login_required = True
 model = Jugadores
 success_url = reverse_lazy('jugadores-list')

