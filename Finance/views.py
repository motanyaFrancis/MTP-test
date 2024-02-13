from django.shortcuts import render

# Create your views here.

def imprests_view(request):
    return render(request, 'imprests.html')


def imprest_detail_view(request):
    return render(request, 'imprest-details.html')