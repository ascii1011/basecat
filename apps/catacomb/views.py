import json

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from django.core.context_processors import csrf

from api import Comm

def main(request):
    print request.user.username
    c = {}
    c.update(csrf(request))
    return render(request, 'base.html', c)


class BrainView(TemplateView):
    template_name="base.html"

    def post(self, request):
        c = Comm( request )
        return HttpResponse(json.dumps( c.generate() ), content_type="application/json")
