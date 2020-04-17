from tkinter.ttk import Frame
from tkinter.ttk import Style
from tkinter.ttk import Label
from tkinter.ttk import Button


class MainMenuFrame(Frame):

    def __init__(self, controller=None, **kw):
        super().__init__(master=controller, **kw)
        self.__controller = controller

        self.__update_title()
        self.__setup_styles()
        self.__setup_widgets()

    def __update_title(self):
        self.__controller.wm_title(
            f"{self.__controller.APPLICATION_NAME} - Main Menu")

    def __setup_styles(self):
        s = Style()

        s.configure("mm-greet.TLabel", foreground="#000",
                    font=("Montserrat", 22, "bold"))
        s.configure("mm-version.TLabel", foreground="#000",
                    font=("Montserrat", 12))

        s.map("mm-newt.TButton",
              background=[("pressed", "#005D82"), ("active", "#005D82")])
        s.configure("mm-newt.TButton", foreground="#fff",
                    background="#03719C", font=("Montserrat", 14, "bold"))

        s.map("mm-tlog.TButton",
              background=[("pressed", "#0A7C72"), ("active", "#0A7C72")])
        s.configure("mm-tlog.TButton", foreground="#fff",
                    background="#0F9B8E", font=("Montserrat", 14, "bold"))

        s.map("mm-exit.TButton",
              background=[("pressed", "#1E2120"), ("active", "#1E2120")])
        s.configure("mm-exit.TButton", foreground="#fff",
                    background="#343837", font=("Montserrat", 14, "bold"))

    def __setup_widgets(self):
        greet = Label(self.__controller, text="Welcome Back!",
                      style="mm-greet.TLabel")
        btn_newt = Button(self.__controller,
                          text="New Transaction", style="mm-newt.TButton", command=lambda: print("mm-newt@clicked!"))
        btn_tlog = Button(self.__controller, text="Transactions Log",
                          style="mm-tlog.TButton", command=lambda: print("mm-tlog@clicked!"))
        btn_exit = Button(self.__controller, text="Exit",
                          style="mm-exit.TButton", command=lambda: print("mm-exit@clicked!"))
        version = Label(
            self.__controller, text=f"{self.__controller.APPLICATION_NAME} v{self.__controller.APPLICATION_VERSION_STRING}")

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
