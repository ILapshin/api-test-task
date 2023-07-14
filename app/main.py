from fastapi import FastAPI


from . import models
from .database import engine
from .routers import (
    files, 
    metadata, 
    users,
    auth
)


app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(files.router)
app.include_router(metadata.router)

models.Base.metadata.create_all(engine)
