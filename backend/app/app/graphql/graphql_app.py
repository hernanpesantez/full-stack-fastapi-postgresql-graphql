import graphene
from fastapi import Depends, Request, FastAPI, APIRouter
from sqlalchemy.orm import Session
from starlette.graphql import GraphQLApp
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer
from .query import Query
from .mutation import MyMutations
from app.api import deps
from app.core.config import settings
from app.db.session import SessionLocal
from app import crud, models, schemas





router = APIRouter() 
graphql_app = FastAPI()
gql_app = GraphQLApp(
        schema=graphene.Schema(query=Query, mutation=MyMutations),

    )

@router.api_route("/graphql", methods=["GET", "POST"])
async def graphql(
    request: Request
    ):
    
    return await gql_app.handle_graphql(request=request)

graphql_app.include_router(router, dependencies=[Depends(deps.get_current_user), Depends(deps.get_db), Depends(deps.get_current_active_user)])

