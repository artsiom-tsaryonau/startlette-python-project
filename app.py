from starlette.applications import Starlette
from starlette.responses import UJSONResponse
from starlette.routing import Route


async def homepage(request):
    return UJSONResponse({'hello': 'world'})

app = Starlette(debug=True, routes=[
    Route('/', homepage)
])
