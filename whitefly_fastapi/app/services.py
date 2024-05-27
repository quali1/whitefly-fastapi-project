from celery import Celery
from sqlalchemy.orm import sessionmaker
from .models import engine, User, SessionLocal
from .config import config

# from time import sleep

celery = Celery('tasks', broker='redis://redis', backend='redis://redis')


@celery.task
def add_user(name, email, gender, dob):
    session = SessionLocal()
    new_user = User(name=name, email=email, gender=gender, dob=dob, method="async")
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    session.close()
