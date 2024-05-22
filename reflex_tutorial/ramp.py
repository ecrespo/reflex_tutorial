import reflex as rx
import requests as rq

class StateApi(rx.State):
    list_personajes: list[dict] = []


    @rx.background
    async def get_personajes(self):
        async with self:
            response = rq.get("https://rickandmortyapi.com/api/character")
            self.list_personajes = response.json()["results"]

    @rx.var
    def get_list_personajes(self) -> list[dict]:
        list_person_to_card: list[dict] = []
        for personaje in self.list_personajes:
            person = {
                "name": personaje["name"],
                "location": personaje["location"]["name"],
                "image": personaje["image"],
            }
            list_person_to_card.append(person)
        return list_person_to_card


def CardPersonaje(personaje: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(personaje["name"] ,size="6"),
            rx.image(src=personaje["image"], width="100%"),
            rx.hstack(
                rx.text("location: "),
                rx.text(personaje["location"]),
            )
        )

    )

@rx.page(route="/ramp", title="Rick and Morty page", on_load=StateApi.get_personajes)
def ramp() -> rx.Component:
    return rx.vstack(
        rx.heading(
            rx.text("Rick and Morty", size="9"),
        ),
        rx.foreach(StateApi.get_list_personajes, CardPersonaje),
        # rx.button("log",on_click=rx.console_log(StateApi.get_list_personajes)),
    )
