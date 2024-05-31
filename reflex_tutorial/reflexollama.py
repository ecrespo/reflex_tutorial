
import reflex as rx
from reflex_tutorial.components.OllamaChatReflex import chat, navbar


@rx.page(route="/reflex_ollama", title="Reflex Ollama IA", description="Reflex Ollama IA")
def reflexollama() -> rx.Component:
    """The main app."""
    return rx.chakra.vstack(
        navbar(),
        chat.chat(),
        chat.action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        min_height="100vh",
        align_items="stretch",
        spacing="0",
    )

