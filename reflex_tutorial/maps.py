import reflex as rx
from reflex_tutorial.components.gmaps_component import gmaps


@rx.page(route="/maps", title="Maps")
def maps() -> rx.Component:
    return rx.box(
        gmaps(),
        align="center",
        justify="center"
    )