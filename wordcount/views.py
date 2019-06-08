from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def result(request):
    text = request.GET['fulltext']
    word_dictionary = {}
    words = text.split()
    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    
    return render(request, 'result.html', {'full':text, 'length': len(words), 'dictionary': word_dictionary.items()})