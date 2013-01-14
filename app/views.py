from app.models 	import *
from app.forms 		import ContactoForm
from django.contrib.auth.models		import User 
from django.http 	import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template 	import RequestContext
from django.core.mail 	import send_mail

def contacto(request):
	if request.method == 'POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo	= 'Mensaje enviado desde Hankook Luis Albarenga'
			contenido = formulario.cleaned_data['mensaje'] + '\n'
			contenido += 'Comunicarse a : ' + formulario.cleaned_data['correo']
			send_mail(titulo, contenido, 'albarenga72@gmail.com', ['softwarelaycho@gmail.com'])

			return HttpResponseRedirect('/contacto')

	else:
		formulario = ContactoForm()
	return render_to_response('contacto/contacto.html', {'formulario': formulario }, context_instance=RequestContext(request))

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def productos(request):
	medidas = Medidas.objects.all()
	neumaticos = Neumatico.objects.all()
	return render_to_response('productos.html', locals() , context_instance=RequestContext(request))
# def search_form(request):
#     return render_to_response('base.html', context_instance=RequestContext(request))


# def contactview(request):
# 	subject 	= request.POST.get('topic', '')
# 	message 	= request.POST.get('message', '')
# 	from_email 	= request.POST.get('email', '')

# 	if subject and message and from_email:
# 		return HttpResponseRedirect('/contact/thankyou/')

# 	else:
# 			# return render_to_response('contactos.html', {'form': ContactForm()})
	
# 		return render_to_response('contacto/contacto.html', {'form': ContactForm()},
# 			RequestContext(request))


# def thanyou(request):
# 	return render_to_response('/contacto/gracias.html')

# def search(request):
# 	if 'q' in request.GET and request.GET['q']:
# 		before = request.GET['q']
# 		q = int(before)
# 		neumaticos = Neumatico.objects.filter(medidas_tipo_exact = q )
# 		return render_to_response('search_results.html', { 'neumatios': neumatios, 'query':q}
# 	else:
# 		 return render_to_response('search_form.html', {'error': True})

# 	return HttpResponse(message)