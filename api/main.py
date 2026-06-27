from fastapi import FastAPI

app = FastAPI(
    title="Meal Planner AI API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Meal Planner AI Backend Running 🚀"
    }