from datetime import datetime
import pythoncom
from multiprocessing.queues import Queue
from config import TICKER_DATA_FOLDER_PATH
from xing_tick_crawler.api import XingAPI
from xing_tick_crawler.real_time import (
    RealTimeKospiOrderBook,
    RealTimeKospiTick,
    RealTimeKosdaqOrderBook,
    RealTimeKosdaqTick,
    RealTimeStockFuturesOrderBook,
    RealTimeStockFuturesTick
)
from xing_tick_crawler import utils

utils.make_dir(TICKER_DATA_FOLDER_PATH)
TODAY = datetime.today().strftime("%Y-%m-%d")
TODAY_PATH = f"{TICKER_DATA_FOLDER_PATH}/{TODAY}"
utils.make_dir(TODAY_PATH)


def stock_crawler(queue: Queue,
                  kospi_order_book=True,
                  kospi_tick=True,
                  kosdaq_order_book=True,
                  kosdaq_tick=True,
                  ):
    _ = XingAPI.login(is_real_server=True)

    # ################################# 코스피 ###################################################################
    listed_code_df = XingAPI.get_listed_code_list(market_type=1)
    listed_code_df.to_csv(f"{TODAY_PATH}/kospi_listed_code.csv", encoding='utf-8-sig')

    code_list = listed_code_df['단축코드'].tolist()

    # 호가
    if kospi_order_book:
        real_time_kospi_order_book = RealTimeKospiOrderBook(queue=queue)
        real_time_kospi_order_book.set_code_list(code_list)

    # 체결
    if kospi_tick:
        real_time_kospi_conclusion = RealTimeKospiTick(queue=queue)
        real_time_kospi_conclusion.set_code_list(code_list)
    # ############################################################################################################

    # ################################# 코스닥 ###################################################################
    listed_code_df = XingAPI.get_listed_code_list(market_type=2)
    listed_code_df.to_csv(f"{TODAY_PATH}/kosdaq_listed_code.csv", encoding='utf-8-sig')

    code_list = listed_code_df['단축코드'].tolist()

    # 호가
    if kosdaq_order_book:
        real_time_kosdaq_order_book = RealTimeKosdaqOrderBook(queue=queue)
        real_time_kosdaq_order_book.set_code_list(code_list)

    # 체결
    if kosdaq_tick:
        real_time_kosdaq_conclusion = RealTimeKosdaqTick(queue=queue)
        real_time_kosdaq_conclusion.set_code_list(code_list)
    # ############################################################################################################

    while True:
        pythoncom.PumpWaitingMessages()


def stock_futures_crawler(queue: Queue,
                          stock_futures_order_book=True,
                          stock_futures_order_tick=True
                          ):
    _ = XingAPI.login(is_real_server=True)

    # ################################# 주식선물 ##################################################################
    listed_code_df = XingAPI.get_stock_futures_listed_code_list()
    listed_code_df.to_csv(f"{TODAY_PATH}/stock_futures_listed_code.csv", encoding='utf-8-sig')

    code_list = listed_code_df['단축코드'].tolist()

    # 호가
    if stock_futures_order_book:
        real_time_stock_futures_order_book = RealTimeStockFuturesOrderBook(queue=queue)
        real_time_stock_futures_order_book.set_code_list(code_list, field="futcode")

    # 체결
    if stock_futures_order_tick:
        real_time_stock_futures_conclusion = RealTimeStockFuturesTick(queue=queue)
        real_time_stock_futures_conclusion.set_code_list(code_list, field="futcode")
    # ############################################################################################################

    while True:
        pythoncom.PumpWaitingMessages()
