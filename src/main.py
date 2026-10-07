from fastapi import FastAPI

from api.v1.auth import router as auth_router
import models

app = FastAPI(
    title="ManiGPT API",
    version="1.0.0",
)


app.include_router(
    auth_router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {
        "message": "ManiGPT API is running",
    }
