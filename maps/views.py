from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy


from os.path import join
from django.conf import settings

import numpy as np, pandas as pd
import matplotlib.pyplot as plt


#from .forms import InputForm
#from .models import STATES_DICT, CURRENCY_DICT

import geopandas as gpd, folium
from geopy import Nominatim

import seaborn as sns
sns.set(font_scale = 1.7)

from io import BytesIO
# Create your views here.
def index(request):
    params = {'title' : "A map of Mexico",
              'form_action' : reverse_lazy('maps:embedded_map'),
              }
    return render(request, 'view_map.html', params)


def embedded_map(request):

  filename = join(settings.STATIC_ROOT, 'maps/MEX_adm0.shp')

  m = folium.Map([22.0399745, -102.9152044], tiles='stamentoner', zoom_start = 4)

  df = gpd.read_file(filename)

  peninsula = [
  "Campeche",
  "Yucatan",
  "Tabasco",
  "Quintana Roo",]

  sur =[
  "Chiapas",
  "Guerrero",
  "Oaxaca",
  "Veracruz",
  ]

  centro = [
  "Ciudad de Mexico",
  "Hidalgo",
  "Mexico",
  "Morelos",
  "Puebla",
  "Tlaxcala",
  ]

  occidente = [
  "Colima",
  "Jalisco",
  "Michoacan",
  "Nayarit",
  "Sinaloa"
   ]

  bajio = [
  "Aguascalientes",
  "Zacatecas",
  "Guanajuato",
  "Queretaro",
   ]

  norte = [
  "Baja California",
  "Baja California Sur",
  "Chihuahua",
  "Durango",
  "Sonora",
  ]

  noreste = [
  "Coahuila",
  "Nuevo Leon",
  "San Luis Potosi",
  "Tamaulipas",
  ]
  sample= ["Mexico"]

  mtn_df = gpd.tools.geocode(sample, provider = "googlev3").to_crs(df.crs)
  #mtn_df2 = gpd.tools.geocode(norte, provider = "googlev3").to_crs(df.crs)
  #mtn_df3 = gpd.tools.geocode(centro, provider = "googlev3").to_crs(df.crs)
 # mtn_df4 = gpd.tools.geocode(bajio, provider = "googlev3").to_crs(df.crs)
  #mtn_df5 = gpd.tools.geocode(sur, provider = "googlev3").to_crs(df.crs)
  #mtn_df6 = gpd.tools.geocode(peninsula, provider = "googlev3").to_crs(df.crs)
  #mtn_df7 = gpd.tools.geocode(occidente, provider = "googlev3").to_crs(df.crs)

  folium.GeoJson(gpd.sjoin(df, mtn_df, how = "inner", op = "contains"),
                 style_function=lambda feature: {
                  'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
                 }).add_to(m)

  #folium.GeoJson(gpd.sjoin(df, mtn_df2, how = "inner", op = "contains"),
    #           style_function=lambda feature: {
    #            'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
    #           }).add_to(m)
 # folium.GeoJson(gpd.sjoin(df, mtn_df3, how = "inner", op = "contains"),
#                 style_function=lambda feature: {
#                  'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
#                 }).add_to(m)

  #folium.GeoJson(gpd.sjoin(df, mtn_df4, how = "inner", op = "contains"),
    #           style_function=lambda feature: {
    #            'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
    #           }).add_to(m)
  #folium.GeoJson(gpd.sjoin(df, mtn_df5, how = "inner", op = "contains"),
    #             style_function=lambda feature: {
    #              'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
    #             }).add_to(m)

  #folium.GeoJson(gpd.sjoin(df, mtn_df6, how = "inner", op = "contains"),
    #           style_function=lambda feature: {
    #            'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
    #           }).add_to(m)

  #folium.GeoJson(gpd.sjoin(df, mtn_df7, how = "inner", op = "contains"),
    #           style_function=lambda feature: {
    #            'fillColor': 'red', 'fillOpacity' : 0.6, 'weight' : 2, 'color' : 'black'
    #           }).add_to(m)

 # Maybe, we do not need this
 #for xi, pt in mtn_df.iterrows():
      #folium.RegularPolygonMarker(pt.geometry.coords[::][0][::-1], popup=pt.address,
                          #number_of_sides = 5, radius = 8, fill_color = "black", fill_opacity = 1.0).add_to(m)

  map_string = m._repr_html_().replace("width:100%;", "width:60%;float:right;", 1)

  return render(request, 'view_map.html', {"title" : "Social Innovation and Crime in Mexico",
                                           "map_string" : map_string})
