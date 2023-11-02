from fastapi import FastAPI, APIRouter
from ..urls import URLS
from core.utils.http_method import HttpMethod

class AppServer:

    __app = FastAPI()
    __router = APIRouter()


    def initialize_server(self):
        try:
            self.__initialize_routes()
            return self.__app
        except Exception as e:
            raise e 
        
    def __initialize_routes(self):
        for url_classes in URLS:
            for url in url_classes:
                if url["method"] not in HttpMethod:
                    raise "HTTP METHOD NOT ALLOWED"

                match url["method"]:
                    case HttpMethod.GET:
                        @self.__router.get(
                            url["path"],
                            tags=url["tags"],
                        )
                        
                        async def call(): 
                            print(url["path"])
                            print(url["function"])
                            print(await url["function"]())
                            return await url["function"]()

                    case HttpMethod.POST:
                        @self.__router.post(
                            url["path"],
                            tags=url["tags"],
                        )
                        async def call(): return await url["function"]()

                    case HttpMethod.PUT:
                        @self.__router.put(
                            url["path"],
                            tags=url["tags"],
                        )
                        async def call(): return await url["function"]()

                    case HttpMethod.PATCH:
                        @self.__router.patch(
                            url["path"],
                            tags=url["tags"],
                        )
                        async def call(): return await url["function"]()

                    case HttpMethod.DELETE:
                        @self.__router.delete(
                            url["path"],
                            tags=url["tags"],
                        )
                        async def call(): return await url["function"]()
            
        
        self.__app.include_router(self.__router)