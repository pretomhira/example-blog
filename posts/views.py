from django.shortcuts import render
import requests
from django.urls import reverse



# POSTS VIEW ENDPOINT
def posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()

    
    return render(request, 'blog-listing.html', {
        'post_data': data,
       
    })


# POST DETAILS VIEW ENDPOINT
def post_details(request,post_id):
    response1 = requests.get('https://jsonplaceholder.typicode.com/posts/'+str(post_id))
    data1= response1.json()

    response2 = requests.get('https://jsonplaceholder.typicode.com/posts/'+str(post_id)+'/comments')
    data2= response2.json()

    return render(request, 'blog-post.html',{
        'post_data1': data1,
        'post_data2': data2,
    })