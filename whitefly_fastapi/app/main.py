from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import router
from .models import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
