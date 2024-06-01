"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Bienvenidos a Reflex!", size="9"),
            rx.heading("Ejemplos: ", size="6"),
            rx.link("Contador", href="/counter", is_external=True),
            rx.link("Rick y Morty", href="/ramp", is_external=True),
            rx.link("Inicio de sesión 1", href="/login", is_external=True),
            rx.link("Inicio de sesión 2", href="/login2", is_external=True),
            rx.link("Usuarios", href="/users", is_external=True),
            rx.link("Reloj", href="/clock", is_external=True),
            rx.link("Calendario", href="/calendario", is_external=True),
            rx.link("Google Maps", href="/maps", is_external=True),
            rx.link("PDF Viewer", href="/pdfview", is_external=True),
            # rx.link("REST API Client", href="/restapi_client", is_external=True),
            rx.link("Portfolio", href="/portfolio", is_external=True),
            rx.link("Tutorial Estático", href="/static_tutorial", is_external=True),
            rx.link("Reflex Ollama IA", href="/reflex_ollama", is_external=True),
            rx.link("Weather App", href="/weather", is_external=True),
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
