import asyncio
from typing import List

import reflex as rx

from reflex_tutorial.model.user_model import User
from reflex_tutorial.notify import notify_component
from reflex_tutorial.service.user_service import select_all_users_service, select_user_by_email_service, \
    create_user_service,delete_user_service


class UserState(rx.State):

    users: List[User]
    user_key: str
    error: str = ""

    async def  handle_notify(self):
        async with self:
            await asyncio.sleep(3)
            self.error = ""



    @rx.background
    async def get_all_users(self):
        async with self:
            self.users = select_all_users_service()


    @rx.background
    async def select_user_by_email(self):
        async with self:
            self.users = select_user_by_email_service(self.user_key)


    @rx.background
    async def delete_user_by_email(self,email):
        async with self:
            self.users = delete_user_service(email)

    @rx.background
    async def create_user(self, data:dict):
        username = data.get("username")
        password = data.get("password")
        phone = data.get("phone")
        name = data.get("name")
        async with self:
            try:
                self.users = create_user_service(username, password, phone, name)
            except BaseException as e:
                print(e.args)
                self.error = str(e.args)
        await self.handle_notify()


    @rx.var
    def get_users(self) -> List[User]:
        return self.users

    @rx.var
    def get_user_key(self) -> str:
        return self.users


    def search_on_change(self, value: str) -> None:
        self.user_key = value




def delete_user_dialog_component(username: str) -> rx.Component:
    return rx. dialog.root(
        rx.dialog.trigger(rx.button(rx.icon("trash-2"))),
        rx.dialog.content(
            rx.dialog.title("Eliminar usuario"),
            rx.dialog.description(f"¿Estás seguro de eliminar el usuario: {username}?"),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft"),
                ),
                rx.dialog.close(
                    rx.button("Confirmar",on_click=UserState.delete_user_by_email(username)),
                ),
                spacing="3",
                margin_top="16px",
                justify="end"
            )
        )
    )
def row_table(user: User) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.username),
        rx.table.cell(user.phone),
        rx.table.cell(rx.hstack(
            # rx.button(rx.icon("pencil")),
            delete_user_dialog_component(user.username),
            )
        )
    )


def table_user(lst_users: List[User]) -> rx.Component:

    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Correo"),
                rx.table.column_header_cell("Telefono"),
                rx.table.column_header_cell("Acción"),
            ),
        ),
        rx.table.body(
            rx.foreach(lst_users, row_table)
        )
    )


def search_user_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ingrese email", on_change=UserState.search_on_change),
        rx.button("Buscar usuario",on_click=UserState.select_user_by_email)

    )


def create_user_form_component() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(placeholder="Nombre", name="name"),
            rx.input(placeholder="Email", name="username"),
            rx.input(placeholder="Telefono", name="phone"),
            rx.input(placeholder="Contraseña", name="password"),
            rx.dialog.close(
                rx.button("Guardar", type="submit")
            ),
        ),
        on_submit=UserState.create_user
    )


def create_user_dialog_component() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Crear usuario")),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Crear usuario"),
                create_user_form_component(),
                justify="center",
                align="center",
                direction="column",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar",color_scheme="gray",variant="soft")
                ),
                spacing="3",
                margin_top="16px",
                justify="end"
            ),
            style={"width": "300px"}
        )
    )


@rx.page(route="/users", title="Users", on_load=UserState.get_all_users)
def user_page() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading("Usuarios", size="9", align="center"),
            search_user_component(),
            create_user_dialog_component(),
            table_user(UserState.get_users),
            justify="center",
            style={"margin-top": "30px"}
        ),
        rx.cond(
            UserState.error != "",
            notify_component(UserState.error, "shield-alert", "yellow"),
        ),
        justify="center",
        direction="column",
        style={"width": "60vw", "margin": "auto"}
    )
