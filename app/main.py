from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app import models
from app.database import engine
from app.routes import user, barman, manager, bar, drink, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(barman.router)
app.include_router(manager.router)
app.include_router(bar.router)
app.include_router(drink.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    html_content = "<h2>Hi bro! This is app for barmen</h2>"
    return HTMLResponse(content=html_content)


