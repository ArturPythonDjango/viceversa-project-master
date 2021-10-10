from django.shortcuts import render, HttpResponse,redirect
import json


def home(request):
    return render(request, 'home.html')


def reverse(request):
    login = request.GET['log']
    password1 = request.GET['pass1']
    password2 = request.GET['pass2']

    if password2 == password1:
        # READ
        with open("viceversa/capitals.json", "r") as my_file:
            capitals_json = my_file.read()

        capitals = json.loads(capitals_json)

        # WRITE
        capitals['REGISTER']['LOGIN_INFO'][login] = password1
        capitals_json = json.dumps(capitals)

        with open("viceversa/capitals.json", "w") as my_file:
            my_file.write(capitals_json)
        return render(request, 'reverse.html')

    else: return HttpResponse("Щось пішло не так! Паролі не співпадають")


def index(request):
    login = request.GET['name']
    passname= request.GET['passname']
    with open("viceversa/capitals.json", "r") as my_file:
        capitals_json = my_file.read()

    capitals = json.loads(capitals_json)
    print(capitals)
    print(type(capitals))
    if capitals['REGISTER']['LOGIN_INFO'][login] == passname:
        context = {
            "login":login,
        }

        return render(request, 'index.html',context=context)
    else: return HttpResponse("Щось пішло не так! Користувача не знайдено :(")



