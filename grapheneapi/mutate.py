import graphene
from graphene_django import DjangoObjectType

from main.models import Brand, Clothes
from grapheneapi.modeltype import BrandModelType, ClothesModelType


class CreateBrand(graphene.Mutation):
    class Arguments:
        # Аргументы которую далжен заполнить пользователь для создания бренда
        # required=True озночает что данное поле должно быть 
        # заполнено обязательно
        name = graphene.String(required=True)
        country = graphene.String(required=True)

    # Тут мы предолтавляем пользователю выбрать какие поля должны показываться
    # после создания 
    brand = graphene.Field(BrandModelType)

    # Тут мы делаем действие и функция mutate всегда с перва делжна принемать
    # такие параметры как self, info дальше уже в зависимосьти от аргументов
    def mutate(self, info, name, country):
        # Тут мы создаем бренд только говорил name=name и country=country 
        # в примере name='Qazaq Republic' а вот country='KZ'
        brand = Brand.objects.create(
            name=name, country=country
        )

        # Тут вы возвыращаем то что выпрал.
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