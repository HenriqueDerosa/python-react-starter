from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('build/index.html')
    return HttpResponse(template.render({}, request))

def test(request):
    data = {
        'name': 'henriquederosa',
        'project': 'python-react-starter'
    }
    return JsonResponse(data)