from django.shortcuts import render


def index(request):
    data = {"school": "Алабуге политех", "groop": "215-8-1", "speciality": "Web-developer", "futureSpeciality": "Дворник"}
    return render(request, "main/index.html", context=data)


def about(request):
    data = {"fullName": "Муратов Арсений Дмитриевич", "growth": "186см", "weight": "65кг", "age": "16 лет"}
    return render(request, "main/about.html", context=data)


def contacts(request):
    data = {"phone": "Мой номер телефона: +7-919-005-81-58", "telegram": "Мой телеграм: @AviaryS", "vk": "Мой вк: @comeback_d"}
    return render(request, "main/contacts.html", context={"data": data})


def form(request):
    return render(request, "main/form.html")