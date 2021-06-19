from django.shortcuts import render, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators import csrf_exempt
from .models import Game
from .serializers import GameSerializer

# Create your views here.


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def game_list(request):
    if request.method == 'GET':
        # Baza danych -> Obiekty -> Serializacja -> Render to JSON
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return JSONResponse(data=games_serializer.data)
    elif request.method == 'POST':
        # Parse from JSON -> Deserializacja -> Obiekty -> Baza danych
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JSONResponse(
                data=game_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return JSONResponse(
            data=game_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@csrf_exempt
def game_detail(request, id):
    try:
        game = Game.objects.get(pk=id)
    except Game.DoesNotExist:
        error_message = {'error': 'Resource not found'}
        return JSONResponse(
            data=error_message,
            status=status.HTTP_404_NOT_FOUND
            )
        #return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        pass
    elif request.method=='PUT':
        pass
    elif request.method=='DELETE':
        pass