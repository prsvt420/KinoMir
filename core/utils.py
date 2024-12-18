from django.http import HttpRequest


def request_is_ajax(request: HttpRequest) -> bool:
    """Возвращает True, если запрос был AJAX"""

    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
