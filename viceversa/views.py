from django.shortcuts import render, HttpResponse, redirect
import json


def home(request):
    return render(request, 'home.html')


def sign_in(request):
    login = request.GET['log']
    password1 = request.GET['pass1']
    password2 = request.GET['pass2']

    if password2 == password1:
        # READ
        with open("viceversa/log_sign.json", "r") as my_file:
            signer_json = my_file.read()

        signer = json.loads(signer_json)

        # WRITE
        signer['REGISTER']['LOGIN_INFO']["user_" + login] = {login: password1}
        signer_json = json.dumps(signer)

        with open("viceversa/log_sign.json", "w") as my_file:
            my_file.write(signer_json)
        return render(request, 'sign_in.html')

    else:
        return HttpResponse("Щось пішло не так! Паролі не співпадають")


def index(request):
    login = request.GET['name']
    passname = request.GET['passname']
    with open("viceversa/log_sign.json", "r") as my_file:
        signer_json = my_file.read()

    signer = json.loads(signer_json)
    print(signer)
    print(type(signer))
    if "user_"+login in [key for key in signer['REGISTER']['LOGIN_INFO'].keys()] and signer['REGISTER']['LOGIN_INFO']["user_"+login] == {login:passname}:
        context = {
            "login": login,
        }

        return render(request, 'index.html', context=context)
    else:
        return HttpResponse("Щось пішло не так! Користувача не знайдено :(")
