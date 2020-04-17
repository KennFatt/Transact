from .baseframe import BaseFrame


class NewTransactionFrame(BaseFrame):

    def __init__(self, controller, **kw):
        super().__init__(controller, "New Transaction", **kw)

    def setup_widgets(self):
        pass
