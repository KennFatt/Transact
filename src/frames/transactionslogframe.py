from .baseframe import BaseFrame
from tkinter import Label
from tkinter import Listbox
from tkinter import StringVar
from ..component.hoveredbutton import HoveredButton


class TransactionsLogFrame(BaseFrame):

    def __init__(self, controller, **kw):
        super().__init__(controller, "Transactions Log", **kw)

        # Log Listbox
        self.__log_listbox = None
        self.__logs_var = StringVar(
            self, value=list(self.controller.transactions.keys()))

        # Transaction details: ID
        self.__t_id = None
        self.__t_id_var = StringVar(self, value="Transaction ID\t: ")

        # Transaction details: Date
        self.__t_date = None
        self.__t_date_var = StringVar(self, value="Transaction Date\t: ")

        # Transaction details: Type
        self.__t_type = None
        self.__t_type_var = StringVar(self, value="Product Type\t: ")

        # Transaction details: Quantity
        self.__t_quantity = None
        self.__t_quantity_var = StringVar(self, value="Product Quantity\t: ")

        # Transaction details: Total Payment
        self.__t_payment = None
        self.__t_payment_var = StringVar(self, value="Total Payment\t: ")

        self.setup_widgets()

    def setup_widgets(self):
        # Log label
        log_label = Label(self, text="Transactions Log",
                          font=("Montserrat", 14, "bold"))

        # Log Listbox
        self.__log_listbox = Listbox(
            self, listvariable=self.__logs_var, bg="#fff")

        # Details label
        details_label = Label(self, text="Transaction Details",
                              font=("Montserrat", 14, "bold"))

        details_font = ("Montserrat", 14)
        # Details: ID
        self.__t_id = Label(self, textvariable=self.__t_id_var,
                            font=details_font)

        # Details: Date
        self.__t_date = Label(self, textvariable=self.__t_date_var,
                              font=details_font)

        # Details: Type
        self.__t_type = Label(self, textvariable=self.__t_type_var,
                              font=details_font)

        # Details: Quantity
        self.__t_quantity = Label(self, textvariable=self.__t_quantity_var,
                                  font=details_font)

        # Details: Total Payment
        self.__t_payment = Label(self, textvariable=self.__t_payment_var,
                                 font=details_font)

        # Back Button
        btn_back = HoveredButton(
            self, text="Back", fg="#fff", bg="#343837", activebackground="#1E2120",
            command=lambda: self.controller.switch_frame("mainmenu"),
            font=("Montserrat", 14, "bold"))

        #
        # ~ Place each widgets into its position
        #

        # Log label
        log_label.place(x=15, y=20)

        # Log Listbox
        self.__log_listbox.bind("<<ListboxSelect>>", self.on_item_selected)
        self.__log_listbox.place(
            anchor="n", width=450, height=185, x=240, y=50)

        # Details label
        details_label.place(x=15, y=255)
        # Details: ID
        self.__t_id.place(x=15, y=285)
        # Details: Date
        self.__t_date.place(x=15, y=315)
        # Details: Type
        self.__t_type.place(x=15, y=345)
        # Details: Date
        self.__t_quantity.place(x=15, y=375)
        # Details: Total Payment
        self.__t_payment.place(x=15, y=405)

        # Back Button
        btn_back.place(anchor="n", width=450, height=50, x=240, y=570)

    def on_item_selected(self, *args):
        # Prevent an error occured when list is empty
        if len(self.controller.transactions) == 0:
            return

        tid = list(self.controller.transactions.keys())[
            self.__log_listbox.curselection()[0]]

        date = self.controller.transactions[tid]["date"]
        type = self.controller.transactions[tid]["type"]
        quantity = self.controller.transactions[tid]["quantity"]
        total = self.controller.transactions[tid]["total"]

        self.__t_id_var.set(f"Transaction ID\t: {tid}")
        self.__t_date_var.set(f"Transaction Date\t: {date}")
        self.__t_type_var.set(f"Product Type\t: {type}")
        self.__t_quantity_var.set(f"Product Quantity\t: {quantity}")
        self.__t_payment_var.set(f"Total Payment\t: IDR {total}")
        pass
