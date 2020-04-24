from tkinter import Label
from tkinter import Entry
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from .baseframe import BaseFrame
from ..component.hoveredbutton import HoveredButton


class NewTransactionFrame(BaseFrame):

    def __init__(self, controller, **kw):
        super().__init__(controller, "New Transaction", **kw)

        # Item Type Combobox
        self.__it_combobox = None

        # Quantity Entry
        self.__q_entry = None

        self.setup_widgets()

    def setup_widgets(self):
        # New Label
        new_label = Label(self, text="New Transaction",
                          font=("Montserrat", 14, "bold"))

        # Item Type Label
        it_label = Label(self, text="Item Type\t\t: ", font=("Montserrat", 12))

        # Item Type Combobox
        Style().configure("m.TCombobox", background="#32BF84")
        self.__it_combobox = Combobox(
            self, state="readonly", values=list(self.controller.products.keys()),
            font=("Montserrat", 14), style="m.TCombobox")

        # Quantity Label
        q_label = Label(self, text="Quantity\t\t: ", font=("Montserrat", 12))

        # Quantity Entry
        self.__q_entry = Entry(self)

        # Confirm Button
        confirm_button = HoveredButton(
            self, text="Confirm", fg="#fff", bg="#32BF84", activebackground="#048243",
            command=self.on_confirm_button, font=("Montserrat", 14, "bold"))

        # Back Button
        btn_back = HoveredButton(
            self, text="Back", fg="#fff", bg="#343837", activebackground="#1E2120",
            command=lambda: self.controller.switch_frame("mainmenu"),
            font=("Montserrat", 14, "bold"))

        #
        # ~ Place each widgets into its position
        #

        # New Label
        new_label.place(x=15, y=20)

        # Item Type Label
        it_label.place(x=15, y=60)

        # Item Type Combobox
        self.__it_combobox.place(
            anchor="ne", width=250, height=35, x=465, y=60)

        # Quantity Label
        q_label.place(x=15, y=100)

        # Quantity Entry
        self.__q_entry.insert(0, 1)
        self.__q_entry.place(
            anchor="ne", width=250, height=35, x=465, y=100)

        # Confirm Button
        confirm_button.place(anchor="s", width=450, height=50, x=240, y=560)

        # Back Button
        btn_back.place(anchor="n", width=450, height=50, x=240, y=570)

    def on_confirm_button(self):
        # Type
        item_type: str = self.__it_combobox.get()
        if len(item_type) == 0:
            showinfo("Invalid Input", "Please select item type!")
            return

        # Quantity
        raw_q: str = self.__q_entry.get()
        if raw_q.isnumeric():
            q = int(raw_q)
        else:
            showinfo("Invalid Input", "Quantity value is invalid!")
            return

        if q == 0:
            showinfo("Invalid Input", "Quantity can't be zero!")
            return

        showinfo("Transaction Succeed", "New transaction has been added!")
        self.controller.add_new_transaction(item_type, q)
        self.controller.switch_frame("mainmenu")
