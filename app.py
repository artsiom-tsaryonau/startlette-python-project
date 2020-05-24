from starlette.applications import Starlette
from starlette.responses import UJSONResponse
from starlette.routing import Route


async def homepage(request):
    return UJSONResponse({'hello': 'world'})


async def homepage_paremeter(request):
    return UJSONResponse({'hello': request.path_params['user']})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/{user}', homepage_paremeter)
])
