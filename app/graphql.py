import strawberry
from strawberry.fastapi import GraphQLRouter
from app.resolvers.task_resolver import TaskQuery, TaskMutation
from app.context import get_context # type: ignore

# Merge queries
@strawberry.type
class Query(TaskQuery):
    pass

# Merge mutations
@strawberry.type
class Mutation(TaskMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema,context_getter=get_context, graphql_ide=True)

