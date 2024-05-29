import reflex as rx
from reflex_tutorial.states.StatusState import StatusState

STATUS: dict = {
    "text": {
        "font_size": "10px",
        "font_color": "#404040",
        "font_weight": "bold"
    },
    "stack": {
        "transition": "all 550ms ease 3s",
        "display": "flex",
        "justify_content": "center",
        "align_items": "center",
    }
}


def render_status() -> rx.Component:
    return rx.hstack(
        rx.text("Supabase", style=STATUS.get("text")),
        rx.badge(
            StatusState.status,
            color_scheme=StatusState.status_color,
            size="1",
            variant="outline",
        ),
        opacity=StatusState.opacity,
        style=STATUS.get("stack"),

    )