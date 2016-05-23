from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from shop.models import *
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'balance', 'info', 'phone', 'skype', 'address')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url','author', 'category', 'bucket', 'title', 'text', 'type', 'isAccept', 'price', 'cur_price',
                    'discount', 'pic', 'sold')

class BucketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bucket
        fields = ('owner')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = Category
         fields = ('chield', 'tittle', 'pic')


class BetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = Bet
         fields = ('user', 'bet', 'result', 'product')

