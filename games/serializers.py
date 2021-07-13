from rest_framework import serializers
from .models import Game, GameCategory, Player, PlayerScore
import games.views


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name = 'game-detail'
    )

    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games'
        )

class GameSerializer(serializers.ModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = ('url', 'name', 'release_date', 'game_category', 'played')

# class GameSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     release_date = serializers.DateTimeField()
#     game_category = serializers.CharField(max_length=200)
#     played = serializers.BooleanField(required=False)

#     def create(self, validated_data):
#         return Game.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name )
#         instance.release_date = validated_data.get('release_date', instance.release_date)
#         instance.game_category = validated_data.get('game_category', instance.game_category)
#         instance.played = validated_data.get('played', instance.played)
#         instance.save()
#         return instance