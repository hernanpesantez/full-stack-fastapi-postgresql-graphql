import graphene
from typing import Any, List

from fastapi import Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

class Query(graphene.ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    goodbye = graphene.String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'



    # def resolve_hello(self, info,
    #     items,
    #     db: Session = Depends(deps.get_db),
    #     skip: int = 0,
    #     limit: int = 100,
    #     # current_user: models.User = Depends(deps.get_current_active_user),
    #     ) -> Any:
    #     """
    #     Retrieve items.
    #     """
    #     # if crud.user.is_superuser(current_user):
    #     items = crud.item.get_multi(db, skip=skip, limit=limit)
    #     # else:
    #     #     items = crud.item.get_multi_by_owner(
    #     #         db=db, owner_id=current_user.id, skip=skip, limit=limit
    #     #     )
    #     return items