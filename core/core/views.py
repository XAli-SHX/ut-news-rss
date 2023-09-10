from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import parser
from .ut_news import UtNews


@api_view(('GET',))
def news_rss(request):
    return Response({
        'news': parser.parse_news(),
    })
