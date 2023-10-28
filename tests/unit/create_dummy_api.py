from fastapi import FastAPI


def create_dummy_api() -> FastAPI:

    app = FastAPI()

    @app.get("/")
    def home():
        return {"hello": "world"}

    return app
