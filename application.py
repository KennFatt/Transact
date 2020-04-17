from tkinter import *
from tkinter.ttk import *


class Application(Tk):

    def __init__(self):
        super().__init__()

        self.__current_frame: Frame = None
        self._switch_frame(MainMenuFrame)
        WindowUtility.apply_settings(self)

    def _switch_frame(self, frame_class):
        new_frame: Frame = frame_class(self)
        if self.__current_frame is not None:
            self.__current_frame.destroy()

        self.__current_frame = new_frame
        self.__current_frame.pack()


class MainMenuFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master=master)


class WindowUtility:

    @staticmethod
    def apply_settings(tl: Toplevel, **settings):
        title = settings["title"] if "title" in settings else "Transact - Transaction Management"
        window_height = settings["height"] if "height" in settings else 640
        window_width = settings["width"] if "width" in settings else 480
        resizable = settings["resizable"] if "resizable" in settings else False

        tl.wm_title(title)
        tl.wm_minsize(window_width, window_height)
        tl.wm_resizable(1, 1) if resizable else tl.wm_resizable(0, 0)


if __name__ == "__main__":
    Application().mainloop()
