# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from django.db.models import F
from books.models import Books, Borrow_log
import json
from django.contrib.auth import authenticate, login, logout



@csrf_exempt
def register(request):
    response_data = {}
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        firstname = body['firstname']
        lastname = body['lastname']
        password = body['password']
        email = body['email']

        user = User(username=username, first_name=firstname, last_name=lastname, email=email)
        user.set_password(password)
        user.save()

        response_data['success'] = True
        response_data['message'] = 'Registration done successfully'
        return JsonResponse(response_data)
    except Exception as e:
        response_data['success'] = False
        response_data['message'] = '%s (%s)' % (e.message, type(e))
        return JsonResponse(response_data)

@csrf_exempt
def login_view(request):
    response_data = {}
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            response_data['success'] = True
            response_data['message'] = "Welcome..!! you've have logged in succesfully"
            return JsonResponse(response_data)
        else:
            response_data['success'] = False
            response_data['message'] = 'Wrong credentials. Login failed.'
            return JsonResponse(response_data)
    except Exception as e:
        response_data['success'] = False
        response_data['message'] = '%s (%s)' % (e.message, type(e))
        return JsonResponse(response_data)


@csrf_exempt
def borrow_book(request):
    response_data = {}
    try:
        if request.user.is_authenticated():
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            book_id = body['book_id']

            # to do - avaialability of book by using count

            Books.objects.filter(id=book_id).update(count=F('count') - 1)
            User_data = User.objects.filter(username=request.user).values('id')[0]

            log = Borrow_log(book_id=book_id, borrow_id=User_data['id'])
            log.save()

            response_data['success'] = True
            response_data['message'] = "Book borrowed successfully..!"
            return JsonResponse(response_data)
        else:
            response_data['success'] = False
            response_data['message'] = "Not Authenticated...!"
            return JsonResponse(response_data)
    except Exception as e:
        response_data['success'] = False
        response_data['message'] = '%s (%s)' % (e.message, type(e))
        return JsonResponse(response_data)



@csrf_exempt
def borrow_list(request):
    response_data = {}
    try:
        if request.user.is_authenticated():

            User_data = User.objects.filter(username=request.user).values('id')[0]
            User_id = int(User_data['id'])
            borrow_data = Borrow_log.objects.filter(borrow_id=User_id).values_list('id', flat=True)

            #TO Do ==>> Join books table to get the user's borrowed books list

            response_data['success'] = True
            response_data['data'] = list(borrow_data)
            response_data['message'] = "Book borrowed successfully..!"
            return JsonResponse(response_data)
        else:
            response_data['success'] = False
            response_data['message'] = "Not Authenticated...!"
            return JsonResponse(response_data)
    except Exception as e:
        response_data['success'] = False
        response_data['message'] = '%s (%s)' % (e.message, type(e))
        return JsonResponse(response_data)