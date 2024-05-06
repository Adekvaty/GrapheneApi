import graphene
from graphene_django import DjangoObjectType

from main.models import Brand, Clothes, Person, Car


class BrandModelType(DjangoObjectType):
    class Meta:
        model = Brand


class ClothesModelType(DjangoObjectType):
    class Meta:
        model = Clothes

class PersonModelType(DjangoObjectType):
    class Meta:
        model = Person

class CarModelType(DjangoObjectType):
    class Meta:
        model = Car
