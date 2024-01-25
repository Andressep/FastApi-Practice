from fastapi import FastAPI
from routes.user import user
##from docs import tags_metadata

app = FastAPI(
  title="FastAPI & Mongo CRUD for practice in Python",
  description="A Little type of api",
  version="0.0.1",
  ##openapi_tags=tags_metadata
)

app.include_router(user)