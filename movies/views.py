from django.shortcuts import render
import requests

# Create your views here.
def movie_list(request):
    url = 'http://www.omdbapi.com/?apikey=8dba5209&s=avengers'
    response = requests.get(url).json()
    context = {
        'response' : response
    }
    return render(request,'movies.html',context)
