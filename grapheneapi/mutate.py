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


class UpdateBrand(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        country = graphene.String()

    brand = graphene.Field(BrandModelType)

    def mutate(self, info, id, name=None, country=None):
        brand = Brand.objects.get(id=id)

        if name:
            brand.name = name

        elif country:
            brand.country = country

        brand.save()
        return UpdateBrand(brand=brand)
    

class DeleteBrand(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        confirmation = graphene.Boolean(required=True)
    
    brand = graphene.Field(BrandModelType)
    success = graphene.Boolean()

    def mutate(self, info, id, confirmation):
        brand = Brand.objects.get(id=id)

        if confirmation:
            brand.delete()
            return DeleteBrand(success=True)
        
        return DeleteBrand(brand=brand, success=False)


class Mutation(graphene.ObjectType):
    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()
    delete_brand = DeleteBrand.Field()