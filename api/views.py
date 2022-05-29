import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from .use_case import comparator


@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def biggest_roman_number(request: Request) -> Response:
    try:
        body = request.data.dict()
        return Response(comparator.biggest_number(body.get("text")))
    except Exception as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
