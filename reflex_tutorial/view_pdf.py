import reflex as rx
from reflex_tutorial.components.pdfview_component import pdfview


@rx.page(route="/pdfview", title="Pdfview")
def view_pdf() -> rx.Component:
    return rx.box(
        pdfview(),
        align="center",
        justify="center"
    )