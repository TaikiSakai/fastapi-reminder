from fastapi import FastAPI
from app.presentation.handler.user_handler import router


app = FastAPI()
app.include_router(router)


@app.get("/health_check")
def health_check():
    return {'status': 'Healthyyyyyy'}
