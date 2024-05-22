import re

import reflex as rx
import requests as rq


class StateLogin(rx.State):
    loader: bool = False
    username: str = "example@mail.com"
    password: str = ""
    error: bool = False
    response: dict = {}

    @rx.background
    async def login_service(self,data:dict):
        async with self:
            self.loader = True
            self.error = False
            response = rq.post(
                "http://127.0.0.1:5000/api/login",
                json=data,
                headers={"Content-Type": "application/json"},
            )
            if response.status_code == 200:
                self.response = response.json()
                self.loader = False
                return rx.redirect("/")
            else:
                self.loader = False
                self.error = True
                return False


    @rx.var
    def user_invalid(self) -> bool:
        return not(re.match(r"[^@]+@[^@]+.[^@]",self.username) and "example@mail.com")


    @rx.var
    def user_empty(self) -> bool:
        return not self.username.strip()


    @rx.var
    def password_empty(self) -> bool:
        return not self.password.strip()


    @rx.var
    def validate_fields(self)->bool:
        return (
            self.user_empty
            or self.user_invalid
            or self.password_empty
        )


style_section = {
    "height": "90vh",
    "width": "80%",
    "margin": "auto"
}

def field_form_component(label: str, placeholder: str, name_var: str, on_change_function, type_field: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name_var,
                    type=type_field,
                    required=True,
                ),
                as_child=True,
            ),
            rx.form.message(
                "El campo no puede estar vacío",
                match="valueMissing",
                color="red",
            ),
            direction="column",
            spacing="2",
            align="stretch",
        ),
        name=name_var,
        width="30vw",
    )

def field_form_component_general(label: str,
                                 placeholder: str,
                                 message_validate: str,
                                 name: str,
                                 on_change_function,
                                 show) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name,
                    required=True,
                ),
                as_child=True,
            ),
            rx.form.message(
                message_validate,
                name=name,
                match="valueMissing",
                force_match=show,
                color="red"
            ),
            direction="column",
            spacing="2",
            align="stretch",

        ),
        name=name,
        width="30vw",
    )



@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return rx.section(
    rx.flex(
            rx.image(src="/login.png", width="300px", border_radius="15px 50px"),
                    rx.heading("Inicio de sesión", size="9"),
                    rx.form.root(
                    rx.flex(
                    field_form_component_general("Usuario", "Ingrese su correo", "Ingrese un correo válido", "username",
                                                 StateLogin.set_username,StateLogin.user_invalid),
                            field_form_component("Contraseña", "Ingrese su contraseña", "password", StateLogin.set_password, "password"),
                            rx.form.submit(
                            rx.cond(
                                StateLogin.loader,
                                rx.chakra.spinner(color="red", size="xs"),
                                rx.button(
                                "Iniciar sesión",
                                        disabled=StateLogin.validate_fields,
                                        width="30vw",
                                )
                            ),
                            as_child=True,
                            ),
                        direction="column",
                        justify="center",
                        align="center",
                        spacing="2",

                    ),
                    rx.cond(
                        StateLogin.error,
                        rx.callout(
                            "Credenciales inválidas",
                            icon="triangle_alert",
                            color_scheme="red",
                            role="alert",
                            style={"margin_top": "10px"}
                        )
                    )
            ),
        width="100%",
        direction="column",
        align="center",
        justify="center",
        ),
        style=style_section,
        justify="center",
        width="80%",
    )



