# SERIALIZERS !!!

import graphene
from graphene_django import DjangoObjectType

from main.models import Brand, Clothes, Car, Person


class CarModelType(DjangoObjectType):
    class Meta:
        model = Car


class PersonModelType(DjangoObjectType):
    class Meta:
        model = Person
        

class BrandModelType(DjangoObjectType):
    class Meta:
        model = Brand


class ClothesModelType(DjangoObjectType):
    class Meta:
        model = Clothes