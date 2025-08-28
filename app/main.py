from fastapi import FastAPI, Request
from app.database import Base, engine, SessionLocal
from app.graphql import graphql_app

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task GraphQL API")

app.include_router(graphql_app, prefix="/graphql")
