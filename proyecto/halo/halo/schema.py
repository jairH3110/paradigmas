import graphene

import razas.schema


class Query(razas.schema.Query, graphene.ObjectType):
    pass

class Mutation(razas.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
