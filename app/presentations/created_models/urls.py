from core.utils.http_method import HttpMethod
from presentations.created_models.created_models import CreatedModelsView


class CreatedModelsUrls:

    view = CreatedModelsView()

    URLS = [
        {   
            "function" : view.get_all_models,
            "method" : HttpMethod.GET,
            "path" : "/models",
            "tags": ["models"],
        }
    ]