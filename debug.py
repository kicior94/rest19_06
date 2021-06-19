from datetime import datetime
from games.models import Game
from games.serializers import GameSerializer
from rest_framework.renderers import JSONRenderer

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