import reflex as rx


class MapContainer(rx.NoSSRComponent):
    library = "react-leaflet"

    tag = "MapContainer"

    center: rx.Var[list]

    zoom: rx.Var[int]

    scroll_wheel_zoom: rx.Var[bool]

    # Can also pass a url like: https://unpkg.com/leaflet/dist/leaflet.css
    def add_imports(self):
        return {"": ["leaflet/dist/leaflet.css"]}


class TileLayer(rx.NoSSRComponent):
    library = "react-leaflet"

    tag = "TileLayer"

    url: rx.Var[str]


map_container = MapContainer.create
tile_layer = TileLayer.create


def index() -> rx.Component:
    return map_container(
        tile_layer(
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        ),
        # 10.184236, -68.004010
        center=[10.184236, -68.004010],
        zoom=13,
        # scroll_wheel_zoom=True
        width="100%",
        height="50vh",
    )


app = rx.App()
app.add_page(index)
