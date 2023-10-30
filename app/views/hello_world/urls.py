from app.core.utils.http_method import HttpMethod
from app.views.hello_world.hello_world import HelloWorldView

class HelloWorldUrls:

    view = HelloWorldView()

    URLS = [
        {   
            "function" : view.get(),
            "method" : HttpMethod.GET,
            "path" : "/hello-world"
        }
    ]