# Views только для GET (Query)

import graphene
from graphene_django import DjangoObjectType

from grapheneapi.modeltype import BrandModelType, ClothesModelType, CarModelType, PersonModelType
from main.models import Brand, Clothes, Car, Person


class Query(graphene.ObjectType):
    brand_model = graphene.List(BrandModelType)
    clothes_model = graphene.List(ClothesModelType)

    car_model = graphene.List(CarModelType)
    person_model = graphene.List(PersonModelType)

    def resolve_brand_model(self, info):
        brands = Brand.objects.all()
        return brands
    
    def resolve_car_model(self, info):
        car = Car.objects.all()
        return car
    
    def resolve_clothes_model(self, info):
        clothes = Clothes.objects.all()
        return clothes
    
    def resolve_person_model(self, info):
        person = Person.objects.all()
        return person