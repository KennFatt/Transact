from tkinter import Label
from .baseframe import BaseFrame
from ..component.hoveredbutton import HoveredButton


class MainMenuFrame(BaseFrame):

    def __init__(self, controller, **kw):
        super().__init__(controller, "Main Menu", **kw)
        self.setup_widgets()

    def setup_widgets(self):
        greet = Label(self, text="Welcome Back!",
                      font=("Montserrat", 22, "bold"), bg=self["background"])

        # Setup default properties for each HoveredButton widget
        # bg -> default background
        # activebackground -> When button hovered
        btn_props = {
            "fg": "#fff",
            "bg": "#000",
            "activebackground": "#111",
            "command": lambda: print("Button clicked!"),
            "font": ("Montserrat", 14, "bold")
        }

        btn_props["bg"] = "#03719C"
        btn_props["activebackground"] = "#005D82"
        btn_props["command"] = lambda: self.controller.switch_frame(
            "newtransaction")
        btn_newt = HoveredButton(self, text="New Transaction", **btn_props)

        btn_props["bg"] = "#0F9B8E"
        btn_props["activebackground"] = "#0A7C72"
        btn_props["command"] = lambda: self.controller.switch_frame(
            "transactionslog")
        btn_tlog = HoveredButton(
            self, text="Transactions Log", **btn_props)

        btn_props["bg"] = "#343837"
        btn_props["activebackground"] = "#1E2120"
        btn_props["command"] = lambda: self.controller.destroy()
        btn_exit = HoveredButton(
            self, text="Exit", **btn_props)

        version = Label(
            self, text=f"{self.controller.APPLICATION_NAME} v{self.controller.APPLICATION_VERSION_STRING}", font=("Montserrat", 12),
            bg=self["background"])

        # Default properties for position placement
        props = {
            "anchor": "n",
            "width": 200,
            "height": 60,
            "x": 240,
            "y": 0
        }

        props["y"] = props["y"] + 50
        greet.place(anchor=props["anchor"], x=props["x"], y=props["y"])

        props["y"] = props["y"] + props["height"] + 200
        btn_newt.place(**props)

        props["y"] = props["y"] + props["height"] + 25
        btn_tlog.place(**props)

        props["y"] = props["y"] + props["height"] + 25
        btn_exit.place(**props)

        version.pack(side="bottom")
