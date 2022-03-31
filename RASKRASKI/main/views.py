from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import picture
from .forms import pictureForm

def index(request):
    pictures = picture.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'pictures': pictures})


def about(request):
    return render(request, 'main/about.html')



def create(request):
    error = ''
    if request.method == 'POST':
        form = pictureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raskraski')

        else:
            error = 'Форма была неверной'
    form = pictureForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)



#{% block content%} <br><br><br>Текст</br></br></br>
#    {% for el in pictures %}
#        <div class="alert alert-warning mt-2">
#                <h3>{{el.title}}</h3>
#            {% if el.photo %}
#                <p><img class="img-article-left thumb" src="{{el.photo}}"></p>
#            {% endif %}
#        </div>
#    {% endfor %}
#{% endblock%}

#ятебялюблююююююююююююююююююююююююююююююююююююююююю