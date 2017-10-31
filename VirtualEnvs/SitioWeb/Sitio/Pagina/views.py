from django.shortcuts import render

# Create your views here.

def mostrar_inicio(request):
	return render(request, 'Pagina/index.html', {})

def widgets(request):
	return render(request, 'Pagina/widgets.html', {})

def calendar(request):
	return render(request, 'Pagina/calendar.html')