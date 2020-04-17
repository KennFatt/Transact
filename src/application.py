from tkinter import Tk
from .frames.mainmenuframe import MainMenuFrame


class Application(Tk):

    APPLICATION_NAME = "Transact"
    APPLICATION_VERSION_STRING = "1.0"

    def __init__(self):
        super().__init__()

        # Properties declaration
        self.__current_frame = None

        # Setup window
        self.__setup_window()

        # Update frame
        self._switch_frame(MainMenuFrame)

    def __setup_window(self):
        self.wm_title(f"{Application.APPLICATION_NAME}")
        self.wm_resizable(False, False)
        self.wm_minsize(480, 640)

    def _switch_frame(self, frame_class, **kw):
        new_frame = frame_class(self, **kw)
        if self.__current_frame is not None:
            self.__current_frame.destroy()

        self.__current_frame = new_frame
        self.__current_frame.pack()
