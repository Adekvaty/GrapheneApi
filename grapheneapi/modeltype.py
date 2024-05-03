#SERIALIZERS

import graphene
from graphene_django import DjangoObjectType

from main.models import Brand, Clothes

class BrandModelType(DjangoObjectType):
    class Meta:
        model = Brand


class ClothesModelType(DjangoObjectType):
    class Meta:
        model = Clothes