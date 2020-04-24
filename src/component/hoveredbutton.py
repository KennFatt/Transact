from tkinter import Button


class HoveredButton(Button):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.__default_bg = self["background"]
        self.__default_fg = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, *args):
        self["activeforeground"] = self.__default_fg
        self["background"] = self["activebackground"]

    def on_leave(self, *args):
        self["background"] = self.__default_bg
