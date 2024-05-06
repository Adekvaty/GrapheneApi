import graphene
from graphene_django import DjangoObjectType

from main.models import Brand, Clothes, Person, Car
from grapheneapi.modeltype import BrandModelType, ClothesModelType, PersonModelType, CarModelType


class CreateClothes(graphene.Mutation):
    class Arguments:
        brand = graphene.ID(required=True)
        type = graphene.String(required=True)
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        material = graphene.String(required=True)

    clothes = graphene.Field(ClothesModelType)

    def mutate(self, info, type, name, brand, price, material):
        brand = Brand.objects.get(id=brand)

        clothes = Clothes.objects.create(
            info=info, 
            type=type, 
            name=name, 
            brand=brand, 
            price=price, 
            material=material
        )
        clothes.save()
        return CreateClothes(clothes=clothes)
    

class UpdateClothes(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        type = graphene.String()
        name = graphene.String()
        brand_id = graphene.ID()
        price = graphene.Decimal()
        material = graphene.String()

    clothes = graphene.Field(ClothesModelType)

    def mutate(self, info, id, name=None, brand_id=None, type=None, price=None, material=None):
        clothes = Clothes.objects.get(id=id)

        if brand_id:
            Brand.objects.get(id=brand_id)

        if name:
            clothes.name = name

        elif type:
            clothes.type = type

        elif price:
            clothes.price = price

        elif material:
            clothes.material = material

        clothes.save()
        return UpdateClothes(clothes=clothes)
    

class DeleteClothes(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    clothes = graphene.Field(ClothesModelType)
    success = graphene.Boolean()

    def mutate(self, info, id):
        clothes = Clothes.objects.get(id=id)
        clothes.delete()
        return DeleteClothes(success=True)
    

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

    # Тут мы делаем действие и функция mutate всегда с перва должна принемать
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
    
class CreatePerson(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        has_licens = graphene.Boolean(required=True)
        icense_cate = graphene.String(required=True)

    person = graphene.Field(PersonModelType)

    def mutate(self, info, first_name, last_name, has_licens, icense_cate):
       
        person = Person.objects.create(
            first_name = first_name,
            last_name = last_name,
            has_licens = has_licens,
            icense_cate = icense_cate      
        )

        return CreatePerson(person=person)
    
class UpdatePerson(graphene.Mutation):
    class Arguments:      
        id = graphene.ID(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        has_license = graphene.Boolean()
        license_category = graphene.String()

    person = graphene.Field(PersonModelType)


    def mutate(self, info, id, first_name=None, last_name=None, has_licens=None, icense_cate=None):

        person = Person.objects.get(id=id)

        if first_name:
            person.first_name = first_name

        elif last_name:
            person.last_name = first_name

        elif has_licens:
            person.has_licens = has_licens

        elif icense_cate:
            person.icense_cate = icense_cate

        person.save()
        return UpdatePerson(person=person)
    
class DeletePerson(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    person = graphene.Field(PersonModelType)
    success = graphene.Boolean()

    def mutate(self, info, id):
        person = Person.objects.get(id=id)
        person.delete()
        return DeletePerson(success=True)
    
class CreateCar(graphene.Mutation):
    class Arguments:
        owner_id = graphene.Int(required=True)
        model = graphene.String(required=True)
        brand = graphene.String(required=True)
        year = graphene.Int(required=True)
        registration_number = graphene.String(required=True)

    car = graphene.Field(CarModelType)

    def mutate(root, info, owner_id, model, brand, year, registration_number):
        car = Car.objects.create(
            owner_id=owner_id,
            model=model,
            brand=brand,
            year=year,
            registration_number=registration_number,
        )
        return CreateCar(car=car)
    
class UpdateCar(graphene.Mutation):
    class Arguments:
        owner_id = graphene.ID(required=True)
        model = graphene.String()
        brand = graphene.String()
        year = graphene.Int()
        registration_number = graphene.String()

    car = graphene.Field(CarModelType)

    def mutate(self, info, id, owner_id=None, model=None, brand=None, year=None, registration_number=None):

        car = Car.objects.get(id=id)

        if owner_id:
            Person.objects.get(id=owner_id)


        elif model:
            car.model = model
        
        elif brand:
            car.brand = brand

        elif year:
            car.year = year
        
        elif registration_number:
            car.registration_number = registration_number

        car.save()
        return UpdateCar(car=car)

class DeleteCar(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    car = graphene.Field(CarModelType)
    success = graphene.Boolean()

    def mutate(self, info, id):
        car = Car.objects.get(id=id)
        car.delete()
        return DeleteCar(success=True)



class Mutation(graphene.ObjectType):
    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()
    delete_brand = DeleteBrand.Field()

    create_clothes = CreateClothes.Field()
    update_clothes = UpdateClothes.Field()
    delete_clothes = DeleteClothes.Field()

    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()

    create_car = CreateCar.Field()
    update_car = UpdateCar.Field()
    delete_car = DeleteCar.Field()

