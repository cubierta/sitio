# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.db import models

#Choices for a 'tipo'
TIPOS 			= (
   				('au', 'Automovil'),
   				('ca', 'Camioneta'),
   				('vh', 'Camiones'),
	)

class Categoria(models.Model):
	
	tipo 		= models.CharField(max_length=10, choices=TIPOS)
	def __unicode__(self):
		return self.tipo


#Choices foa a 'modelo'
CLASES 			= (
				('vt','VENTUS'),
				('dp','DYNAPRO'),
				('op','OPTIMO'),
				('ra08','RA08'),
				('tbr','TBR'),

	)
class Disenho(models.Model):
	modelo 		= models.CharField(max_length=10, choices=CLASES)
	def __unicode__(self):
		return self.modelo


class Medidas(models.Model):
	altura 		= models.IntegerField()
	aro 		= models.DecimalField(max_digits=5, decimal_places=2)
	ancho 		= models.IntegerField()
	def __unicode__(self):
		return str(self.ancho) 


class Neumatico(models.Model):
	nombre 		= models.CharField(max_length=200)
	categoria 	= models.ForeignKey(Categoria)
	disenho		= models.ForeignKey(Disenho)
	medidas		= models.ForeignKey(Medidas)
	image 		= models.ImageField(upload_to='pictures')
	def __unicode__(self):
		return self.nombre



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=200)


class Personal(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=400)
	tel_numb = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	twitter = models.CharField(max_length=30)



