from django.shortcuts import render, redirect, HttpResponse
import nltk
from nltk.tokenize import word_tokenize


# Create your views here.
def index(request):
    return render(request, "natural_language/index.html")

def process(request):
    # print request.POST['sentence']
    # print(len(request.POST['sentence']))
    if len(request.POST['sentence']) < 1:
        print "*" * 50
        return redirect('/')

    else:
        sentence = request.POST['sentence']
        print "this is the sentence area ", sentence
        print "*" * 50
        request.session["sentence"] = nltk.word_tokenize(sentence)
        print "*" * 50
        return render(request, "natural_language/success.html")

def success(request):
    return render(request, "natural_language/success.html")
