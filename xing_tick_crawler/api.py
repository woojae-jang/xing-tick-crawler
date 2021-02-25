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
    def t1702(cls, code, start_date: str, end_date: str) -> pd.DataFrame:
        """
        t1702 외인/기관 종목별동향
        연속데이터 조회

        start_date: YYYYMMDD
        end_date: YYYYMMDD
        """
        stock_code = code
        t1702 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandler)
        t1702.ResFileName = f"{RES_FOLDER_PATH}/t1702.res"

        # 연속조회 여부
        next_data = False
        data = []
        is_last = False

        while True:
            t1702.SetFieldData('t1702InBlock', 'shcode', 0, stock_code)
            t1702.SetFieldData('t1702InBlock', 'todt', 0, end_date)
            t1702.SetFieldData('t1702InBlock', 'volvalgb', 0, '1')  # 0: 금액, 1: 수량, 2: 단가
            t1702.SetFieldData('t1702InBlock', 'msmdgb', 0, '0')  # 0: 순매수, 1: 매수, 2: 매도
            t1702.SetFieldData('t1702InBlock', 'cumulgb', 0, '0')  # 0:일간, 1: 누적
            if next_data is False:
                t1702.SetFieldData('t1702InBlock', 'cts_date', 0, '')
                t1702.SetFieldData('t1702InBlock', 'cts_idx', 0, '')
            else:
                t1702.SetFieldData('t1702InBlock', 'cts_date', 0, cts_date)
                t1702.SetFieldData('t1702InBlock', 'cts_idx', 0, cts_idx)

            if next_data:
                cls.request_api(t1702, 1)
            else:
                cls.request_api(t1702, 0)
            cls.wait_query(XAQueryEventHandler)

            cts_idx = t1702.GetFieldData("t1702OutBlock", "cts_idx", 0)
            cts_date = t1702.GetFieldData("t1702OutBlock", "cts_date", 0)
            next_data = True

            if cts_date < start_date:
                is_last = True

            count = t1702.GetBlockCount("t1702OutBlock1")
            if count == 0:
                break
            for i in range(count):
                date = t1702.GetFieldData("t1702OutBlock1", "date", i)
                amt0000 = t1702.GetFieldData("t1702OutBlock1", "amt0000", i)  # 사모펀드
                amt0001 = t1702.GetFieldData("t1702OutBlock1", "amt0001", i)  # 증권
                amt0002 = t1702.GetFieldData("t1702OutBlock1", "amt0002", i)  # 보험
                amt0003 = t1702.GetFieldData("t1702OutBlock1", "amt0003", i)  # 투신
                amt0004 = t1702.GetFieldData("t1702OutBlock1", "amt0004", i)  # 은행
                amt0005 = t1702.GetFieldData("t1702OutBlock1", "amt0005", i)  # 종금
                amt0006 = t1702.GetFieldData("t1702OutBlock1", "amt0006", i)  # 기금
                amt0007 = t1702.GetFieldData("t1702OutBlock1", "amt0007", i)  # 기타법인
                amt0008 = t1702.GetFieldData("t1702OutBlock1", "amt0008", i)  # 개인
                amt0009 = t1702.GetFieldData("t1702OutBlock1", "amt0009", i)  # 등록외국인
                amt0010 = t1702.GetFieldData("t1702OutBlock1", "amt0010", i)  # 미등록외국인
                amt0011 = t1702.GetFieldData("t1702OutBlock1", "amt0011", i)  # 국가외
                amt0018 = t1702.GetFieldData("t1702OutBlock1", "amt0018", i)  # 기관
                amt0088 = t1702.GetFieldData("t1702OutBlock1", "amt0088", i)  # 외인(등록외국인 + 미등록외국인)
                amt0099 = t1702.GetFieldData("t1702OutBlock1", "amt0099", i)  # 기타계(기타 + 국가)

                data.append([
                    date,
                    amt0000,
                    amt0001,
                    amt0002,
                    amt0003,
                    amt0004,
                    amt0005,
                    amt0006,
                    amt0007,
                    amt0008,
                    amt0009,
                    amt0010,
                    amt0011,
                    amt0018,
                    amt0088,
                    amt0099,
                ])
            if is_last:
                break

        df = pd.DataFrame(data, columns={
            "date": str,
            "사모펀드": str,
            "증권": str,
            "보험": str,
            "투신": str,
            "은행": str,
            "종금": str,
            "기금": str,
            "기타법인": str,
            "개인": str,
            "등록외국인": str,
            "미등록외국인": str,
            "국가외": str,
            "기관": str,
            "외인": str,
            "기타계": str,
        })
        df = df.sort_values('date', ascending=True)
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
