import graphene
from graphene_django import DjangoObjectType

from main.models import Brand, Clothes
from grapheneapi.modeltype import BrandModelType, ClothesModelType


class CreateBrand(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        country = graphene.String(required=True)

    brand = graphene.Field(BrandModelType)

    def mutate(self, info, name, country):
        brand = Brand.objects.create(
            name=name, country=country
        )
        return CreateBrand(brand=brand)


