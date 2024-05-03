import graphene
from graphene_django.views import GraphQLView

from django.contrib.auth.decorators import login_required
from django.urls import path

from grapheneapi.schema import Query


schema = graphene.Schema(query=Query)


class CustomGraphQLView(GraphQLView):
    # Переопределяем метод execute_graphql_request, 
    # чтобы добавить дополнительную логику перед 
    # выполнением запроса GraphQL. 
    def execute_graphql_request(
            self, request, data, 
            query, variables, operation_name, 
            show_graphiql=False):
        
        return super().execute_graphql_request(
            request, data, query, variables, operation_name, show_graphiql
        )


@login_required(login_url="/admin")
def graphql_view(request):
    view = CustomGraphQLView.as_view(graphiql=True, schema=schema)
    return view(request)


urlpatterns = [
    path("", graphql_view, name="graphql")
]
