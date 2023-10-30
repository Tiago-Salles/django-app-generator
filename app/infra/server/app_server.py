from fastapi import FastAPI, APIRouter
from app.infra.urls import URLS
from core.utils.http_method import HttpMethod

class AppServer:

    _app = FastAPI()
    _router = APIRouter()


    async def initialize_server(self):
        try:
            await self.initialize_routes()
        except Exception as e:
            raise e 
        
    async def initialize_routes(self):
        for url_classes in URLS:
            for url in url_classes:
                if url["method"] not in [HttpMethod]:
                    raise "HTTP METHOD NOT ALLOWED"

                match url["method"]:
                    case HttpMethod.GET:
                        @self._router.get(url["path"])
                        async def call(): return url["function"]

                    case HttpMethod.POST:
                        @self._router.post(url["path"])
                        async def call(): return url["function"]

                    case HttpMethod.PUT:
                        @self._router.put(url["path"])
                        async def call(): return url["function"]

                    case HttpMethod.PATCH:
                        @self._router.patch(url["path"])
                        async def call(): return url["function"]

                    case HttpMethod.DELETE:
                        @self._router.delete(url["path"])
                        async def call(): return url["function"]