from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/',response_class = HTMLResponse)
async def home(request: Request):
    sent = 'Press Enter to read. When prompted a question, use f for yes and j for no.'
    return templates.TemplateResponse('home.html', {'request':request, 'sent':sent})

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.post('/go/{scnt}/{wcnt}')
async def go(request: Request, scnt:str, wcnt:str):
    ls = []
    scnt = int(scnt)
    ls.append({'s':'While the mother washed the baby puked on the floor','q':'did the mom wash the baby?','a':'no'})
    ls.append({'s':'While the mother washed, the baby puked on the floor','q':'did the baby puke on the floor?','a':'yes'})
    ls.append({'s':'This is a sentence without question','q':'','a':''})
    ls.append({'s':'The horse raced past the barn fell','q':'did the barn fall?','a':'no'})
    ls.append({'s':'This is the last sentence of this experiment.','q':'OK?','a':'yes'})
    # above is dataframe preprocessing, below is communiation
    
    sent = ls[scnt]['s']
    q = ls[scnt]['q']
    a = ls[scnt]['a']

    #  read next word within the sentence
    #  r = templates.TemplateResponse('inplace.html',{'request':request, 'sent':sent})
    #  rendered_sent = r.template.render(r.context)
    content = {'s':sent,'scnt':scnt,'wcnt':wcnt,'q':q,'a':a}
    json_data = jsonable_encoder(content)
    print(f'q is {q}, scnt is {scnt}')
    print(json_data)
    return json_data
