from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

STATES = (
    ['Aguascalientes', 'Aguascalientes'],
    ['Baja California', 'Baja California'],
    ['Baja California Sur', 'Baja California Sur'],
    ['Campeche', 'Campeche'],
    ['Coahuila de Zaragoza', 'Coahuila de Zaragoza'],
    ['Colima', 'Colima'],
    ['Chiapas', 'Chiapas'],
    ['Chihuahua', 'Chihuahua'],
    ['Ciudad de Mexico', 'Ciudad de Mexico'],
    ['Durango', 'Durango'],
    ['Guanajuato', 'Guanajuato'],
    ['Guerrero', 'Guerrero'],
    ['Hidalgo', 'Hidalgo'],
    ['Jalisco', 'Jalisco'],
    ['Mexico', 'Mexico'],
    ['Michoacan de Ocampo', 'Michoacan de Ocampo'],
    ['Morelos', 'Morelos'],
    ['Nayarit', 'Nayarit'],
    ['Nuevo Leon', 'Nuevo Leon'],
    ['Oaxaca', 'Oaxaca'],
    ['Puebla', 'Puebla'],
    ['Queretaro', 'Queretaro'],
    ['Quintana Roo', 'Quintana Roo'],
    ['San Luis Potosi', 'San Luis Potosi'],
    ['Sinaloa', 'Sinaloa'],
    ['Sonora', 'Sonora'],
    ['Tabasco', 'Tabasco'],
    ['Tamaulipas', 'Tamaulipas'],
    ['Tlaxcala', 'Tlaxcala'],
    ['Veracruz de Ignacio de la Llave', 'Veracruz de Ignacio de la Llave'],
    ['Yucatan', 'Yucatan'],
    ['Zacatecas', 'Zacatecas']
   )

STATES_DICT = dict(STATES)

class Input(models.Model):

    state = models.CharField(choices=STATES, max_length=32)

#COUNTIES = ()


class States(models.Model):

    state = models.CharField(choices=STATES, max_length=32)
