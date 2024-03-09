from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from .models import Thread, Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class TreadListView(TemplateView):
    template_name = 'message/thread_list.html'

@method_decorator(login_required, name='dispatch')
class ThreadDetailView(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetailView, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request, pk):
    json_response = {'created':False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("User is not authenticated")

    return JsonResponse(json_response)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))