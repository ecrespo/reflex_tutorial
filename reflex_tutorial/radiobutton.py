import reflex as rx

#https://reflex.dev/docs/library/forms/radio-group/


class FormRadioState_HL(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    @rx.var
    def get_data(self) -> str:
        return self.form_data.get("radio")


@rx.page("/radiobutton", title="Radio Button",description="This is a radio button page.")
def radiobutton() -> rx.Component:
    return rx.vstack(
        rx.form.root(
            rx.vstack(
                rx.radio(
                    ["1", "2", "3"],
                    name="radio",
                    required=True,
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=FormRadioState_HL.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(width="100%"),
        rx.heading("Results"),
        rx.text(FormRadioState_HL.form_data.to_string()),
        rx.divider(width="100%"),
        rx.text(FormRadioState_HL.get_data),
    )