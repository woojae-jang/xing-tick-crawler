from xing_tick_crawler.crawler import stock_crawler, stock_futures_crawler
from datetime import datetime
from multiprocessing import Process, get_context
from multiprocessing.queues import Queue

if __name__ == "__main__":
    KOSPI_ORDER_BOOK = False               # 코스피 전종목 호가
    KOSPI_TICK = True                      # 코스피 전종목 체결
    KOSDAQ_ORDER_BOOK = False              # 코스닥 전종목 호가
    KOSDAQ_TICK = True                     # 코스닥 전종목 체결
    STOCK_FUTURES_ORDER_BOOK = False       # 주식선물 전종목 호가
    STOCK_FUTURES_TICK = True              # 주식선물 전종목 체결

    queue = Queue(ctx=get_context())
    p0 = Process(target=stock_crawler, args=(queue, KOSPI_ORDER_BOOK, KOSPI_TICK, KOSDAQ_ORDER_BOOK, KOSDAQ_TICK))
    p1 = Process(target=stock_futures_crawler, args=(queue, STOCK_FUTURES_ORDER_BOOK, STOCK_FUTURES_TICK))

    p0.start()
    p1.start()

    while True:
        tick = queue.get()
        waiting_tasks = queue.qsize()
        tick_type, tick_data = tick
        print(f"\r{datetime.now()} waiting tasks : {'%6d' % waiting_tasks}", end='')
        print(tick_type, tick_data)
