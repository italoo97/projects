# from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# from django.views import View
from django.utils.decorators import method_decorator
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

# Objetos Definidos com as classes proprias para cada uma das suas respectivas funções

class CarListView(ListView):
	model = Car
	template_name = 'cars.html'
	context_object_name = 'cars'

	def get_queryset(self):
		cars = super().get_queryset().order_by('model')
		search = self.request.GET.get('search')
		if search:
			cars = cars.filter(model__icontains=search)
		return cars

@method_decorator(login_required, name='dispatch')
class NewCarsCreateView(CreateView):
	model = Car
	form_class = CarModelForm
	template_name = "new_car.html"
	success_url = '/cars/'

class CarDetailView(DetailView):
	model = Car
	template_name = 'car_detail.html'

@method_decorator(login_required, name='dispatch')
class CarUpdateView(UpdateView):
	model = Car
	form_class = CarModelForm
	template_name = 'car_update.html'
	success_url = '/cars/'

	def get_success_url(self):
		return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class CarDeleteView(DeleteView):
	model = Car
	template_name = 'car_delete.html'
	success_url = '/cars/'

#==============================================================================================#

#Objetos definidos como funções, mais manual e trabalhoso

# def cars_view(request):
# 	cars = Car.objects.all().order_by('model')
# 	search = request.GET.get('search')
	
# 	if search:
# 		cars = Car.objects.filter(model__icontains=search) #(brand__name='Fiat') #aqui se usa 2 _ para indicar que voce quer pesquisar pelo nome e não pelo ID do item 
# 										# o icontains ele ignora letras maiusculas e minusculas trazendo todos os dados 

# 	return render(
# 				request, 
# 				'cars.html',
# 				{'cars': cars} #Aqui é um dicionario para simbolizar o banco de dados
# 				)

# @login_required
# def new_cars_view(request):
# 	if request.method =='POST':
# 		new_car_form = CarModelForm(request.POST, request.FILES)
# 		if new_car_form.is_valid():
# 			new_car_form.save()
# 			return redirect('cars_list')
# 	else:
# 		new_car_form = CarModelForm()
# 	return render(request, 'new_car.html', {'new_car_form': new_car_form})

#==============================================================================================#

# Objetos definidos penas com a classe base de View

# class CarsView(View):
# 	def get(self, request):
# 		cars = Car.objects.all().order_by('model')
# 		search = request.GET.get('search')
		
# 		if search:
# 			cars = Car.objects.filter(model__icontains=search) #(brand__name='Fiat') #aqui se usa 2 _ para indicar que voce quer pesquisar pelo nome e não pelo ID do item 
# 											# o icontains ele ignora letras maiusculas e minusculas trazendo todos os dados 

# 		return render(
# 					request, 
# 					'cars.html',
# 					{'cars': cars} #Aqui é um dicionario para simbolizar o banco de dados
# 					)

# @method_decorator(login_required, name='dispatch')
# class NewCarsView(View):
# 	def get(self, request):
# 		new_car_form = CarModelForm()
# 		return render(request, 'new_car.html', {'new_car_form': new_car_form})
	
# 	def post(self, request):
# 		new_car_form = CarModelForm(request.POST, request.FILES)
# 		if new_car_form.is_valid():
# 			new_car_form.save()
# 			return redirect('cars_list')
# 		return render(request, 'new_car.html', {'new_car_form': new_car_form})