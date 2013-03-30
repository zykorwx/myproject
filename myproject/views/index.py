from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from myproject.forms import MensajeForm
from datetime import datetime



def index(request):
    return render_to_response('web/index.html', context_instance=RequestContext(request))


def sse(request):

		loco = 'data: por %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		return HttpResponse(loco, status=200,content_type='text/event-stream')

def envia(request):
	if request.method=='POST':
		formulario = MensajeForm(request.POST)
		if formulario.is_valid():
				sse(request)
				return HttpResponseRedirect('#')
	else:
		formulario = MensajeForm()
	return render_to_response('web/envia.html', {'formulario': formulario}, context_instance=RequestContext(request))

