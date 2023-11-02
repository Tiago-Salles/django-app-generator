class CreatedModelsView:

    models = [
        {
            "model": "ProductModel",
            "fields" : []
        },
    ]
    
    async def get_all_models(self):
        return {"response" : self.models}