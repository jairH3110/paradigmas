import graphene
from graphene_django import DjangoObjectType

from .models import Raza


class RazaType(DjangoObjectType):
    class Meta:
        model = Raza


class Query(graphene.ObjectType):
    razas = graphene.List(RazaType)

    def resolve_razas(self, info, **kwargs):
        return Raza.objects.all()
#1
class CreateRaza(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    description = graphene.String()

    #2
    class Arguments:
        nombre = graphene.String()
        description = graphene.String()

    #3
    def mutate(self, info, nombre, description):
        raza = Raza(nombre=nombre, description=description)
        raza.save()

        return CreateRaza(
            id=raza.id,
            nombre=raza.nombre,
            description=raza.description,
        )


#4
class Mutation(graphene.ObjectType):
    create_raza = CreateRaza.Field()
