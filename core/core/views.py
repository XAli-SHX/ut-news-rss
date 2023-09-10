from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from . import parser


@api_view(('GET',))
@renderer_classes([JSONRenderer])
def news_rss(request):
    return Response({
        'news': parser.parse_news(),
    })
