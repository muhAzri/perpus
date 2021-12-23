from django.http.response import HttpResponse
from django.shortcuts import render


def buku(request):
    list_title = ["Belajar Django", "Belajar Python", "Belajar Dart"]
    writer = "Muhammad Azri"

    konteks = {
        "title" : list_title,
        "writter" : writer
    }

    return render(request, 'buku.html', konteks)

def penerbit(request):
    return HttpResponse("Halaman Penerbit")