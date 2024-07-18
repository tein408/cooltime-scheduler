from django.shortcuts import render
from django.http import HttpResponse

def upload_photo(request):
    # TODO(kimnamgue): Save a photo to the remote storage.
    return HttpResponse("Uploaded!")
