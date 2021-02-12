import csv
from typing import Tuple
from xing_tick_crawler.crawler import TODAY_PATH
from xing_tick_crawler import utils
from xing_tick_crawler.constant import (
    DataType,
    ORDER_BOOK_COLUMNS,
    TICK_COLUMNS,
    STOCK_FUTURES_ORDER_BOOK_COLUMNS,
    STOCK_FUTURES_TICK_COLUMNS,
)
import io
import win32file
from main import BUNDLE_BY_MARKET

if not BUNDLE_BY_MARKET:
    win32file._setmaxstdio(1024 * 8)

CSV_HANDLER_STORE = dict()


def get_csv_writer(code: str, tick_type: DataType, bundle_by_market=True) -> Tuple[io.TextIOWrapper, csv.writer]:
    """
    bundle_by_market: True, 시장별 파일
                      False, 종목별 파일
    """
    if bundle_by_market:
        return bundle_writer(tick_type)
    else:
        return single_code_writer(code, tick_type)


def single_code_writer(code: str, tick_type: DataType) -> Tuple[io.TextIOWrapper, csv.writer]:
    global CSV_HANDLER_STORE

    handler_id = f"{code}|{tick_type.name}"

    csv_handler = CSV_HANDLER_STORE.get(handler_id, None)
    if csv_handler is None:
        tick_type_folder = f'{TODAY_PATH}/{tick_type.name}'
        utils.make_dir(tick_type_folder)
        file_name = f'{tick_type_folder}/{code}.csv'
        is_exist = utils.is_exist(file_name)

        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)

        if not is_exist:
            write_header(tick_type, writer)

        csv_handler = (f, writer)
        CSV_HANDLER_STORE[handler_id] = csv_handler
    return csv_handler


def bundle_writer(tick_type: DataType) -> Tuple[io.TextIOWrapper, csv.writer]:
    handler_id = tick_type.name
    csv_handler = CSV_HANDLER_STORE.get(handler_id, None)
    if csv_handler is None:
        file_name = f'{TODAY_PATH}/{handler_id}.csv'
        is_exist = utils.is_exist(file_name)

        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)

        if not is_exist:
            write_header(tick_type, writer)

        csv_handler = (f, writer)
        CSV_HANDLER_STORE[handler_id] = csv_handler
    return csv_handler


def write_header(tick_type: DataType, writer: csv.writer) -> None:
    if tick_type in [DataType.KOSPI_ORDER_BOOK, DataType.KOSDAQ_ORDER_BOOK]:
        writer.writerow(ORDER_BOOK_COLUMNS)
    elif tick_type in [DataType.KOSPI_TICK, DataType.KOSDAQ_TICK]:
        writer.writerow(TICK_COLUMNS)
    elif tick_type == DataType.STOCK_FUTURES_ORDER_BOOK:
        writer.writerow(STOCK_FUTURES_ORDER_BOOK_COLUMNS)
    elif tick_type == DataType.STOCK_FUTURES_TICK:
        writer.writerow(STOCK_FUTURES_TICK_COLUMNS)



def create_csv_writer(code_list: str, tick_type: DataType) -> None:
    for code in code_list:
        get_csv_writer(code, tick_type)


def handle_tick_data(tick_data: list, tick_type: DataType) -> None:
    """
    tick_data : [system_time, code, ...]
    """
    code = tick_data[1]
    f, writer = get_csv_writer(code, tick_type, BUNDLE_BY_MARKET)
    writer.writerow(tick_data)
    f.flush()


def close_all_writer() -> None:
    global CSV_HANDLER_STORE

    handler_id_list = list(CSV_HANDLER_STORE.keys())

    for handler_id in handler_id_list:
        handler = CSV_HANDLER_STORE.pop(handler_id)
        f, writer = handler
        f.close()
