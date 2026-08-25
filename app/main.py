from fastapi import FastAPI

app = FastAPI(title="AI Knowledge Search")


@app.get("/health")
def health():
    return {"status": "ok"}
