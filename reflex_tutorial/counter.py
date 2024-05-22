import reflex as rx


class StateCounter(rx.State):
    """The app state."""
    index: int = 0

    def increment(self):
        self.index += 1

    def decrement(self):
        self.index -= 1

    @rx.var
    def get_index(self) -> int:
        return self.index

    def reset_index(self):
        self.index = 0

@rx.page(route="/counter",title="Contador")
def counter() -> rx.Component:
    """Counter Page"""
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading("Contador", size="9"),
                rx.text("Mi primer contador en Reflex!"),
                rx.hstack(
                    rx.button("-", on_click=StateCounter.decrement),
                    rx.text(StateCounter.get_index),
                    rx.button("+", on_click=StateCounter.increment),
                ),
                rx.button("Reset", on_click=StateCounter.reset_index),
            ),
            align_items="center",
        )
    )
