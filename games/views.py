from django.shortcuts import render, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Game
from .serializers import GameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        # Baza danych -> Obiekty -> Serializacja -> Render to JSON
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)
    elif request.method == 'POST':
        # Parse from JSON -> Deserializacja -> Obiekty -> Baza danych
        # game_data = JSONParser().parse(request)
        # game_serializer = GameSerializer(data=game_data)
        game_serializer = GameSerializer(data=request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(
                game_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            game_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@csrf_exempt
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def game_detail(request, id):
    try:
        game = Game.objects.get(pk=id)
    except Game.DoesNotExist:
        error_message = {'error': 'Resource not found'}
        return Response(
            error_message,
            status=status.HTTP_404_NOT_FOUND
        )
        # return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data)
    elif request.method == 'PUT':
        # game_data = JSONParser().parse(request)
        # game_serializer = GameSerializer(game, data=game_data)
        game_serializer = GameSerializer(data=request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data)
        return Response(
            game_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
