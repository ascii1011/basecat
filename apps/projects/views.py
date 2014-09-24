import json

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from django.core.context_processors import csrf

from .models import Project


def project_dashboard(request, pk):
    p = Project.objects.get(pk=pk)
    pages = [ 
        (1,'f0r.jpg','Front Cover Outside'), 
        (2,'f0v.jpg','Front Cover Inside'), 
        (3,'f1r.jpg','f1r'), 
        (4,'f1v.jpg','f1v'), 
        (5,'f2r.jpg','f2r'), 
        (6,'f2v.jpg','f2v'), 
    ]
    thumbs = [
        (1,'f0r_thumb.jpg'),
        (2,'f0v_thumb.jpg'),
        (3,'f1r_thumb.jpg'),
        (4,'f1v_thumb.jpg'),
        (5,'f2r_thumb.jpg'),
        (6,'f2v_thumb.jpg'),
    ]

    c = {
        'participants': p.participants,
        'pages': pages,
        'thumbs': thumbs,
    }
    #c.update(csrf(request))
    return render(request, 'projects/project_dashboard.html', c)
