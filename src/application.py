import datetime
from tkinter import Tk
from tkinter import BOTH
from .frames import MainMenuFrame
from .frames import NewTransactionFrame
from .frames import TransactionsLogFrame


class Application(Tk):

    APPLICATION_NAME = "Transact"
    APPLICATION_VERSION_STRING = "1.0"

    def __init__(self):
        super().__init__()

        # Properties declaration
        self.__current_frame = None
        self.__registered_frames = {
            "mainmenu": MainMenuFrame,
            "newtransaction": NewTransactionFrame,
            "transactionslog": TransactionsLogFrame
        }
        self.products = {
            "topi": 40_000,
            "kaos": 100_000,
            "celana": 70_000,
            "sepatu": 65_000
        }
        self.transactions = {}

        # Setup window
        self.__setup_window()

        # Update frame
        self.switch_frame("mainmenu")

    def __setup_window(self):
        self.wm_title(f"{Application.APPLICATION_NAME}")
        self.wm_resizable(False, False)
        self.wm_minsize(480, 640)

    def switch_frame(self, frame_name):
        if frame_name not in self.__registered_frames:
            raise ValueError(
                f"Frame with name: \'{frame_name}\' is not found!")

        frame_class = self.__registered_frames[frame_name]
        new_frame = frame_class(self, bg="#EFF0F1")
        if self.__current_frame is not None:
            self.__current_frame.destroy()

        self.__current_frame = new_frame

        # Pack new frame to fill both X and Y axis
        # And allow its to expand all the free spaces on main window.
        self.__current_frame.pack(fill=BOTH, expand=True)

    def add_new_transaction(self, item_type, quantity):
        per_pcs = self.products[item_type]
        tid_int = len(self.transactions) + 1
        tid = f"#ID{tid_int}"
        date_t = datetime.datetime.now()

        self.transactions[tid] = {
            "date": f"{date_t.day}/{date_t.month}/{date_t.year}",
            "type": item_type,
            "quantity": quantity,
            "total": per_pcs * quantity
        }
