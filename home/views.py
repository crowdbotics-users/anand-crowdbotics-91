from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-oscar', 'url': 'http://pypi.python.org/pypi/django-oscar/1.5.1'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'title': 'anand-crowdbotics-91',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
