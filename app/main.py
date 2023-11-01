from infra.server.app_server import AppServer
import sys
sys.path.append("..")

app = AppServer().initialize_server()