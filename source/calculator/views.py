from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse

numbers = {
        "A": 555,
        "B": 0
    }
a = numbers.get("A")
b = numbers.get("B")

def index_view(request, *args, **kwargs):
    if request.method == 'GET':
        print(HttpResponse.status_code)
        return render(request, 'index.html')


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def add_view(request, *args, **kwargs):

    if is_number(a) or is_number(b):
        sum = a + b
        answer = {
            "answer": sum
        }
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)
    else:
        answer = {
            "error": "Not number"
        }
        HttpResponse.status_code = 400
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)


def subtract_view(request, *args, **kwargs):

    if is_number(a) or is_number(b):
        sum = a - b
        answer = {
            "answer": sum
        }
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)
    else:
        answer = {
            "error": "Not number"
        }
        HttpResponse.status_code = 400
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)


def multiply_view(request, *args, **kwargs):

    if is_number(a) or is_number(b):
        sum = a * b
        answer = {
            "answer": sum
        }
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)
    else:
        answer = {
            "error": "Not number"
        }
        HttpResponse.status_code = 400
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)


def divide_view(request, *args, **kwargs):
    
    if is_number(a) or is_number(b):
        if b != 0:
            sum = a / b
            answer = {
                "answer": sum
            }
            if request.body:
                answer['content'] = json.loads(request.body)
            return JsonResponse(answer)
        else:
            answer = {
            "error": "Division by zero!"
        }
        HttpResponse.status_code = 400
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)
    else:
        answer = {
            "error": "Not number"
        }
        HttpResponse.status_code = 400
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)
