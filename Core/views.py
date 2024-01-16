from django.shortcuts import render
from random import randint
# def sum(a, b):
#     return a + b


def example(request):
    return render(request, 'Core/example.html')


def example2(request):
    return render(request, 'Core/index.html')

    
def magic_number(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        random_number = randint(1, 2)
        if number == random_number:
            return render(request, 'Core/magic_number.html', {'result': '1' })
        else: 
            return render(request, 'Core/magic_number.html', {'result': '0' })

    return render(request, 'Core/magic_number.html')

