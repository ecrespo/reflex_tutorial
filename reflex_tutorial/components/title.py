import reflex as rx


BASE_FONT: int = 16


def render_title() -> rx.Component:
    return rx.heading("Supabase client",
                      font_size=[f"{BASE_FONT} * (1.2** {index})px" for index in range(5)],
                      size="9",
                      transition="all 500ms ease",
                      )
