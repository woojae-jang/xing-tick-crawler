from multiprocessing.queues import Queue
import win32com.client
from config import RES_FOLDER_PATH
from xing_tick_crawler.event_handler import XARealEventHandler


class RealTimeAbs:
    def __init__(self, queue: Queue, res_code: str):
        xa_real = win32com.client.DispatchWithEvents("XA_DataSet.XAReal", XARealEventHandler)
        xa_real.queue = queue
        xa_real.ResFileName = f"{RES_FOLDER_PATH}/{res_code}.res"
        self.xa_real = xa_real

    def set_code_list(self, code_list: list, field="shcode"):
        for code in code_list:
            self.xa_real.SetFieldData("InBlock", field, code)
            self.xa_real.AdviseRealData()


class RealTimeKospiOrderBook(RealTimeAbs):
    """
    [H1_] KOSPI호가잔량
    """

    def __init__(self, queue: Queue):
        super().__init__(queue, "H1_")


class RealTimeKospiTick(RealTimeAbs):
    """
    [S3_] KOSPI체결
    """

    def __init__(self, queue: Queue):
        super().__init__(queue, "S3_")


class RealTimeKosdaqOrderBook(RealTimeAbs):
    """
    [HA_] KOSDAQ호가잔량
    """

    def __init__(self, queue: Queue):
        super().__init__(queue, "HA_")


class RealTimeKosdaqTick(RealTimeAbs):
    """
    [K3_] KOSDAQ체결
    """

    def __init__(self, queue: Queue):
        super().__init__(queue, "K3_")


class RealTimeStockFuturesOrderBook(RealTimeAbs):
    """
    [JH0] 주식선물호가
    """
    def __init__(self, queue: Queue):
        super().__init__(queue, "JH0")


class RealTimeStockFuturesTick(RealTimeAbs):
    """
    [JC0] 주식선물체결
    """
    def __init__(self, queue: Queue):
        super().__init__(queue, "JC0")
