from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI(title="User Registration API")
app.include_router(user_router)