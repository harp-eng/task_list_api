from fastapi import FastAPI
from app.database import Base, engine
from app.graphql import graphql_app

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tasks GraphQL API")

app.include_router(graphql_app, prefix="/graphql")
