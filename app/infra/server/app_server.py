from fastapi import FastAPI
from app.infra.urls import URLS
from core.utils.http_method import HttpMethod

class AppServer:

    _app = FastAPI()

    async def initialize_server(self):
        try:
            await self.initialize_routes()
        except Exception as e:
            raise e 
        
    async def initialize_routes(self):
        for url in URLS:
            if url["method"] not in [HttpMethod]:
                raise "HTTP METHOD NOT ALLOWED"