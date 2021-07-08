# xing-tick-crawler
  - 반드시 python 32bit를 사용

## 설치
```shell script
pip install xing-tick-crawler
```

## 사용예시
#### 1. config.py 파일 생성 및 설정 
```python
config = {
    "id": "my_id",  # xing api 아이디
    "password": "my_password",  # xing api 패스워드
    "cert_password": "my_cert_password",  # 공동인증서 비밀번호
}

RES_FOLDER_PATH = "C:/eBEST/xingAPI/Res"  # xing_tick_crawler Res 파일 폴더 위치
TICKER_DATA_FOLDER_PATH = "."  # tick 데이터 저장할 위치
```

#### 2. main.py 생성 및 실행
 - 필요없는 데이터 off 하고, 실행
```python
"""
크롤러 1 구독옵션 (기본값 All True)
    - STOCK_VI_ON_OFF
    - KOSPI_ORDER_BOOK
    - KOSPI_AFTER_MARKET_ORDER_BOOK
    - KOSPI_AFTER_MARKET_TICK
    - KOSPI_BROKER_INFO
    - STOCK_FUTURES_ORDER_BOOK
    - STOCK_FUTURES_TICK

크롤러 2 구독옵션 (기본값 All True)
    - KOSDAQ_ORDER_BOOK
    - KOSDAQ_AFTER_MARKET_ORDER_BOOK
    - KOSDAQ_AFTER_MARKET_TICK
    - KOSDAQ_BROKER_INFO
"""

from xing_tick_crawler.crawler import crawler_1, crawler_2, crawl_kospi_tick, crawl_kosdaq_tick
from datetime import datetime
from multiprocessing import Process, get_context
from multiprocessing.queues import Queue

if __name__ == "__main__":
    crawler_1_subs_option = {
        # 주식 VI 정보 off
        'STOCK_VI_ON_OFF': False,
    }
    crawler_2_subs_option = {

    }

    queue = Queue(ctx=get_context())
    p1 = Process(target=crawl_kospi_tick, args=(queue,))
    p2 = Process(target=crawl_kosdaq_tick, args=(queue,))
    p3 = Process(target=crawler_1, args=(queue,), kwargs=crawler_1_subs_option)
    p4 = Process(target=crawler_2, args=(queue,), kwargs=crawler_2_subs_option)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    while True:
        tick = queue.get()
        waiting_tasks = queue.qsize()
        tick_type, tick_data = tick
        print(f"\r{datetime.now()} waiting tasks : {'%6d' % waiting_tasks}", end='')
        print(tick_type, tick_data)


```


## 구현 Real 목록
#### 주식시장
 - [x] 코스피 호가
 - [x] 코스피 체결
 - [x] 코스닥 호가
 - [x] 코스닥 체결
 - [x] 주식VI 발동해제
 - [x] 코스피 시간외단일가 호가
 - [x] 코스피 시간외단일가 체결
 - [x] 코스닥 시간외단일가 호가
 - [x] 코스닥 시간외단일가 체결
 - [X] 코스피 거래원
 - [X] 코스닥 거래원
 - [ ] 코스피 프로그램매매 종목별
 - [ ] 코스닥 프로그램매매 종목별

#### 선물옵션시장
 - [x] 주식선물 호가
 - [x] 주식선물 체결
 - [ ] 주식선물 가격제한폭확대
 - [ ] 코스피200 선물호가
 - [ ] 코스피200 선물체결
 - [ ] 코스피200 옵션체결
 - [ ] 코스피200 옵션호가
 - [ ] 코스피200 옵션가격제한폭확대