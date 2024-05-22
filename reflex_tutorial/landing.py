import reflex as rx


class LandingState(rx.State):
    """The app state."""
    pass


class Header:
    def __init__(self):
        self.header: rx.Hstack = rx.hstack()
        self.email: rx.Hstack = rx.hstack(
            rx.box(
                rx.icon(
                    tag="email",
                    _dark={"color": "rgba(255,255,255,0.5)"}
                )
            )
        )

    def compile_component(self) -> list:
        return []
    def build(self):
        ...

@rx.page(route="/landing", title="Landing")
def landing() -> rx.Component:
    return rx.vstack(

    )