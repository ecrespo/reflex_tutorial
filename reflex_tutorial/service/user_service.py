from typing import List

from reflex_tutorial.model.user_model import User
from reflex_tutorial.repository.user_repository import select_all, select_user_by_email, create_user, delete_user


def select_all_users_service()-> list[User]:
    users = select_all()
    return users


def select_user_by_email_service(email: str)-> List[User]:
    if len(email) == 0:
        users = select_all()
        return users

    user = select_user_by_email(email)
    return user

def create_user_service(username: str, password: str, phone: str, name: str) -> List[User]:

    users = select_user_by_email(username)
    if len(users) > 0:
        print("User already exists")
        raise BaseException("User already exists")

    user_saved = User(username=username, password=password, phone=phone, name=name)
    create_user(user_saved)
    return create_user(user_saved)


def delete_user_service(email: str) -> List[User]:
    return delete_user(email)


def update_user_service(email: str) -> List[User]:
    return delete_user(email)
