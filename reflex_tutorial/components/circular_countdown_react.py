import reflex as rx

class Countdown(rx.Component):
    library = "circular-countdown-react@1.1.4"
    tag = "Countdown"

    size: rx.Var[str]
    total_seconds: rx.Var[int]
    should_stop: rx.Var[bool]
    on_done: rx.EventHandler


countdown = Countdown.create




