from core.utils.http_method import HttpMethod
from presentations.hello_world.hello_world import HelloWorldView

class HelloWorldUrls:

    view = HelloWorldView()

    URLS = [
        {   
            "function" : view.hello,
            "method" : HttpMethod.GET,
            "path" : "/hello",
            "tags": ["hello"],
        },
        {   
            "function" : view.just_hello,
            "method" : HttpMethod.GET,
            "path" : "/just",
            "tags": ["hello"],
        }
    ]