# Views только для GET (Query)

import graphene
from graphene_django import DjangoObjectType

from grapheneapi.modeltype import BrandModelType, ClothesModelType
from main.models import Brand, Clothes


class Query(graphene.ObjectType):
    brand_model = graphene.List(BrandModelType)
    clothes_model = graphene.List(ClothesModelType)

    def resolve_brand_model(self, info):
        brands = Brand.objects.all()
        return brands
    
    def resolve_clothes_model(self, info):
        clothes = Clothes.objects.all()
        return clothes
    
    