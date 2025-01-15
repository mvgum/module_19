from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from task1.models import Buyer, Game

# Create your views here.
# users = ["Игорь", "Сергей", "Антон", "Марат", "Павел"]
users = Buyer.objects.all()
usernames = [i.name for i in users]
info = {}


def sign_up_by_html(request):
    context = info
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'Username: {username}')
        print(f'password: {password}')
        print(f'age: {age}')
        if username in users:
            context['error'] = 'Пользователь уже существует'
        elif str(password) != str(repeat_password):
            context['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            context['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        return render(request, 'registration_page.html', context)
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    context = info
    print(context)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(f'Username: {username}')
            print(f'password: {password}')
            print(f'age: {age}')
            if username in users:
                context['error'] = 'Пользователь уже существует'
            elif str(password) != str(repeat_password):
                context['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                context['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
        else:
            form = UserRegister()
        context['form'] = form
        return render(request, 'registration_page.html', context)
    return render(request, 'registration_page.html')


def ind(request):
    return render(request, 'index.html')


def shop(request):
    context = {'text': ["Отправиться в прошлое", "Отправиться в будущее", "Посетить параллельный мир"]}
    return render(request, 'shop.html', context)


def basket(request):
    return render(request, 'basket.html')
