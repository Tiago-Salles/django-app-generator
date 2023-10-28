from app.views.hello_world import HelloWorldView
from app.core.utils.http_method import HttpMethod

URLS = [
    {   
        "view" : HelloWorldView,
        "method" : HttpMethod.GET,
        "path" : "/hello-world"
    }
]
