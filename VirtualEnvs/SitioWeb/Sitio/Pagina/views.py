from django.shortcuts import render

# Create your views here.

def mostrar_inicio(request):
	return render(request, 'Pagina/index.html', {})

def widgets(request):
	return render(request, 'Pagina/widgets.html', {})

def calendar(request):
	return render(request, 'Pagina/calendar.html', {})

def dashboardv2(request):
	return render(request, 'Pagina/dashboard2.html', {})

def topNav(request):
	return render(request, 'Pagina/topNav.html', {})

def boxed(request):
	return render(request, 'Pagina/boxed.html', {})

def fixed(request):
	return render(request, 'Pagina/fixed.html', {})

def collapsedSidebar(request):
	return render(request, 'Pagina/collapsedSidebar.html', {})

def chartjs(request):
	return render(request, 'Pagina/chartjs.html', {})

def flot(request):
	return render(request, 'Pagina/flot.html', {})

def morris(request):
	return render(request, 'Pagina/morris.html', {})

def inline(request):
	return render(request, 'Pagina/inline.html', {})

def buttons(request):
	return render(request, 'Pagina/buttons.html', {})

def general(request):
	return render(request, 'Pagina/general.html', {})

def icons(request):
	return render(request, 'Pagina/icons.html', {})