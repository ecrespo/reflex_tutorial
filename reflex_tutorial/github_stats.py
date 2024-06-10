import reflex as rx
import requests
from bs4 import BeautifulSoup


options = [
    "Rust", "Python", "Javascript", "Go","C++"
]


class StateTrendingLanguage(rx.State):
    lang: str = ""
    url: str = f"https://www.github.com/trending/{lang}"
    repositories: list[list[str]] = []

    def set_language(self, lang: str):
        self.lang = lang

    def search_repo(self):
        if self.lang != "":
            self.repositories = []
            url = f"{self.url}{self.lang.lower()}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            repositories = soup.find_all("article", class_="Box-row")
            for repo in repositories[:5]:
                span_elements = repo.find("span", class_="text-normal")
                title_1 = span_elements.text.strip().replace(" ", "")
                title_2 = span_elements.next_sibling.text.strip().replace(" ", "")
                name = title_1 + title_2
                result = repo.find("p", class_="col-9 color-fg-muted my-1 pr-4")
                subtitle = result.text.strip() if result is not None else "No description provided"
                stars_element = repo.find("a", href=lambda href: href and "/stargazers" in href)
                stars_count = stars_element.text.strip()
                forks_element = repo.find("a", href=lambda href: href and "/forks" in href)
                forks_count = forks_element.text.strip()
                self.repositories.append([
                    name,
                    subtitle,
                    stars_count,
                    forks_count
                ])


def create_repo_details(data: list[list[str]]) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.container(
                rx.image(
                    src="https://img.icons8.com/material-rounded/384/github.png",
                    width="28px",
                    height="auto",
                ),
                padding="0",
                display="flex"
            )
        ),
        rx.vstack(
            rx.container(
                rx.tooltip(
                    rx.text(data[0],color="black", align="left"),
                    content=data[1],
                    gutter=50
                ),
                padding="0"
            ),
        ),
        rx.container(
            rx.hstack(
                rx.image(
                    src="https://img.icons8.com/ios-filled/100/star--v1.png",
                    width="12px",
                    height="auto",
                ),
                rx.text(data[2], color="black", align="left"),
                rx.image(
                    src="https://img.icons8.com/ios-filled/100/wishbone.png",
                    width="12px",
                    height="auto",
                ),
                rx.text(data[3], color="black",  align="left"),
                padding="0"
            ),
        ),
        box_shadow="lg",
        padding="12px",
        border_radius="6px",
        bg="white"
    )


@rx.page("/github_stats", title="Github Stats", description="Github Stats")
def github_stats() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.heading("Find trending Repositories", size="9", font_weight="bold", color="black"),
            rx.spacer(),
            rx.spacer(),
            rx.radio(
                options,
                direction="row",
                spacing="8",
                size="3",
                color="black",
                font_weight="bold",
                on_change=StateTrendingLanguage.set_language,
            ),
            rx.spacer(),
            rx.spacer(),
            rx.button(
                "Search",
                widh="230px",
                height="45px",
                color_scheme="blue",
                on_click=lambda: StateTrendingLanguage.search_repo,
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.hstack(
                rx.foreach(
                    StateTrendingLanguage.repositories,
                    create_repo_details,
                ),
                spacing="2"
            ),
            align_items="center",
            justify_content="center",
            display="flex",
        ),
        width="100%",
        height="100vh",
        bg="lightblue",
        display="flex",
        align_items="center",
        justify_content="center"
    )
