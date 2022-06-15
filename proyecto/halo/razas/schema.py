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
    armas = graphene.String()
    planeta = graphene.String()
    papel = graphene.String()
    rango = graphene.String()
    habilidad = graphene.String()
    tamano = graphene.String()
    #2
    class Arguments:
        nombre = graphene.String()
        description = graphene.String()
        armas = graphene.String()
        planeta = graphene.String()
        papel = graphene.String()
        rango = graphene.String()
        habilidad = graphene.String()
        tamano = graphene.String()    

    #3
    def mutate(self, info, nombre, description, armas, planeta, papel, rango, habilidad, tamano):
        raza = Raza(nombre=nombre, description=description, armas=armas, planeta=planeta,papel=papel, rango=rango, habilidad=habilidad,tamano=tamano)
        raza.save()

        return CreateRaza(
            id=raza.id,
            nombre=raza.nombre,
            description=raza.description,
            armas=raza.armas,
            planeta=raza.planeta,
            papel=raza.papel,
            rango=raza.rango,
            habilidad=raza.habilidad,
            tamano=raza.tamano,
        )


#4
class Mutation(graphene.ObjectType):
    create_raza = CreateRaza.Field()
