from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy

from os.path import join
from django.conf import settings

import numpy as np, pandas as pd
import matplotlib.pyplot as plt

from .forms import InputForm, StatesForm
from .models import STATES_DICT

import geopandas as gpd, folium
from geopy import Nominatim

import seaborn as sns
sns.set(font_scale = 1.7)

from io import BytesIO

# abc: Welcome page
def index(request):
    params = {"title" : "Welcome",
        }
    return render(request, 'welcome.html', params)

# abc: csv table with all our Data???
def csv(request, year = None):


   filename = join(settings.STATIC_ROOT, 'myapp/master.csv')

   df = pd.read_csv(filename)

  # if year: df = df[df["Year"] == int(year)]

   table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
   table = table.replace('border="1"','border="0"')
   table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

   return HttpResponse(table)

# abc: After selecting the state you are interested in, displays a table with all the info
from .forms import InputForm
def display_table(request):

    state = request.GET.get('state', 'Aguascalientes')

    filename = join(settings.STATIC_ROOT, 'home/master.csv')

    df = pd.read_csv(filename)

    df = df[df["NOM_ENT"] == state]
    if not df.size: return HttpResponse("No such state!")

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'title' : state,
              'form_action' : reverse_lazy('home:display_table'),
              'form_method' : 'get',
              'form' : InputForm({'state' : state}),
              'html_table' : table,
              'pic_source' : reverse_lazy("home:plot", kwargs = {'c' : state})
              }

    return render(request, 'view_table.html', params)
from django.views.generic import FormView
class FormClass(FormView):

    template_name = 'forms.html'
    form_class = InputForm

    def get(self, request):

      state = request.GET.get('state', 'Jalisco')

      return render(request, self.template_name, {'form_action' : reverse_lazy('home:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})

    def post(self, request):

      state = request.POST.get('state', 'Jalisco')

      return render(request, self.template_name, {'form_action' : reverse_lazy('home:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})
# abc: Form to request the the info by state
def form(request):

    state = request.GET.get('state', 'Jalisco')
    g = Nominatim()

    location = str(g.geocode(STATES_DICT[state])._point[:2])

    params = {'form_action' : reverse_lazy('home:display_table'), #correct path
              'form_method' : 'get',
              'form' : InputForm({'state' : state}), # now, we only have InputForm
              'state' : STATES_DICT[state],
              'location' : location}

    return render(request, 'forms.html', params) #forms.html is the name of the template


from django.views.generic import FormView
class FormClass(FormView):

    template_name = 'forms.html'
    form_class = InputForm

    def get(self, request):

      state = request.GET.get('state', 'Jalisco')

      return render(request, self.template_name, {'form_action' : reverse_lazy('home:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})

    def post(self, request):

      state = request.POST.get('state', 'Jalisco')

      return render(request, self.template_name, {'form_action' : reverse_lazy('home:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'state' : state}),
                                                  'state' : STATES_DICT[state]})
#No sabia si querias que tambien agregara esto

def pic(request, c = None):

   t = np.linspace(0, 2 * np.pi, 30)
   u = np.sin(t)

   plt.figure() # needed, to avoid adding curves in plot
   plt.plot(t, u, color = c)

   # write bytes instead of file.
   figfile = BytesIO()

   # this is where the color is used.
   try: plt.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")

# Esto que nos da?
from .forms import StatesForm
def display_pic(request, c = 'r'):

    state = request.GET.get('state', 'Aguascalientes')

    params = {'title' : state,
              'form_action' : reverse_lazy('home:display_table'),
              'form_method' : 'get',
              'form' : InputForm({'state' : state}),
              'pic_source' : reverse_lazy("home:plot", kwargs = {'c' : state})}

    return render(request, 'view_table.html', params)


# Plot of crime vs projects granted by state
def plot(request, c = "Aguascalientes"):

   filename = join(settings.STATIC_ROOT, 'master.csv')

   df = pd.read_csv(filename, index_col = "id", parse_dates = ["id"])

   df = df[df["NOM_ENT"] == c]
   if not df.size: return HttpResponse("No such state!")

   ax =  ax = df.plot(kind='scatter', x='3x1 Projects Granted in 2013', y='Homicide Rate in 2013')
   ax.set_ylabel("Homice Rate in 2013")

   # write bytes instead of file.
   figfile = BytesIO()

   # this is where the color is used.
   plt.subplots_adjust(bottom = 0.16)
   try: ax.figure.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")

# Tampoco supe si queriamos lo que sigue
def resp_redirect(request):

    state = request.POST.get('state', '')
    if not state: state = request.GET.get('state', '')

    if state: return HttpResponseRedirect(reverse_lazy('home:resp', kwargs = {'state' : state}))

    return HttpResponseRedirect(reverse_lazy('home:form'))


def resp(request, state):

    return HttpResponse("I hear you, {}.".format(STATES_DICT[state]))


def static_site(request):

  return render(request, "static_site.html")
