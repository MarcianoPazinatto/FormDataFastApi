import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.view.form_view import form_data_views


app = FastAPI()
app.include_router(form_data_views)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

if __name__ == '__main__':
    uvicorn.run(app, debug=True)
