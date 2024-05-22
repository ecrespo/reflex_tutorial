import reflex as rx


class Gmaps(rx.Component):
    library = "react-gmaps"
    tag = "Gmaps"
    height = "800px"
    lat = 37.774929
    lng = -122.419416
    zoom = 8

gmaps = Gmaps.create