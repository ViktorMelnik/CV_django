from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def works(request):
    data = {
        'title': 'CV',
        'valus': ['Hello', 'some', '1234'],
        'obj':{
            'car':'BMW',
            'age': 20,
            'hobby': 'IT'
        }
    }
    return render(request, 'main/works.html', data)

