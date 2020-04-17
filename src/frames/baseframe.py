from abc import ABCMeta, abstractmethod
from tkinter.ttk import Frame


class BaseFrame(Frame, metaclass=ABCMeta):

    def __init__(self, controller, title, **kw):
        super().__init__(master=controller, **kw)
        controller.wm_title(f"{controller.APPLICATION_NAME} - {title}")
        self.__controller = controller

    @property
    def controller(self):
        return self.__controller

    @abstractmethod
    def setup_widgets(self):
        pass
