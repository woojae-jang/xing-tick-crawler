import csv
from typing import Tuple
from xing_tick_crawler.crawler import TODAY_PATH
from xing_tick_crawler import utils
from xing_tick_crawler.constant import (
    DataType,
    ORDER_BOOK_COLUMNS,
    CONCLUSION_COLUMNS,
    STOCK_FUTURES_ORDER_BOOK_COLUMNS,
    STOCK_FUTURES_CONCLUSION_COLUMNS
)
import io

CSV_HANDLER_STORE = dict()


def get_csv_writer(code: str, tick_type: DataType) -> Tuple[io.TextIOWrapper, csv.writer]:
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

        if tick_type in [DataType.KOSPI_ORDER_BOOK, DataType.KOSDAQ_ORDER_BOOK]:
            if not is_exist:
                writer.writerow(CONCLUSION_COLUMNS)
        elif tick_type in [DataType.KOSPI_TICK, DataType.KOSDAQ_TICK]:
            if not is_exist:
                writer.writerow(ORDER_BOOK_COLUMNS)
        elif tick_type == DataType.STOCK_FUTURES_ORDER_BOOK:
            if not is_exist:
                writer.writerow(STOCK_FUTURES_ORDER_BOOK_COLUMNS)
        elif tick_type == DataType.STOCK_FUTURES_TICK:
            if not is_exist:
                writer.writerow(STOCK_FUTURES_CONCLUSION_COLUMNS)

        csv_handler = (f, writer)
        CSV_HANDLER_STORE[handler_id] = csv_handler
    return csv_handler


def create_csv_writer(code_list: str, tick_type: DataType):
    for code in code_list:
        get_csv_writer(code, tick_type)


def handle_tick_data(tick_data: list, tick_type: DataType):
    """
    tick_data : [system_time, code, ...]
    """
    code = tick_data[1]
    f, writer = get_csv_writer(code, tick_type)
    writer.writerow(tick_data)
    f.flush()


def close_all_writer():
    global CSV_HANDLER_STORE

    handler_id_list = CSV_HANDLER_STORE.keys()

    for handler_id in handler_id_list:
        handler = CSV_HANDLER_STORE.pop(handler_id)
        f, writer = handler
        f.close()
