import reflex as rx
from rxconfig import config

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def get_button(button_text, img_src, href_url) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.image(
                src=img_src,
                width="30px"
            ),

            rx.text(button_text,
                    font_size="20px",
                    font_weight="500",
                    font_family="DM Sans",
                    text_align="center",
                    color='#57618A',
                    width="calc(100% - 80px)"

                    ),

            padding="9px 7px",
            width="95vw",
            max_width="700px",
            border="1px solid rgb(128, 160, 201)",
            border_radius="5px",
            bg='white',

            box_shadow="rgb(128 160 201) 8px 8px 0px 0px",

            _hover={
                "cursor": "pointer",
                "translate": "4px 4px",
                "box_shadow": "rgb(128 160 201) 4px 4px 0px 0px"
            },

        ),

        href=href_url,
        _hover={}
    )


def get_social_media_button(image_path, href_url) -> rx.Component:
    return rx.link(
                rx.image(
                        src=image_path,
                        width='60px',
                        _hover={
                                    "cursor": "pointer",
                                    "transform": "scale(1.1)",
                                },
                    ),
                    href=href_url
            )


@rx.page("/linktree",title="Linktree", description="Linktree")
def linktree() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.vstack(
                    rx.image(
                        src="/profile_pic.jpg",
                        width="168px",
                        height="168px",
                        border_radius="50%",
                        margin_bottom="8px"
                    ),
                    rx.text(
                        font_weight="700",
                        font_size="36px",
                        line_height='1.5em',
                        font_family="DM Sans",
                        text_align="center",
                        width="100%",
                        color="rgb(255, 255, 255)",
                        padding_bottom='3px'
                    ),
                    rx.text(
                        "Community focused artist, with a taste for everything local",
                        font_weight="500",
                        font_size="18px",
                        font_family="DM Sans",
                        text_align="center",
                        width="100%",
                        color="rgb(255, 255, 255)",
                        padding_bottom='30px'
                    ),
                    spacing="0",
                ),
                rx.vstack(
                    get_button('Tour dates',
                               '/calendar.png',
                               "https://google.com"
                               ),

                    get_button('Our Discord',
                               '/discord.png',
                               "https://google.com"),

                    get_button('Website',
                               '/link.png',
                               "https://google.com"),

                    get_button('Email',
                               '/email.png',
                               "https://google.com"),
                    rx.hstack(
                        get_social_media_button('/twitter_logo_white.png',
                                                'https://twitter.com/'
                                                ),

                        get_social_media_button('/instagram_logo_white.png',
                                                'https://instagram.com/'
                                                ),

                        get_social_media_button('/facebook_logo_white.png',
                                                'https://facebook.com/'
                                                ),

                        spacing="1",
                    ),
                    spacing="1",
                )
            ),
            padding_top="36px",
            width="100vw"
        ),
        bg="linear-gradient(160deg, rgba(103,151,193,255) , rgba(225,156,162,255))",
        width="100vw",
        height="100vh",
    )


