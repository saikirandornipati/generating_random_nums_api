from fastapi import FastAPI
from .api import router  # Import your API router

app = FastAPI()

# Include the API router
app.include_router(router)

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello World"}
