from django.shortcuts import render
from django.http import JsonResponse
from  .documents import PostDocument

# Create your views here.
def search_post(request):
    return JsonResponse({"result":[]})