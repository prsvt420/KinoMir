from datetime import datetime
from typing import Dict, Any

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from KinoMir import settings


@shared_task
def send_feedback(data: Dict) -> None:
    """Отправляет обратную связь на почту"""

    text: Any | None = data.get('text')
    topic: Any | None = data.get('topic')
    email: Any | None = data.get('email')

    html_message: str = render_to_string('core/template_feedback.html', {
        'text': text,
        'topic': topic,
        'email': email,
        'date': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
    })

    send_mail(
        subject=f'Обратная связь на KinoMir - {topic} | {email}',
        html_message=html_message,
        message=text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
