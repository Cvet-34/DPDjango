
from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
import webbrowser


# Create your views here.
def menu(request):
    text = 'Природные товары для красоты издоровья!'
    list = ['надежная упаковка', 'высокое качество продукции', 'вся продукция сертифицирована']
    context = {
        'text': text,
        'list': list
        }
    return render(request, 'menu.html', context)


def infoobshee(request):
    return render(request, 'infoobshee.html')


def nametov(request):
    title = 'КАТОЛОГ ТОВАРОВ'
    context = {
        'title': title,
    }
    return render(request, 'nametov.html', context)



def registration_page(request):

    users = {
        'Vasya': 'VasyokUrban',
        'Terminator2000': 'lolkekcheburek1894'
    }
    info = {
    }
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            #Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!, {webbrowser.open("http://127.0.0.1:8000/infoobshee/")} Перейдите по ссылке в магазин Брусника")
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'

    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})