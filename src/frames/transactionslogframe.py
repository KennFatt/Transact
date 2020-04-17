from .baseframe import BaseFrame


class TransactionsLogFrame(BaseFrame):

    def __init__(self, controller, **kw):
        super().__init__(controller, "Transactions Log", **kw)

    def setup_widgets(self):
        pass
