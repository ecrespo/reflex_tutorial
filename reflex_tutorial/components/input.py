import reflex as rx

from reflex_tutorial.components.entry import render_text_entry, render_key_value_entries

from reflex_tutorial.states.StatusState import StateFather, WebObject, Update, AddObject, ResetObject

BOX: dict = {
    "overflow": "hidden",
    "flex": ["100%", "100%", "100%", "30%", "30%"],
    "entry_ui": {
        "border_bottom": "1px solid #373a3e",
        "width": "100%",
        "title": {"font_size": "12px"},
    },
    "key_value_stack": {
        "width": "100%",
        "border_top": "1px solid red",
        "border_bottom": "1px solid #404040",
        "padding_left": ["1rem", "1rem", "1rem", "3rem", "3rem"]
    },
    "key_value_type": {
        "opacity": "0.61",
        "width": "60px",
        "font_size": "12px",
    },
    "vstack_web_object": {
        "width": "100%",
        "border_top": "1px solid red",
        "border_bottom": "1px solid #404040",
        "padding_left": ["1rem", "1rem", "1rem", "3rem", "3rem"]
    },
    "web_object": {
        "width": "100%",
        "border_bottom": "1px solid #373a3e",
        "padding": "1em 0em",
        "display": "flex",
        "align_items": "center",
        "justify_content": "space-between"
    }
}



def create_entry_ui(title: str, component: rx.Component) -> rx.Component:
    return rx.vstack(
        rx.text(title,style=BOX.get("entry_ui").get("title")),
        component,
        spacing="0",
        style=BOX.get("entry_ui"),
    )


def create_key_value_entry_ui(object: WebObject) -> rx.Component:
    return rx.hstack(
        rx.text(f"-{object.type}"),
        *render_key_value_entries(
            item=object,
            _key_update=lambda e: Update.key(e, object),
            _key_value=lambda e: Update.value(e, object),
            #
        ),
        style=BOX.get("vstack_web_object")
    )


def create_web_object_ui(title: str, _type_: str) -> rx.Component:
    return rx.hstack(
        rx.text(title, font_size="12px"),
        rx.spacer(),
        rx.badge(
            _type_,
            color_scheme="grass",
            size="1",
            on_click=AddObject.add(_type_),

        ),
        rx.badge(
            "R",
            color_scheme="ruby",
            size="1",
            on_click=ResetObject.reset_list(_type_),
        ),
        style=BOX.get("web_object")

    )


def render_input_box() -> rx.Component:
    return rx.vstack(
        create_entry_ui(
            title="Supabase API Key",
            component=rx.box(
                render_text_entry(
                    value=StateFather.api_key,
                    placeholder="Supabase API Key",
                    update=StateFather.set_api_key,
                ),
                width="100%"
            ),
        ),
        create_entry_ui(
            title="Supabase Project URL",
            component=rx.box(
                render_text_entry(
                    value=StateFather.project_url,
                    placeholder="Supabase Project URL",
                    update=StateFather.set_project_url,
                ),
                width="100%"
            ),
        ),
        create_entry_ui(
            title="Node Name",
            component=rx.box(
                render_text_entry(
                    value=StateFather.node,
                    placeholder="Node",
                    update=StateFather.set_node,
                ),
                width="100%"
            ),
        ),
        create_entry_ui(
            title="Method",
            component=rx.box(
                render_text_entry(
                    value=StateFather.method,
                    placeholder="Method",
                    update=StateFather.set_method,
                ),
                width="100%"
            ),
        ),
        rx.vstack(
            create_web_object_ui(title="Header", _type_="H"),
            rx.foreach(
                iterable=StateFather.headers,
                render_fn=create_key_value_entry_ui,
            ),
            width="100%",
        ),
        rx.vstack(
            create_web_object_ui(title="Data", _type_="D"),
            rx.foreach(
                iterable=StateFather.datas,
                render_fn=create_key_value_entry_ui,
            ),
            width="100%",
        ),


        spacing="5",
        style=BOX
    )
