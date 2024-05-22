import random

import reflex as rx


class StateCount(rx.State):
    count: int = 0
    def random(self):
        self.count = random.randint(0, 100)

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    @rx.var
    def get_count(self) -> int:
        return self.count

@rx.page(route="/tutorial3", title="Tutorial 3")
def tutorial3() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                StateCount.get_count,
                size="9"
            ),
            rx.hstack(
                rx.button(
                    "Decrement",
                    on_click=StateCount.decrement,
                    color_scheme="red"
                ),
                rx.button(
                    "Randomize",
                    on_click=StateCount.random,
                    background_image="linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(0,176, 34,1) 100%",
                    color="white"
                ),
                rx.button(
                    "Increment",
                    on_click=StateCount.increment,
                    color_scheme="green"
                ),
            ),
            padding="1em",
            bg="#ededed",
            border_radius="1em"
        ),
        padding_y="5em",
        font_size="2em",
        text_align="center",
        height="100vh"
    )
