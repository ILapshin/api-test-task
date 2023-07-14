from fastapi import FastAPI


from . import models
from .database import engine
from .routers import files, metadata, users


app = FastAPI()

app.include_router(files.router)
app.include_router(metadata.router)
app.include_router(users.router)

models.Base.metadata.create_all(engine)
