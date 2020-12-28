import time
from xing_tick_crawler.constant import (
    DataType,
    ORDER_BOOK_FIELDS,
    TICK_FIELDS,
    STOCK_FUTURES_ORDER_BOOK_FIELDS,
    STOCK_FUTURES_TICK_FIELDS,
)


class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")


class XAQueryEventHandler:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandler.query_state = 1


class XARealEventHandler:
    def __init__(self):
        self.queue = None

    def handle_order_book(self) -> list:
        """
        코스피, 코스닥 호가 데이터
        """
        values = []
        for field in ORDER_BOOK_FIELDS:
            values.append(self.GetFieldData("OutBlock", field))
        return values

    def handle_conclusion(self) -> list:
        """
        코스피, 코스닥 체결 데이터
        """
        values = []
        for field in TICK_FIELDS:
            values.append(self.GetFieldData("OutBlock", field))
        return values

    def handle_stock_futures_order_book(self) -> list:
        """
        주식선물 호가 데이터
        """
        values = []
        for field in STOCK_FUTURES_ORDER_BOOK_FIELDS:
            values.append(self.GetFieldData("OutBlock", field))
        return values

    def handle_stock_futures_conclusion(self) -> list:
        """
        주식선물 체결 데이터
        """
        values = []
        for field in STOCK_FUTURES_TICK_FIELDS:
            values.append(self.GetFieldData("OutBlock", field))
        return values

    def handle_h1(self) -> tuple:
        """
        H1_ : 코스피 호가
        """
        values = self.handle_order_book()
        values.insert(0, time.time())
        return DataType.KOSPI_ORDER_BOOK, values

    def handle_s3(self) -> tuple:
        """
        S3_ : 코스피 체결
        """
        values = self.handle_conclusion()
        values.insert(0, time.time())
        return DataType.KOSPI_TICK, values

    def handle_ha(self) -> tuple:
        """
        HA_ : 코스닥 호가
        """
        values = self.handle_order_book()
        values.insert(0, time.time())
        return DataType.KOSDAQ_ORDER_BOOK, values

    def handle_k3(self) -> tuple:
        """
        K3 : 코스닥 체결
        """
        values = self.handle_conclusion()
        values.insert(0, time.time())
        return DataType.KOSDAQ_TICK, values

    def handle_jh0(self) -> tuple:
        """
        JH0 : 주식선물 호가
        """
        values = self.handle_stock_futures_order_book()
        values.insert(0, time.time())
        return DataType.STOCK_FUTURES_ORDER_BOOK, values

    def handle_jc0(self) -> tuple:
        """
        JC0 : 주식선물 체결
        """
        values = self.handle_stock_futures_conclusion()
        values.insert(0, time.time())
        return DataType.STOCK_FUTURES_TICK, values

    def OnReceiveRealData(self, tr_code):
        if tr_code == "H1_":
            # 코스피 호가
            self.queue.put(self.handle_h1())
        elif tr_code == "S3_":
            # 코스피 체결
            self.queue.put(self.handle_s3())
        elif tr_code == "HA_":
            # 코스닥 호가
            self.queue.put(self.handle_ha())
        elif tr_code == "K3_":
            # 코스닥 체결
            self.queue.put(self.handle_k3())
        elif tr_code == "JH0":
            # 주식선물 호가
            self.queue.put(self.handle_jh0())
        elif tr_code == "JC0":
            # 주식선물 체결
            self.queue.put(self.handle_jc0())
        else:
            raise ValueError(f"Invalid TR code : {tr_code}")
