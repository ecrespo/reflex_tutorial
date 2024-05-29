import reflex as rx


class PortfolioState(rx.State):
    pass


dots: dict = {
    "@keyframes dots": {
        "0%": {
            "background_position": "0 0"
        },
        "100%": {
            "background_position": "40px 40px"
        }
    },
    "animation": "dots 4s linear infinite alternate-reverse both",
}


wave:dict = {
    "@keyframes wave": {
        "0%": {
            "transform": "rotate(45deg)"
        },
        "100%": {
            "transform": "rotate(-15deg)"
        }
    },
    "animation": "wave 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite alternate-reverse both",
}


css: dict = {
    "app": {
        "_dark": {
            "bg": "#15171b"
        }
    },
    "header": {
        "width": "100%",
        "height": "50px",
        "padding": ["0rem 1rem","0rem 1rem","0rem 1rem","0rem 8rem","0rem 8rem"],
        "transition": "all 550ms ease",
    },
    "main": {
        "property": {
            "width": "100%",
            "height": "84vh",
            "padding": "15rem 0rem",
            "align_items": "center",
            "justify_content": "start",
        }
    },
    "footer": {
        "width": ["100%", "90%", "60%", "45%", "45%"],
        "height": "50px",
        "align_items": "center",
        "justify_content": "center",
    }
}

class Header:
    def __init__(self):
        self.header: rx.Hstack = rx.hstack(style=css["header"])
        self.email: rx.Hstack = rx.hstack(
            rx.box(rx.icon(tag="mail", _dark={"color": "rgba(255, 255, 255, 0.5)"})),
            rx.box(rx.text("ecrespo@gmail.com", _dark={"color": "rgba(255, 255, 255, 0.5)"})),
            align_items="center",
            justify_content="center"
        )
        self.theme: rx.Component = rx.color_mode.button(
            rx.chakra.color_mode_icon(),
            color_scheme="gray",
            _light={"color": "black"},
            _dark={"color": "white"},
        )

    def compile_components(self):
        return [
            self.email,
            rx.spacer(),
            self.theme,
        ]

    def build(self):
        self.header.children = self.compile_components()
        return self.header


class Main:
    def __init__(self):
        self.box: rx.Box = rx.box(width="100%")
        self.name: rx.Hstack = rx.hstack(
            rx.heading(
                "Hi - 👨 I'm Seraph",
                font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"],
                font_weight="900",
                _dark={
                    "background": "linear-gradient(to right, #e1e1e1, #757575)",
                    "background_clip": "text",
                }
            ),
            rx.heading("👋", size="5",style=wave),
            spacing="2",
        )
        self.badge_stack_max: rx.Hstack = rx.hstack(spacing="1")
        self.badge_stack_min: rx.Vstack = rx.vstack(spacing="2")
        titles: list = ["Python Developer","Data Engineer", "Data Scientist", "Machine Learning Engineer"]
        self.badge_stack_max.children = [self.create_badges(title) for title in titles]
        self.badge_stack_min.children = [self.create_badges(title) for title in titles]
        self.crumbs: rx.chakra.Breadcrumb = rx.chakra.breadcrumb()
        data: list = [
            ["/github.svg", "Github", "#"],
            ["/linkedin.svg", "Linkedin", "#"],
            ["/x.svg", "X", "#"],
        ]
        self.crumbs.children = [self.create_breadcrumb_item(path, title, url) for path, title, url in data]

    def create_breadcrumb_item(self, path: str, title: str, url: str|None):
        return rx.chakra.breadcrumb_item(
            rx.hstack(
                rx.image(
                    src=path,
                    html_width="24px",
                    html_height="24px",
                    _dark={"color": "rgba(255,255,255,0.7)"}
                ),
            )
        )

    def create_badges(self, title: str):
        return rx.badge(
            title,
            variant="solid",
            padding=[
                "0.15rem 0.35rem",
                "0.15rem 0.35rem",
                "0.15rem 1rem",
                "0.15rem 1rem",
                "0.15rem 1rem",
            ]
        )


    def compile_mobile_component(self):
        return rx.mobile_only(
            rx.vstack(
                self.name,
                self.badge_stack_min,
                self.crumbs,
                style=css["main"]["property"]
            )
        )

    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                self.badge_stack_max,
                self.crumbs,
                style=css["main"]["property"],
                spacing="6"
            )
        )

    def build(self):
        self.box.children = [self.compile_desktop_component(), self.compile_mobile_component()]
        return self.box


class Footer:
    def __init__(self):
        self.footer: rx.Hstack = rx.hstack(style=css["footer"])
        self.footer.children.append(
            rx.text(
                "© 2024 Seraph",
                font_size= "10px",
                font_weight= "semibold"
            )
        )

    def build(self):
        return self.footer




@rx.page(route="/portfolio",description="Portfolio")
def portfolio() -> rx.Component:
    header: object = Header().build()
    main: object = Main().build()
    footer: object = Footer().build()
    return rx.vstack(
        # page background
        header,
        main,
        footer,
        _light={
            "background": "radial-gradient(circle, rgba(0,0,0,0.35) 1px, transparent 1px)",
            "backgroud_size" : "25px 25px",
        },
        background="radial-gradient(circle, rgba(255,255,255,0.09) 1px, transparent 1px)",
        backgroud_size="25px 25px",
        style=dots
    )