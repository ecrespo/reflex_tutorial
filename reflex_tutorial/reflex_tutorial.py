import reflex as rx

from reflex_tutorial.components.circular_countdown_react import countdown


# https://www.youtube.com/watch?v=UygBVsDLeWI&ab_channel=emmakodes
# https://www.npmjs.com/package/circular-countdown-react?activeTab=readme


class State(rx.State):

    def display_value_on_done(self):
        print("done")

def index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading("Reflex countdown Demo"),
            countdown(size="large",total_seconds=10*24*3600,should_stop=False,on_done=State.display_value_on_done),
        ),
    )


app = rx.App()
app.add_page(index)
