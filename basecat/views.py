import json

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from django.core.context_processors import csrf

from profiles.models import UserProfile

def home(request):
    c = {}
    c.update(csrf(request))
    try:
        p = UserProfile.objects.get(user=request.user)
        c.update({'projects': [(x.id, x.name) for x in p.my_project_list]})
    except Exception as e:
        print e

    return render(request, 'index.html', c)
