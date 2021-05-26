"""
주식시장 구독 옵션(기본값 All True)
    - STOCK_VI_ON_OFF
    - KOSPI_ORDER_BOOK
    - KOSPI_TICK
    - KOSDAQ_ORDER_BOOK
    - KOSDAQ_TICK
    - KOSPI_AFTER_MARKET_ORDER_BOOK
    - KOSPI_AFTER_MARKET_TICK
    - KOSDAQ_AFTER_MARKET_ORDER_BOOK
    - KOSDAQ_AFTER_MARKET_TICK
    - STOCK_VI_ON_OFF
    - KOSPI_BROKER_INFO
    - KOSDAQ_BROKER_INFO

선물옵션시장 구독 옵션(기본값 All True)
    - STOCK_FUTURES_ORDER_BOOK
    - STOCK_FUTURES_TICK
"""

from xing_tick_crawler.crawler import stock_market_crawler, futures_option_market_crawler
from datetime import datetime
from multiprocessing import Process, get_context
from multiprocessing.queues import Queue

if __name__ == "__main__":
    stock_market_subs_option = {
        # 주식 VI 정보 off
        'STOCK_VI_ON_OFF': False,
    }
    futures_option_market_subs_option = {
        
    }

    queue = Queue(ctx=get_context())
    p0 = Process(target=stock_market_crawler, args=(queue,), kwargs=stock_market_subs_option)
    p1 = Process(target=futures_option_market_crawler, args=(queue,), kwargs=futures_option_market_subs_option)

    p0.start()
    p1.start()

    while True:
        tick = queue.get()
        waiting_tasks = queue.qsize()
        tick_type, tick_data = tick
        print(f"\r{datetime.now()} waiting tasks : {'%6d' % waiting_tasks}", end='')
        print(tick_type, tick_data)
