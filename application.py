from tkinter import *
from tkinter.ttk import *


class Application(Tk):

    def __init__(self):
        super().__init__()

        # Properties declaration
        self.__current_frame: Frame = None

        # Setup window
        self.__setup_window()

        # Setup styles
        self.__setup_styles()

        # Update frame
        self._switch_frame(MainMenuFrame)

    def __setup_window(self):
        self.wm_title("Transact")
        self.wm_resizable(0, 0)
        self.wm_minsize(480, 640)

    def __setup_styles(self):
        style = Style()

        # Style for greeting message in MainMenu
        style.configure("mainMenu-label-greet.TLabel",
                        foreground="#000", font=("Montserrat", 22, "bold"))

        # Style for mainMenu-button-newtransaction
        style.map("mainMenu-button-newTransaction.TButton",
                  background=[("pressed", "#005D82"), ("active", "#005D82")])
        style.configure(
            "mainMenu-button-newTransaction.TButton", foreground="#fff", background="#03719C", font=("Montserrat", 14, "bold"))

        style.map("mainMenu-button-transactionLog.TButton",
                  background=[("pressed", "#0A7C72"), ("active", "#0A7C72")])
        style.configure("mainMenu-button-transactionLog.TButton", foreground="#fff",
                        background="#0F9B8E", font=("Montserrat", 14, "bold"))

        style.map("mainMenu-button-exit.TButton",
                  background=[("pressed", "#1E2120"), ("active", "#1E2120")])
        style.configure("mainMenu-button-exit.TButton", foreground="#fff",
                        background="#343837", font=("Montserrat", 14, "bold"))

    def _switch_frame(self, frame_class):
        new_frame: Frame = frame_class(self)
        if self.__current_frame is not None:
            self.__current_frame.destroy()

        self.__current_frame = new_frame
        self.__current_frame.pack()


class MainMenuFrame(Frame):

    def __init__(self, controller: Application = None):
        super().__init__(master=controller)
        controller.wm_title("Transact - Main Menu")

        self.__controller: Application = controller

        self.__setup_widgets()

    def __setup_widgets(self):
        l_motd: Label = Label(self.__controller, text="Welcome Back!",
                              style="mainMenu-label-greet.TLabel")
        l_motd.place(anchor="n", x=240, y=50)

        btn_top = Button(self.__controller, text="New Transaction",
                         command=lambda: print("btn_top@clicked!"), style="mainMenu-button-newTransaction.TButton")
        btn_top.place(
            anchor="n", width=200, height=60, x=240, y=250)

        btn_mid = Button(self.__controller, text="Transaction Log",
                         command=lambda: print("btn_mid@clicked!"), style="mainMenu-button-transactionLog.TButton")
        btn_mid.place(
            anchor="n", width=200, height=60, x=240, y=335)

        btn_bot = Button(self.__controller, text="Exit",
                         command=lambda: print("btn_bot@clicked!"), style="mainMenu-button-exit.TButton")
        btn_bot.place(anchor="n", width=200, height=60, x=240, y=420)


if __name__ == "__main__":
    Application().mainloop()
