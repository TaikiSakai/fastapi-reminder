from fastapi import FastAPI, APIRouter
# from app.api.v1 import router
from app.presentation.handler.user_handler import UserHandler


app = FastAPI()

# app.include_router(router.v1_router, prefix="/v1")
# app.include_router(user.ddd_router, prefix="/ddd")

user_handler = UserHandler()
user_handler.register_routes(app)


@app.get("/health_check")
def health_check():
    return {'status': 'Healthyyyyyy'}
