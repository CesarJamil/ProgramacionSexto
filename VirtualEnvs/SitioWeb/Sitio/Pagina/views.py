from django.shortcuts import render

# Create your views here.

def mostrar_inicio(request):
	return render(request, 'Pagina/index.html', {})

def widgets(request):
	return render(request, 'Pagina/widgets.html', {})

def calendar(request):
	return render(request, 'Pagina/calendar.html', {})

def dashboardv2(request):
	return render (request, 'Pagina/dashboard2.html', {})

def topNav(request):
	return render (request, 'Pagina/topNav.html', {})

def boxed(request):
	return render (request, 'Pagina/boxed.html', {})

def fixed(request):
	return render (request, 'Pagina/fixed.html', {})

def collapsedSidebar(request):
	return render (request, 'Pagina/collapsedSidebar.html', {})

def chartjs(request):
	return render (request, 'Pagina/chartjs.html', {})