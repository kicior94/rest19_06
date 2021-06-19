from datetime import datetime
from games.models import Game
from games.serializers import GameSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO

'''
Baza danych -> Obiekty -> Serializacja -> Render to JSON
'''

game1 = Game(name='7 Cudow Swiata', release_date=datetime.now(),
             game_category='strategic', played=True)
game2 = Game(name='Pociagi', release_date=datetime.now(),
             game_category='strategic', played=False)
game1.save()
game2.save()

game1_serializer = GameSerializer(game1)
game2_serializer = GameSerializer(game2)

renderer = JSONRenderer()
rendered_game1 = renderer.render(game1_serializer.data)
rendered_game2 = renderer.render(game2_serializer.data)

'''
Parse from JSON -> Deserializacja -> Obiekt -> Baza danych
'''
new_game_json_string = '{"name":"7 Cudow Swiata","release_date":"2021-06-19T08:46:46.170465Z","game_category":"strategic","played":true}'
new_game_json_bytes = bytes(new_game_json_string, encoding="UTF-8")
new_game_bytes_stream = BytesIO(new_game_json_bytes)
parser = JSONParser()
new_game_parsed = parser.parse(new_game_bytes_stream)
new_game_serializer = GameSerializer(data=new_game_parsed)
if new_game_serializer.is_valid():
    new_game = new_game_serializer.save()
    print(new_game)
