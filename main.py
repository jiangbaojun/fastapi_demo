import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), "views")
print(static_dir)
app.mount("/static", StaticFiles(directory=static_dir), name="views")

@app.get("/")
async def hello():
    return RedirectResponse(url="/static/index.html", status_code=301)
    # return "hello"


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
