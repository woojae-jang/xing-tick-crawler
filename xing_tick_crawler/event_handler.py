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
            print(f"로그인 실패 {msg}")


class XAQueryEventHandler:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandler.query_state = 1


class XARealEventHandler:
    def __init__(self):
        self.queue = None

    def handle_event(self, field_list: list) -> dict:
        values = dict()
        for field in field_list:
            values[field] = self.GetFieldData("OutBlock", field)
        return values

    def OnReceiveRealData(self, tr_code):
        if tr_code == "H1_":
            # 코스피 호가
            tick_type = DataType.KOSPI_ORDER_BOOK
            field_list = ORDER_BOOK_FIELDS
        elif tr_code == "S3_":
            # 코스피 체결
            tick_type = DataType.KOSPI_TICK
            field_list = TICK_FIELDS
        elif tr_code == "HA_":
            # 코스닥 호가
            tick_type = DataType.KOSDAQ_ORDER_BOOK
            field_list = ORDER_BOOK_FIELDS
        elif tr_code == "K3_":
            # 코스닥 체결
            tick_type = DataType.KOSDAQ_TICK
            field_list = TICK_FIELDS
        elif tr_code == "JH0":
            # 주식선물 호가
            tick_type = DataType.STOCK_FUTURES_ORDER_BOOK
            field_list = STOCK_FUTURES_ORDER_BOOK_FIELDS
        elif tr_code == "JC0":
            # 주식선물 체결
            tick_type = DataType.STOCK_FUTURES_TICK
            field_list = STOCK_FUTURES_TICK_FIELDS
        else:
            raise ValueError(f"Invalid TR code : {tr_code}")

        values = self.handle_event(field_list=field_list)
        values['system_time'] = time.time()
        data = (tick_type, values)
        self.queue.put(data)
