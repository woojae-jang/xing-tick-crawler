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
from multiprocessing import Process, get_context
from multiprocessing.queues import Queue
from datetime import datetime
from xing_tick_crawler.crawler import stock_crawler, stock_futures_crawler
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

```


## 기능
 - [x] 코스피 호가
 - [x] 코스피 체결
 - [x] 코스닥 호가
 - [x] 코스닥 체결
 - [x] 주식선물 호가
 - [x] 주식선물 체결
 - [ ] 코스피200 선물호가
 - [ ] 코스피200 선물체결
 - [ ] 코스피 시간외단일가 호가
 - [ ] 코스피 시간외단일가 체결
 - [ ] 코스닥 시간외단일가 호가
 - [ ] 코스닥 시간외단일가 체결
 - [ ] 코스피 거래원
 - [ ] 코스닥 거래원
 - [ ] 주식VI 발동해제