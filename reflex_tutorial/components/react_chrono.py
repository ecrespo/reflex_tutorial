import reflex as rx
from typing import Any, Dict, List, Union




class ReactChrono(rx.Component):
    library = "react-chrono@2.6.1"






class Chrono(ReactChrono):
    tag = "Chrono"

    active_item_index:  rx.Var[int] = 0
    allow_dynamic_update: rx.Var[bool] = False
    border_less_cards: rx.Var[bool] = False
    card_less: rx.Var[bool] = False
    card_position_horizontal: rx.Var[str] = "TOP"
    card_width:  rx.Var[int]
    content_details_height: rx.Var[int] = 150
    disable_auto_scroll_on_click: rx.Var[bool] = False
    disable_click_on_circle: rx.Var[bool] = False
    disable_interaction: rx.Var[bool] = False
    disable_nav_on_key: rx.Var[bool] = False
    disable_timeline_point: rx.Var[bool] = False
    enable_break_point: rx.Var[bool] = False
    enable_dark_toggle: rx.Var[bool] = False
    enable_layout_switch: rx.Var[bool] = True
    enable_quick_jump: rx.Var[bool] = True
    flipLayout: rx.Var[bool] = False
    focus_active_item_on_load: rx.Var[bool] = False
    highlightCardsOnHover: rx.Var[bool] = False
    items: rx.Var[List[Dict[str, Any]]] = []
    item_width: rx.Var[int] = 300
    line_width: rx.Var[str] = "3px"
    media_height: rx.Var[int] = 200
    media_settings: rx.Var[Dict[str, Any]] = {}
    mode: rx.Var[str] = "HORIZONTAL"
    nested_card_height: rx.Var[int] = 150
    no_unique_id: rx.Var[bool] = False
    parse_details_as_html: rx.Var[bool] = False
    responsive_break_point: rx.Var[int] = 1024
    scrollable:  rx.Var[bool] = True
    slide_item_duration: rx.Var[int] = 5000
    slide_show: rx.Var[bool] = False
    text_density: rx.Var[str] = "HIGH"
    text_overlay:  rx.Var[bool] = False
    theme:  rx.Var[Dict[str, Any]] = {}
    timeline_point_shape:  rx.Var[str] = "circle"
    title_date_format: rx.Var[str] = "MM DD, YYYY"
    toolbar_position:  rx.Var[str] = "TOP"
    use_read_more:  rx.Var[bool] = True
    disable_toolbar:  rx.Var[bool] = False

chrono = Chrono.create