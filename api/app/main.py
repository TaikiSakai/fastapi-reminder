from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.presentation.handler.user_handler import router


app = FastAPI()
app.include_router(router)
add_pagination(app)


@app.get("/health_check")
def health_check():
    return {'status': 'Healthyyyyyy'}
