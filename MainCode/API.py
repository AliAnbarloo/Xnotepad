from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Main import MyWindow, OPENFILE, NEWFILE

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

window_instance = MyWindow()
openfile_instance = OPENFILE()
newfile_instance = NEWFILE()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": None})

@app.get("/new_file")
async def read_item():
    return newfile_instance.NewFile()

@app.get("/open_file")
async def read_item():
    return openfile_instance.OpenFile()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
