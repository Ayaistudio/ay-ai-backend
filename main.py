from fastapi import FastAPI
app=FastAPI(title="AY AI Backend",version="1.0")
@app.get("/")
def home():
    return {"message":"Welcome to AY AI Backend","status":"online"}
@app.get("/health")
def health():
    return {"status":"ok"}
@app.get("/chat")
def chat(prompt:str):
    return {"user":prompt,"reply":"AY AI backend is working successfully."}
