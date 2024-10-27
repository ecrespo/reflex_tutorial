import reflex as rx
from reflex_qrcode import QRCode

from reflex_tutorial.components.nodes import State
from reflex_tutorial.components.reactflow import react_flow, background, controls

#https://www.npmjs.com/package/reactflow
def index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading("Reflex ReactFlow Demo"),
            rx.vstack(
                react_flow(
                    background(),
                    controls(),
                    nodes_draggable=True,
                    nodes_connectable=True,
                    on_connect=lambda e0: State.on_connect(e0),
                    on_nodes_change=lambda e0: State.on_nodes_change(
                        e0
                    ),
                    nodes=State.nodes,
                    edges=State.edges,
                    fit_view=True,
                ),
                rx.hstack(
                    rx.button(
                        "Clear graph",
                        on_click=State.clear_graph,
                        width="100%",
                    ),
                    rx.button(
                        "Add node",
                        on_click=State.add_random_node,
                        width="100%",
                    ),
                    width="100%",
                ),
                height="30em",
                width="100%",
            )
        ),
    )


app = rx.App()
app.add_page(index)
