import reflex as rx
from reflex_tutorial.components.title import render_title
from reflex_tutorial.components.status import render_status
from reflex_tutorial.states.StatusState import StatusState
from reflex_tutorial.components.input import render_input_box


CLIENT: dict = {
    "width": "100%",
    "display": "flex",
    "justify_content": "start",
    "align_items": "center",
    "title_status": {
        "width": "100%",
        "display": "flex",
        "flex_wrap": ["wrap-reverse", "wrap-reverse", "wrap-reverse", "wrap","wrap"],
        "justify_content": "space-between",
        "align_items": "center",
        "gap": "1em 0.4em",
        "padding": ["2em 2em", "2em 2em", "2em 4em", "2em 4em", "2em 4em"]
    },
    "data_boxes": {
        "width": "100%",
        "display": "flex",
        "align_items": "start",
        "justify_content": "start",
        "flex_wrap": [
            "wrap-reverse",
            "wrap-reverse",
            "wrap-reverse",
            "wrap",
            "wrap"
        ],
        "padding": ["2em 2em", "2em 2em", "2em 4em", "2em 4em", "2em 4em"]
    },
}

theme_btn: rx.Component = rx.button(
    rx.color_mode_cond(
        light=rx.icon(tag="moon"),
        dark=rx.icon(tag="sun"),
    ),
    variant="ghost",
    on_click=rx.toggle_color_mode,
)


@rx.page(route="/restapi_client", title="REST API Client",on_load=[StatusState.get_status])
def restapi_client() -> rx.Component:
    return rx.vstack(
        theme_btn,
        rx.hstack(
            render_title(),
            render_status(),
            style=CLIENT.get("title_status")
        ),
        rx.box(
            rx.divider(size="3", width="100%"),
            padding=CLIENT.get("title_status").get("padding"),
            width="100%",
        ),
        rx.hstack(
            # output box
            # input box
            render_input_box(),
            spacing="6",
            style= CLIENT.get("data_boxes")
        ),
        style=CLIENT,
    )