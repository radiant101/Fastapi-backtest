from fastapi import FastAPI
from app.database import connect_db, disconnect_db
from contextlib import asynccontextmanager
from app.routes import router
from app.moving_average_crossover import routers

@asynccontextmanager
async def lifespan(app: FastAPI):   #handling startup and shutdown using lifespan so that connect to db before causing error
    await connect_db()
    yield
    await disconnect_db()

app = FastAPI(lifespan=lifespan) 


@app.get("/")
async def root():
    return {"message":"fastapi is connected to postgres"}

app.include_router(router)
app.include_router(routers)