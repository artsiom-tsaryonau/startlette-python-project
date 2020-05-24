from starlette.applications import Starlette
from starlette.responses import UJSONResponse
from starlette.routing import Route


async def homepage(request):
    return UJSONResponse({'hello': 'world'})


async def homepage_path_paremeter(request):
    return UJSONResponse({'hello': request.path_params['user']})


async def homepage_headers(request):
    return UJSONResponse({'content-type': request.headers['content-type']})


async def homepage_get_parameters(request):
    return UJSONResponse({'query': request.query_params['query']})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/path/{user}', homepage_path_paremeter),
    Route('/headers', homepage_headers),
    Route('/params', homepage_get_parameters)
])
