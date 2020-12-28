from xing_tick_crawler.crawler import stock_crawler, stock_futures_crawler
from datetime import datetime
from multiprocessing import Process, get_context
from multiprocessing.queues import Queue
from xing_tick_crawler import tick_writer

if __name__ == "__main__":
    KOSPI_ORDER_BOOK = True               # 코스피 전종목 호가
    KOSPI_TICK = True                     # 코스피 전종목 체결
    KOSDAQ_ORDER_BOOK = True              # 코스닥 전종목 호가
    KOSDAQ_TICK = True                    # 코스닥 전종목 체결
    STOCK_FUTURES_ORDER_BOOK = True       # 주식선물 전종목 호가
    STOCK_FUTURES_TICK = True             # 주식선물 전종목 체결

    queue = Queue(ctx=get_context())
    p0 = Process(target=stock_crawler, args=(queue, KOSPI_ORDER_BOOK, KOSPI_TICK, KOSDAQ_ORDER_BOOK, KOSDAQ_TICK))
    p1 = Process(target=stock_futures_crawler, args=(queue, STOCK_FUTURES_ORDER_BOOK, STOCK_FUTURES_TICK))

    p0.start()
    p1.start()

    try:
        while True:
            waiting_tasks = queue.qsize()
            tick = queue.get()
            tick_type, tick_data = tick
            print(f"\r{datetime.now()} waiting tasks : {waiting_tasks}", end='')

            tick_writer.handle_tick_data(tick_data, tick_type)

    except KeyboardInterrupt:
        tick_writer.close_all_writer()
        print("사용자 종료")
