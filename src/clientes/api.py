from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API CRUD Clientes funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}