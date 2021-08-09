import requests
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from testapp.forms import LoginForm
from testapp.models import User
from testapp.models import BPI
from django.core.exceptions import ValidationError



def login(request):
    try:
        if request.method == 'POST':
            data = request.POST.copy() # so we can manipulate data
            form = LoginForm(data)
            print(form.__dict__.keys())
            # if form.is_valid():
            #     user = User.objects.get(email=data['email'])
            #     user.is_authenticated = True
            return render(request, template_name='home.html', context={'user': None})
        else:
            form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})
    except ValidationError as ve:
        print(f'ValidationError: {ve}')
        return render(request, template_name='login.html', context={'form': form})
    # except Exception as e:
    #     print(f'Exception: {e}')
    #     return render(request, template_name='error.html', context={'error': "Unknown Error"})
    

def home(request):
    return render(request, template_name='home.html', context={'form': form})

def save_coindesk():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        for k,v in data['bpi'].items():
            bpi = BPI(code=v['code'], symbol=v['symbol'], rate=v['rate_float'], description=v['description'])
            bpi.save()
        print(f'Saved {len(data.keys())} items')
    else:
        print('Unreachable API')
    return None
