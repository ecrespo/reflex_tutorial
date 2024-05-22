import reflex as rx


def render_user_entries(title: str,is_password:bool =False) -> rx.Component:
    return rx.vstack(
        rx.text(title, color="gray",font_size="11px", weight="bold"),
        rx.chakra.input(color="white", type_="text" if not is_password else "password", width="100%",),
        width="100%",

    )


def render_trigger() -> rx.Component:
    return rx.badge(
        rx.text("Login", text_align="center",width="100%"),
        color_scheme="teal",
        variant="outline",
        size="2",
        width="100%",
        padding="0.75em 0em"
    )


def render_main_component() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="lock",size=28,color="rgba(127,127,127,1"),
            width="100%",
            height="55px",
            bg="#181818",
            border_radius="10px 10px 0px 0px",
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        rx.vstack(
            render_user_entries("Email"),
            render_user_entries("Password",is_password=True),
            rx.spacer(),
            render_trigger(),
            width="100%",
            padding="2em 2em 4em 2em",
            spacing="6",
        ),
        width=["100%", "100%", "65%", "50%", "35%"],
        bg="rgba(21,21,21, 0.55)",
        border="0.75px solid #2e2e2e",
        border_radius="10px",
        box_shadow="0px 8px 16px 6px rgba(0,0,0,0.25)"
    )

@rx.page(route="/login2", title="Inicio de sesión 2")
def login2() -> rx.Component:
    return rx.center(
        render_main_component(),
        width="100vw",
        height="100vh",
        padding="2em",
        bg="#121212",
    )