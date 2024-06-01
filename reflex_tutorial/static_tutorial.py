import reflex as rx


css: dict = {
    "_dark": {"bg": "#1f2028"},
    "_light": {"bg": "#fafafa"},
    "main": {
        "width": "100%",
        "height": "100vh",

    },
    "header": {
        "_dark": {"bg": "#141518"},
        "_light": {"bg": "#ffffff"},
        "width": "100%",
        "height": "50px",
        "padding": ["0 1rem", "0 1rem", "0 4rem", "0 10rem"],
        "transition": "all 300ms ease",
        "box_shadow": "0px 8px 16px 0px rgba(0,0,0,0.25)",
    },
    "content": {
        "width": "100%",
        "height": "inherit",
        "padding": "4rem 0rem",
    },
    "footer": {
        "width": "100%",
        "height": "60px",
        "bg": "#141518",
        "padding": ["0 1rem", "0 1rem", "0 4rem", "0 10rem"],
    }
}

class Header(rx.chakra.Hstack):
    def __init__(self) -> rx.hstack:
        super().__init__(style=css["header"])
        self.children = [
            rx.heading("Static Site", size="5"),
            rx.spacer(),
            rx.color_mode.button(position="top-right"),
            # rx.chakra.color_mode_button(
            #
            #     rx.chakra.color_mode_icon(),
            #     color_schema="none",
            #     _dark={"color": "white"},
            #     _light={"color": "black"},
            # ),
        ]


class Content(rx.chakra.Vstack):
    def __init__(self) -> rx.vstack:
        super().__init__(style=css["content"])
        self.children = [
            rx.heading(
                "Static site content area",
                size="5",
                transition="all 300ms ease",
            ),
        ]


class Footer(rx.chakra.Hstack):
    def __init__(self) -> rx.hstack:
        super().__init__(style=css["footer"])
        self.children = [
            rx.text("Created with Reflex",color="white"),
            rx.spacer(),
            rx.link(
                rx.image(
                    src="/github.svg",
                    html_width="26px",
                    html_height="26px",
                    filter="brightness(0) invert(1)",
                ),
                href="https://github.com/reflex-ui/reflex",
                is_external=True,
                color="white",
                transition="all 300ms ease",
            ),
        ]


@rx.page(route="/static_tutorial", description="Static Tutorial")
def static_tutorial() -> rx.Component:
    header: rx.chakra.Hstack =  Header()
    content: rx.chakra.Vstack = Content()
    footer: rx.chakra.Hstack = Footer()
    return rx.vstack(
        header,
        content,
        footer,
        style=css["main"],
    )