from fastapi import FastAPI, HTTPException, requests
from fastapi import staticfiles
from fastapi.responses import FileResponse
from fastapi. staticfiles import StaticFiles

app = FastAPI(title="UpgradedSelf.live")



@app.get('/')
def home():
    return {"message": "This is uploaded.self API default return statement"}

app.mount('/assets', StaticFiles(directory='./FrontEnd/dist/assets'), name='assets')
app.mount('/', StaticFiles(directory='./FrontEnd/dist'), name="root of SPA")

@app.exception_handler(404)
def SPA_fallback(request:requests, exc):
    return FileResponse('./FrontEnd/dist/index.html')
