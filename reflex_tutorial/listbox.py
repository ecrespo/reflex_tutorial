import reflex as rx
import ollama

class FormSelectState1(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    @rx.var
    def get_data(self) -> str:
        return self.form_data.get("select", "")


items = [item["model"] for item in ollama.list()["models"]]


@rx.page("/listbox", title="Listbox",description="Listbox")
def listbox() -> rx.Component:
    return rx.vstack(
        rx.form.root(
            rx.vstack(
                rx.select(
                    items,
                    default_value="apple",
                    name="select",
                ),
                rx.button("Submit", type="submit"),
                width="100%",
            ),
            on_submit=FormSelectState1.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rx.divider(width="100%"),
        rx.heading("Results"),
        rx.text(FormSelectState1.form_data.to_string()),
        rx.divider(width="100%"),
        rx.text(FormSelectState1.get_data),
        width="100%",
    )