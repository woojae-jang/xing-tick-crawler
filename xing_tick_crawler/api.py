import win32com.client
import pythoncom
from xing_tick_crawler.event_handler import *
from config import config
import pandas as pd
from config import RES_FOLDER_PATH


class XingAPI:
    __id = config["id"]
    __password = config["password"]
    __cert_passwd = config["cert_password"]
    recent_request = time.time()
    __MIN_INTERVAL = 3

    @classmethod
    def login(cls, is_real_server=True):
        xa_session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)
        if is_real_server:
            url = "hts.ebestsec.co.kr"  # 싫전
        else:
            url = "demo.ebestsec.co.kr"  # 모의
        xa_session.ConnectServer(url, 20001)
        xa_session.Login(XingAPI.__id, XingAPI.__password, XingAPI.__cert_passwd, 0, 0)

        while XASessionEventHandler.login_state == 0:
            pythoncom.PumpWaitingMessages()
        XASessionEventHandler.login_state = 0
        return xa_session

    @classmethod
    def request_api(cls, req_func, req_type):
        """
        api request 10분당 200건 제한 (3초당 1건)
        :return:
        """
        recent_request = cls.recent_request
        min_interval = cls.__MIN_INTERVAL
        now = time.time()
        interval = now - recent_request
        if min_interval > interval:
            time.sleep(min_interval - interval)
        req_func.Request(req_type)
        cls.recent_request = time.time()

    @classmethod
    def get_listed_code_list(cls, market_type: int) -> pd.DataFrame:
        """
        [t8436] 주식종목조회 API용
        :param market_type: int, 시장구분
                            전체:0, 코스피:1, 코스닥:2
        :return:
        """
        t8436 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandler)
        t8436.ResFileName = f"{RES_FOLDER_PATH}/t8436.res"

        assert market_type in [0, 1, 2]

        args = {
            "gubun": market_type,  # 시장구분
        }

        for key, value in args.items():
            t8436.SetFieldData('t8436InBlock', key, 0, value)
        cls.request_api(t8436, 0)
        cls.wait_query(XAQueryEventHandler)

        count = t8436.GetBlockCount("t8436OutBlock")

        col_list = [
            "hname",
            "shcode",
            "expcode",
            "etfgubun",
            "uplmtprice",
            "dnlmtprice",
            "jnilclose",
            "memedan",
            "recprice",
            "gubun",
            "bu12gubun",
            "spac_gubun",
            "filler",
        ]

        data_list = []
        for i in range(count):
            values = []
            for col in col_list:
                value = t8436.GetFieldData("t8436OutBlock", col, i)
                values.append(value)
            data_list.append(values)

        df = pd.DataFrame(data_list, columns={
            "종목명": str,
            "단축코드": str,
            "확장코드": str,
            "ETF구분(1:ETF|2:ETN)": str,
            "상한가": int,
            "하한가": int,
            "전일가": int,
            "주문수량단위": str,
            "기준가": int,
            "구분(1:코스피|2:코스닥)": str,
            "증권그룹": str,
            "기업인수목적회사여부": str,
            "filler(미사용)": str,
        })

        return df

    @classmethod
    def get_stock_futures_listed_code_list(cls) -> pd.DataFrame:
        """
        [t8401] 주식선물 마스터조회
        """
        t8401 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandler)
        t8401.ResFileName = f"{RES_FOLDER_PATH}/t8401.res"

        args = {
            "dummy": "1",  # Dummy
        }

        for key, value in args.items():
            t8401.SetFieldData('t8401InBlock', key, 0, value)

        cls.request_api(t8401, 0)
        cls.wait_query(XAQueryEventHandler)

        count = t8401.GetBlockCount("t8401OutBlock")

        col_list = [
            "hname",
            "shcode",
            "expcode",
            "basecode",
        ]

        data_list = []
        for i in range(count):
            values = []
            for col in col_list:
                value = t8401.GetFieldData("t8401OutBlock", col, i)
                values.append(value)
            data_list.append(values)

        df = pd.DataFrame(data_list, columns={
            "종목명": str,
            "단축코드": str,
            "확장코드": str,
            "기초자산코드": str,
        })

        return df

    @classmethod
    def wait_query(cls, target_class):
        while target_class.query_state == 0:
            pythoncom.PumpWaitingMessages()
        # 데이터를 얻은 후, 0으로 세팅
        target_class.query_state = 0
