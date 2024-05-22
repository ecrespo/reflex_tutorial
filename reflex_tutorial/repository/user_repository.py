from typing import List

from sqlmodel import Session, select

from reflex_tutorial.model.user_model import User
from reflex_tutorial.repository.connect_db import connect


def select_all()-> List[User]:
    engine = connect()
    with Session(engine) as session:
        query = select(User)
        return session.exec(query).all()

def select_user_by_email(email: str)-> List[User]:
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.username == email)
        return session.exec(query).all()


def create_user(user: User)-> List[User]:
    engine = connect()
    with Session(engine) as session:
        session.add(user)
        session.commit()
        query = select(User)
        return session.exec(query).all()


def delete_user(email: str) -> List[User]:
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.username == email)
        user_delete = session.exec(query).one()
        session.delete(user_delete)
        session.commit()
        query = select(User)
        return session.exec(query).all()

def update_user_by_email(email: str) -> List[User]:
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.username == email)
        user_update = session.exec(query).one()
        session.update(user_update)
        session.commit()
        query = select(User)
        return session.exec(query).all()