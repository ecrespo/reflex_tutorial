import reflex as rx
import enum


class EditorButtonList(list, enum.Enum):
    BASIC = [
        ["font", "fontSize"],
        ["fontColor"],
        ["horizontalRule"],
        ["link", "image"],
    ]
    FORMATTING = [
        ["undo", "redo"],
        [
            "bold",
            "underline",
            "italic",
            "strike",
            "subscript",
            "superscript",
        ],
        ["removeFormat"],
        ["outdent", "indent"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
    ]
    COMPLEX = [
        ["undo", "redo"],
        ["font", "fontSize", "formatBlock"],
        [
            "bold",
            "underline",
            "italic",
            "strike",
            "subscript",
            "superscript",
        ],
        ["removeFormat"],
        "/",
        ["fontColor", "hiliteColor"],
        ["outdent", "indent"],
        ["align", "horizontalRule", "list", "table"],
        ["link", "image", "video"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
        ["save", "template"],
    ]


class EditorState(rx.State):
    content: str = "<p>Editor content</p>"

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

@rx.page("/editor", title="Editor", description="Editor")
def editor_file()-> rx.Component:
    return rx.vstack(
        rx.editor(
            lang="es",
            set_contents=EditorState.content,
            set_options=rx.EditorOptions(
            button_list=[
                ["save", "template"],
                ["font", "fontSize", "formatBlock"],
                ["fontColor", "hiliteColor"],
                [
                    "bold",
                    "underline",
                    "italic",
                    "strike",
                    "subscript",
                    "superscript",
                ],
                ["removeFormat"],
                "/",
                ["outdent", "indent"],
                ["align", "horizontalRule", "list", "table"],
                ["link"],
                ["fullScreen", "showBlocks", "codeView"],
                ["preview", "print"],
            ]
            ),
        on_change=EditorState.handle_change,
        ),
        rx.box(
            rx.html(EditorState.content),
            border="1px dashed #ccc",
            border_radius="4px",
            width="100%",
        ),
    )