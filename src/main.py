from fastapi import FastAPI
from src.api.routers.user_router import router as user_router
from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container
from src.ioc_container import AppProvider
from src.config import Config

app = FastAPI()
app.include_router(user_router, prefix="/users")
config = Config()

container = make_async_container(AppProvider(), context={Config: config})
setup_dishka(container=container, app=app)
