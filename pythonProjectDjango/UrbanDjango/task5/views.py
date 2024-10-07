from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#     else:
#         form = UserRegister()
#     return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    users = ['Tom', 'John', 'Ilia']
    info = {}
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            errors.append('Пароли не совпадают')
        elif age < 18:
            errors.append('Вы должны быть старше 18')
        elif username in users:
            errors.append('Пользователь уже существует')
    info['error'] = errors
    return render(request, 'registration_page.html', context=info)


def sign_up_by_django(request):
    users = ['Tom', 'John', 'Ilia']
    info = {}
    errors = []
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if password == repeat_password and age >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                errors.append('Пароли не совпадают')
            elif age < 18:
                errors.append('Вы должны быть старше 18')
            elif username in users:
                errors.append('Пользователь уже существует')
    else:
        form = UserRegister()
    info['error'] = errors
    return render(request, 'registration_page.html', {'form': form, 'info': info})
