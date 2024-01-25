from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# dynamic url function
def profile_page_view(request, username):
    text = f'welcome {username}'
    return HttpResponse(text)

# TO RENDER THE HTML PAGE:
def home_page_view(request):
    # passing python code to HTML
    name = 'django developer'
    return render(request, 'index.html', {'name':name})

# def home_page_view(request):
#     text = 'welcome to my django website'
#     return HttpResponse(text)


# HOW TO RETURN A TEMPLATE BACK AS A RESPONSE
# 1. define the location where the template will be obtained from
# if you want it to be in the app, create a folder called templates 

# about page url
def about_page_view(request):
    school = 'univelcity'
    return render(request, 'about.html', {'school':school})

# def about_page_view(request): 
#     text = f'about us'
#     return HttpResponse(text)

# static url function
def profile_page_view(request):
    text = f'welcome user'
    return HttpResponse(text)