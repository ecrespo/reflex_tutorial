import reflex as rx


class AgCharts(rx.Component):
    """A simple line chart component using AG Charts"""

    library = "ag-charts-react"

    tag = "AgCharts"

    options: rx.Var[dict]


chart = AgCharts.create


class State(rx.State):
    """The app state."""

    chart_options: dict = {
        "data": [
            {
                "month": "Jan",
                "avgTemp": 2.3,
                "iceCreamSales": 162000,
            },
            {
                "month": "Mar",
                "avgTemp": 6.3,
                "iceCreamSales": 302000,
            },
            {
                "month": "May",
                "avgTemp": 16.2,
                "iceCreamSales": 800000,
            },
            {
                "month": "Jul",
                "avgTemp": 22.8,
                "iceCreamSales": 1254000,
            },
            {
                "month": "Sep",
                "avgTemp": 14.5,
                "iceCreamSales": 950000,
            },
            {
                "month": "Nov",
                "avgTemp": 8.9,
                "iceCreamSales": 200000,
            },
        ],
        "series": [
            {
                "type": "bar",
                "xKey": "month",
                "yKey": "iceCreamSales",
            }
        ],
    }


def index() -> rx.Component:
    return chart(
        options=State.chart_options,
    )


app = rx.App()
app.add_page(index)
