
from re import I
import graphene
from app import crud, models, schemas
from sqlalchemy.orm import Session



from app.db.session import SessionLocal


import graphene

class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(root, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()

class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()


# We must define a query for our schema
class Query(graphene.ObjectType):
    person = graphene.Field(Person)

# class CreateNewItem(graphene.Mutation):
#     class Argumetns:
        
#         title = graphene.String()
#         description = graphene.String()



#     ok = graphene.Boolean()

#     @staticmethod
#     def mutate(root, info, title, description):
#         print('hello')
#         item = schemas.ItemCreate(title=title, description=description)
#         db_item = models.Item(title=item.title, description=item.description)

#         print('ok ')
#         # db = SessionLocal()
#         # db.add(db_item)
#         # db.commit()
#         # db.refresh(db_item)
#         ok = True
#         return CreateNewItem(ok=ok)


# class ItemMutation(graphene.ObjectType):
#     create_new_item = CreateNewItem.Field()