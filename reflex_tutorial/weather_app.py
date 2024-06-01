import reflex as rx
import os
import requests
import asyncio
import json

from dotenv import load_dotenv

load_dotenv()

API_KEY:str = os.getenv("API_KEY")

WIDTH: list[str] = ["90%", "80%", "70%", "65%", "55%"]

css: dict = {
    "app": {"_dark": {"bg": "#1f2028"}},
    "main": {"width": "100%", "height": "100vh"},
    "header": {
        "width": "100%",
        "height": "50px",
        "box_shadow": "0px 8px 16px 0px rgba(0,0,0,0.25)",
        "padding": ["0 1rem","0 1rem","0 1rem","0 4rem","0 10rem"],
        "_dark": {"bg": "#141518"},
        "_light": {"bg": "#ffffff"},
        "transition": "all 300ms ease",
    },
    "input": {
        "width": WIDTH,
        "height": "70px",
        "text_align": "left",
        "font_size": "32px",
        "transition": "all 300ms ease",
    },
    "stack": {
        "width": "100%",
        "align_items": "center",
        "justify_content": "center",
        "display": "flex",
        "padding_top": "4rem",
    },
    "content": {
        "width": WIDTH,
        "transition": "all 300ms ease",
        "border_radius": "10px",
        "display": "flex",
        "overflow": "hidden",
        "box_shadow": "0px 10px 20px 0px rgba(0,0,0,0.5)",
    },
}


class WeatherState(rx.State):

    location: str = ""
    city: str = ""
    country: str = ""
    temp: str = ""
    speed: str = ""
    humidity: str = ""
    image_src: str = ""
    user_input: str = ""
    content_height: str = "0px"
    content_bg: str = ""

    def get_input_value(self, user_input: str) -> None:
        self.user_input = user_input

    async def route_after_key_press(self, key):
        if key == "Enter" and self.user_input!= "":
            self.expand_content_height()
            await self.give_content_bg()
            await self.get_weather_data()

    async def give_content_bg(self):
        await asyncio.sleep(0.75)
        if self.content_bg != "#fafafa":
            self.content_bg = "#fafafa"

    def expand_content_height(self):
        if self.content_height!= "250px":
            self.content_height = "250px"

    async def get_weather_data(self):
        __city__: str = self.user_input
        response = requests.get(get_weather_request(__city__))
        await asyncio.sleep(0.5)

        if response.status_code == 200:
            data = response.json()
            
            self.city = __city__
            self.country = data["sys"]["country"]
            self.temp = f"{int(data['main']['temp'])} °C"
            self.speed = f"{int(data['wind']['speed'])} km/h"
            self.humidity = f"{int(data['main']['humidity'])} %"
            self.location = f"{self.city.capitalize()}, {self.country}"

            if data["weather"][0]["main"].lower() in  ["clear","sun"]:
                self.image_src = "/sun.png"

            if data["weather"][0]["main"].lower() in ["cloud", "clouds"]:
                self.image_src = "cloud.png"

            if data["weather"][0]["main"].lower() == "rain":
                self.image_src = "/rain.png"

            if data["weather"][0]["main"].lower() == "snow":
                self.image_src = "/snow.png"
            else:
                self.image_src = "/partly-cloudy.png"

            self.user_input



def get_weather_request(city:str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    return url



class Header(rx.chakra.Hstack):

    def __init__(self):
        super().__init__(style=css.get("header"))
        self.toogle: rx.Component = rx.color_mode.button(
            rx.chakra.color_mode_icon(),
            color_schema="None",
            position="top-right",
            _dark={"color": "white"},
            _light={"color": "black"},
        )
        self.title = rx.heading("Weather App", size="5")

        self.children = [
            self.title,
            rx.spacer(),
            self.toogle,
        ]


@rx.page(route="/weather", title="Weather App",description="Weather App")
def weather_app() -> rx.Component:
    header: rx.chakra.Hstack = Header()
    return rx.vstack(
        header,
        rx.vstack(
            rx.box(
                rx.text(
                    "1. Enter a city name to get the weather forecast.",
                    align="left",
                    font_weight="bold",
                ),
                width=WIDTH,
            ),
            rx.input(
                value=WeatherState.user_input,
                on_change=WeatherState.get_input_value,
                on_key_down=WeatherState.route_after_key_press,
                style=css.get("input"),
            ),
            style=css.get("stack"),
        ),
        rx.divider(height="2em", border_color="transparent"),
        rx.hstack(
            rx.container(
                rx.vstack(
                    # image of sun
                    rx.heading(WeatherState.location, size="4"),
                    rx.image(
                        src=WeatherState.image_src,
                        html_height="128px",
                        html_width="128px",
                        filter="brightness(0) invert(1)",

                    ),

                    color="white",
                    spacing="0",
                    width="100%",
                    height="inherit",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                width=["30%", "30%", "30%", "35%", "35%"],
                height="inherit",
                bg="#3e8be7",
            ),
            rx.container(
                rx.hstack(
                    rx.vstack(
                        rx.heading(WeatherState.temp, size="2"),
                        rx.text("TEMP",
                                font_size="10px",
                                font_weight="bold",
                                opacity="0.6",
                                ),
                        spacing="0",
                    ),
                    rx.vstack(
                        rx.heading(WeatherState.speed, size="2"),
                        rx.text("SPEED",
                                font_size="10px",
                                font_weight="bold",
                                opacity="0.6",
                                ),
                        spacing="0",
                    ),
                    rx.vstack(
                        rx.heading(WeatherState.humidity, size="2"),
                        rx.text("HUMIDITY",
                                font_size="10px",
                                font_weight="bold",
                                opacity="0.6",
                                ),
                        spacing="0",
                    ),
                    width="100%",
                    height="inherit",
                    display="flex",
                    align_items="center",
                    justify_content="space-between",
                    color="black",
                ),
                width=["70%", "70%", "70%", "65%", "65%"],
                height="inherit"
            ),
            height=WeatherState.content_height,
            bg=WeatherState.content_bg,
            style=css.get("content"),
            spacing="0",
        ),
        rx.logo(),
        style=css.get("main")
    )