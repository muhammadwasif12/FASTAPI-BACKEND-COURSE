from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.routes.issues import router as issues_router
from app.middleware.timing import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issues_router)


# items = [
#     {"id": 1, "name": "ItemOne"},
#     {"id": 2, "name": "ItemTwo"},
#     {"id": 3, "name": "ItemThree"},
# ]


# @app.get("/health")
# def health_check():
#     return {"status": "ok"}


# @app.get("/items")
# def get_items():
#     return items


# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     return {"error": "Item not Found"}


# @app.post("/items")
# def create_item(item:dict):
#     items.append(item)
#     return item
