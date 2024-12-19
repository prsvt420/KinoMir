from django.urls import reverse_lazy
from django.views.generic import FormView

from core.forms import FeedbackForm


class FeedbackView(FormView):
    """Представление обратной связи"""

    template_name: str = 'core/feedback.html'
    form_class: type = FeedbackForm
    success_url: str = reverse_lazy('movies:movies-list')
