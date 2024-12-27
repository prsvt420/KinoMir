from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from core.forms import FeedbackForm


class FeedbackView(FormView):
    """Представление обратной связи"""

    template_name: str = 'core/feedback.html'
    form_class: type = FeedbackForm
    success_url: str = reverse_lazy('movies:movies-list')


def redirect_to_movies_list(request: HttpRequest) -> HttpResponseRedirect:
    """Редирект на список фильмов"""
    return redirect('movies:movies-list')
