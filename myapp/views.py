from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# in django render is the shortcut function used to combine a templet with the data and return an HTTP response

#create your view/logic here

# def index(request):
#     return render(request, 'index.html')

# def counter(request):
#     text = request.GET['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount': amount_of_words})

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Experience'
    feature1.details = '3+ years.'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Degree'
    feature2.details = 'Master of science in computer Science Engineering'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Based In'
    feature3.details = 'Thunder Bay, Ontario, Canada.'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Email'
    feature4.details = 'ssah@lakeheadu.ca'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Phone'
    feature5.details = '+18073583778'

    feature6 = Feature()
    feature6.id = 5
    feature6.name = 'Availability'
    feature6.details = 'Open to work'

    features = [feature1, feature2, feature3, feature4, feature5, feature6]
    return render(request, 'index.html', {'features': features})

# def index(request):
#     features = Feature.objects.all()
#     return render(request, 'index.html', {'features': features})
    

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})