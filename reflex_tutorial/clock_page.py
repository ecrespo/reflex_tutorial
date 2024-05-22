from datetime import datetime

import pytz
import reflex as rx
from reflex_tutorial.data import cities

class StateClock(rx.State):
    """The app state."""
    curr_hour: int = datetime.now().hour
    curr_minute: int = datetime.now().minute

    time: str
    city: str
    cities: list = cities

    css_hour: str = "rotate(90deg)"
    css_minute: str = "rotate(90deg)"

    clock_face: str = "inset 5px 5px 10px #0d0d0d, inset -5px -5px 10px  #333333"

    flat: str = "13px 13px 25px #0d0d0d, -13px -13px 25px #333333"
    pressed: str = "inset 5px 5px 10px #0d0d0d, inset -5px -5px 10px #333333"

    def change_clock_face(self, face: int):
        if face == 1:
            self.clock_face = self.pressed
        else:
            self.clock_face = self.flat

    async def return_minutes(self):
        value: float = ((self.curr_minute/60)* 360) + 90
        self.css_minute = f"rotate({value}deg)"

    async def return_hours(self):

        value: float = ((self.curr_hour % 12) * 30) + ((self.curr_minute) * 0.5 ) + 90
        self.css_hour = f"rotate({value}deg)"

    async def return_local_time_string(self):
        if self.curr_hour < 12 and self.curr_hour != 0:
            self.time = (f"{self.curr_hour}:{str(self.curr_minute).zfill(2)} AM")
        elif self.curr_hour == 12:
            self.time = (f"12:{str(self.curr_minute).zfill(2)} PM")
        else:
            self.time = (f"{self.curr_hour-12}:{str(self.curr_minute).zfill(2)} PM")

    async def update_user_input(self,city:str):

        self.city = city

    async def get_users_current_time(self):
        await self.return_minutes()
        await self.return_hours()
        await self.return_local_time_string()

    def split_list_item(self, item: str) -> str:
        return (item.split("/")[1].lower()
                if len(item.split("/")) > 1 else item.split("/")[0].lower())


    def format_users_city(self,item:str) -> str:
        item = item.split(" ") if " " in item else item
        item = "_".join(item) if isinstance(item, list) else item
        return item


    async def get_user_input(self):
        for item in cities:
            city: str = self.split_list_item(item)
            if self.format_users_city(self.city.lower()) == city:
                self.curr_hour = datetime.now(pytz.timezone(item)).hour
                self.curr_minute = datetime.now(pytz.timezone(item)).minute

        await self.get_users_current_time()


app_style = {
    "_dark": {"bg": "#202020"},
    "_light": {"bg": "#f5f5f5"},
}

inner_circle_style: dict = {
    "position": "absolute",
    "width":"32px",
    "height":"32px",
    "border": "1px solid #222222",
    "background": "linear-gradient(145deg, #222222, #1d1d1d)",
    "border_radius": "50%",
    "top": "50%",
    "left": "50%",
    "transform": "translate(-50%, -50%)",
    "box_shadow": "8px 8px 16px #141414, -8px -8px 16px #2c2c2c",
    "z_index": "11",
}

clock_style: dict = {
    "width": "30rem",
    "height": "30rem",
    "position": "relative",
    "padding": "2rem",
    "border": "3px solid #2929292",
    "margin": "50px auto",
    "border_radius": "50%",
    "background": "#202020",
    "box_shadow": StateClock.clock_face,
    "transition": "all 700ms ease",
}

hand_style: dict = {
    "width": "20%",
    "right": "50%",
    "height": "2px",
    "background": "#61afff",
    "position": "absolute",
    "top": "50%",
    "border-radius": "6px",
    "transform_origin": "100%",
    "transition-timing-function": "cubic-bezier(0.1, 2.7, 0.58, 1)",
    "transition": "all 700ms ease",
}

hand_hour_style: dict = {"transform": StateClock.css_hour}
hour: dict = {**hand_style, **hand_hour_style}

hand_minute_style: dict = {"transform": StateClock.css_minute}
minute: dict = {**hand_style, **hand_minute_style}

# hand_second_style: dict = {"transform": StateClock.css_second}
# second: dict = {**hand_style, **hand_second_style}

stack_style: dict = {
    "width": "100%",
    "display": "flex",
    "align_items": "start",
    "justify_content": "center",

}


def return_sub_text(value: str) -> rx.Component:

    return rx.text(
            value,
            color="white",
            font_size="12px",
            opacity="0.81",
            font_weight="bold",
            font_family="Teko",
        )


def return_clock_face_btn(value: str, num: int) -> rx.Component:
    return rx.button(
        rx.hstack(
        rx.icon(tag="alarm_clock", color="white"),
        rx.text(value, color="white"),
        ),
        width="10rem",
        _hove={"variant": "solid"},
        on_click=StateClock.change_clock_face(num),
    )




@rx.page(route="/clock", title="Reloj",on_load=StateClock.get_users_current_time)
def clock_page() -> rx.Component:
    return rx.flex(
        rx.heading("Reloj", size="9", color="white"),
        rx.vstack(
                rx.vstack(
                    rx.container(
                        rx.container(style=inner_circle_style),
                    rx.container(width="25%",style=hour, bg="cyan"),
                    rx.container(width="40%",style=minute, bg="cyan"),
                    style=clock_style
                ),

        ),
        rx.vstack(
            rx.vstack(
                return_sub_text("CITY-NAME"),
                rx.hstack(
                    rx.input(
                        height="50px",
                        font_size="24px",
                        # bg="black",
                        on_change=StateClock.update_user_input,
                        style={"background": "#202020", "color": "white"}
                    ),
                    rx.button("Get", on_click=StateClock.get_user_input),
                    spacing="1",
                ),
                style=stack_style,
            ),
            rx.vstack(
                return_sub_text("LOCAL TIME"),
                rx.text(
                    StateClock.time,
                    font_size="64px",
                    color="white",
                    font_family="Teko",
                ),
                style=stack_style,
                spacing="0",
            ),
            rx.vstack(
                return_sub_text("CLOCK FACE"),
                rx.chakra.button_group(
                    return_clock_face_btn("Pressed", 1),
                    return_clock_face_btn("Flat", 2),
                    variante="outline",
                    is_attached=True,
                ),
                style=stack_style,
                spacing="1",
            ),
            spacing="2",
            display="flex",
            align_items="start",
            justify_content="center",
        ),
        width="100%",
        height="100vh",
        display="flex",
        align_items="center",
        justify_content="center",

        ),
        style=app_style["_dark"],
    )
