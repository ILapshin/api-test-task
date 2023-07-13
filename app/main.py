from fastapi import FastAPI


from . import models
from .database import engine
from .routers import files, metadata


app = FastAPI()

app.include_router(files.router)
app.include_router(metadata.router)

models.Base.metadata.create_all(engine)
