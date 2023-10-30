from app.infra.server.app_server import AppServer

async def main():
    await AppServer().initialize_server()
    

if __name__ == "__main__":
    main()