from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from .models import User, get_db
from .services import add_user
from datetime import datetime

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    context = {'users': users}
    return templates.TemplateResponse(request=request, name="home.html", context=context)


@router.get("/regular_form", response_class=HTMLResponse)
async def regular_form_get(request: Request):
    return templates.TemplateResponse(request=request, name="regular_form.html")


@router.post("/regular_form")
async def regular_form_post(
        name: str = Form(...), email: str = Form(...), gender: str = Form(...), dob: str = Form(...),
        db: Session = Depends(get_db)
):
    dob = datetime.strptime(dob, '%Y-%m-%d')
    new_user = User(name=name, email=email, gender=gender, dob=dob, method="regular")
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}


@router.get("/async_form", response_class=HTMLResponse)
async def async_form(request: Request):
    return templates.TemplateResponse(request=request, name="async_form.html")


@router.post("/async_form")
async def async_form_post(name: str = Form(...), email: str = Form(...), gender: str = Form(...), dob: str = Form(...)):
    dob = datetime.strptime(dob, '%Y-%m-%d')
    add_user.delay(name, email, gender, dob)
    return {"message": "User creation task submitted successfully"}
