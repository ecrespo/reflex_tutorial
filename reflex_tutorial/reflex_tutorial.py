import reflex as rx
from reflex_qrcode import QRCode



def index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading("Reflex QRCode Demo"),
            QRCode(
                title="Esta es una prueba de generación de código QR",
                value="Prueba",
                level="H",
                size=256
            )
        ),
    )


app = rx.App()
app.add_page(index)
