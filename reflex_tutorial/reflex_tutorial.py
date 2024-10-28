import reflex as rx


from reflex_tutorial.components.react_chrono import chrono


# https://www.youtube.com/watch?v=UygBVsDLeWI&ab_channel=emmakodes
# https://www.npmjs.com/package/circular-countdown-react?activeTab=readme


items = [
    {
      "title": "May 1940",
      "cardTitle": "Dunkirk",
      "url": "http://www.history.com",
      "cardSubtitle":"Men of the British Expeditionary Force (BEF) wade out to..",
      "cardDetailedText": "Men of the British Expeditionary Force (BEF) wade out to..",
      "media": {
        "type": "IMAGE",
        "source": {
          "url": "http://someurl/image.jpg"
        }
      }
    }
]


def index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading("Reflex timeline Demo"),
            chrono(items=items),
        ),
    )


app = rx.App()
app.add_page(index)
