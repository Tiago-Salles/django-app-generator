class HelloWorldView:
    
    async def hello(self):
        return {"response" : "Hello World"}
    
    async def just_hello(self):
        return {"response" : "Hello"}