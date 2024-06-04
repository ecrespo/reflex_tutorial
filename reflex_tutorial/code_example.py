import reflex as rx





@rx.page("/code_example", title="Code Example",description="This is a code example page.")
def code_example() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.heading("Code Example", size="2"),
        rx.code_block(
            """def fib(n):
            if n <= 1:
                return n
            else:
                return(fib(n-1) + fib(n-2))""",
            language="python",
            show_line_numbers=True,
        )
    )