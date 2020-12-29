from enum import Enum


class DataType(Enum):
    KOSPI_ORDER_BOOK = 1
    KOSPI_TICK = 2

    KOSDAQ_ORDER_BOOK = 3
    KOSDAQ_TICK = 4

    STOCK_FUTURES_ORDER_BOOK = 5
    STOCK_FUTURES_TICK = 6


ORDER_BOOK_FIELDS = [
    "shcode", "hotime", "donsigubun", "totofferrem", "totbidrem",
    "offerho1", "bidho1", "offerrem1", "bidrem1",
    "offerho2", "bidho2", "offerrem2", "bidrem2",
    "offerho3", "bidho3", "offerrem3", "bidrem3",
    "offerho4", "bidho4", "offerrem4", "bidrem4",
    "offerho5", "bidho5", "offerrem5", "bidrem5",
    "offerho6", "bidho6", "offerrem6", "bidrem6",
    "offerho7", "bidho7", "offerrem7", "bidrem7",
    "offerho8", "bidho8", "offerrem8", "bidrem8",
    "offerho9", "bidho9", "offerrem9", "bidrem9",
    "offerho10", "bidho10", "offerrem10", "bidrem10",
]
ORDER_BOOK_COLUMNS = [
    "system_time",
    *ORDER_BOOK_FIELDS
]

TICK_FIELDS = [
    "shcode",
    "chetime",
    "sign",
    "change",
    "drate",
    "price",
    "opentime",
    "open",
    "hightime",
    "high",
    "lowtime",
    "low",
    "cgubun",
    "cvolume",
    "volume",
    "value",
    "mdvolume",
    "mdchecnt",
    "msvolume",
    "mschecnt",
    "cpower",
    "w_avrg",
    "offerho",
    "bidho",
    "status",
    "jnilvolume",
]
TICK_COLUMNS = [
    "system_time",
    *TICK_FIELDS
]

STOCK_FUTURES_TICK_FIELDS = [
    "futcode",       # 단축코드
    "chetime",       # 체결시간
    "sign",          # 대비기호
    "change",        # 전일대비
    "drate",         # 등락율
    "price",         # 현재가
    "open",          # 시가
    "high",          # 고가
    "low",           # 저가
    "cgubun",        # 체결구분
    "cvolume",       # 체결량
    "volume",        # 누적거래량
    "value",         # 누적거래대금
    "mdvolume",      # 매도누적체결량
    "mdchecnt",      # 매도누적체결건수
    "msvolume",      # 매수누적체결량
    "mschecnt",      # 매수누적체결건수
    "cpower",        # 체결강도
    "offerho1",      # 매도호가1
    "bidho1",        # 매수호가1
    "openyak",       # 미결제약정수량
    "k200jisu",      # KOSPI200지수
    "theoryprice",   # 이론가
    "kasis",         # 괴리율
    "sbasis",        # 시장BASIS
    "ibasis",        # 이론BASIS
    "openyakcha",    # 미결제약정증감
    "jgubun",        # 장운영정보
    "jnilvolume",    # 전일동시간대거래량
]
STOCK_FUTURES_CONCLUSION_COLUMNS = [
    "system_time",
    *STOCK_FUTURES_TICK_FIELDS
]

STOCK_FUTURES_ORDER_BOOK_FIELDS = [
    "futcode",        # 단축코드
    "hotime",         # 호가시간
    "offerho1",       # 매도호가1
    "bidho1",         # 매수호가1
    "offerrem1",      # 매도호가수량1
    "bidrem1",        # 매수호가수량1
    "offercnt1",      # 매도호가건수1
    "bidcnt1",        # 매수호가건수1
    "offerho2",       # 매도호가2
    "bidho2",         # 매수호가2
    "offerrem2",      # 매도호가수량2
    "bidrem2",        # 매수호가수량2
    "offercnt2",      # 매도호가건수2
    "bidcnt2",        # 매수호가건수2
    "offerho3",       # 매도호가3
    "bidho3",         # 매수호가3
    "offerrem3",      # 매도호가수량3
    "bidrem3",        # 매수호가수량3
    "offercnt3",      # 매도호가건수3
    "bidcnt3",        # 매수호가건수3
    "offerho4",       # 매도호가4
    "bidho4",         # 매수호가4
    "offerrem4",      # 매도호가수량4
    "bidrem4",        # 매수호가수량4
    "offercnt4",      # 매도호가건수4
    "bidcnt4",        # 매수호가건수4
    "offerho5",       # 매도호가5
    "bidho5",         # 매수호가5
    "offerrem5",      # 매도호가수량5
    "bidrem5",        # 매수호가수량5
    "offercnt5",      # 매도호가건수5
    "bidcnt5",        # 매수호가건수5
    "offerho6",       # 매도호가6
    "bidho6",         # 매수호가6
    "offerrem6",      # 매도호가수량6
    "bidrem6",        # 매수호가수량6
    "offercnt6",      # 매도호가건수6
    "bidcnt6",        # 매수호가건수6
    "offerho7",       # 매도호가7
    "bidho7",         # 매수호가7
    "offerrem7",      # 매도호가수량7
    "bidrem7",        # 매수호가수량7
    "offercnt7",      # 매도호가건수7
    "bidcnt7",        # 매수호가건수7
    "offerho8",       # 매도호가8
    "bidho8",         # 매수호가8
    "offerrem8",      # 매도호가수량8
    "bidrem8",        # 매수호가수량8
    "offercnt8",      # 매도호가건수8
    "bidcnt8",        # 매수호가건수8
    "offerho9",       # 매도호가9
    "bidho9",         # 매수호가9
    "offerrem9",      # 매도호가수량9
    "bidrem9",        # 매수호가수량9
    "offercnt9",      # 매도호가건수9
    "bidcnt9",        # 매수호가건수9
    "offerho10",      # 매도호가10
    "bidho10",        # 매수호가10
    "offerrem10",     # 매도호가수량10
    "bidrem10",       # 매수호가수량10
    "offercnt10",     # 매도호가건수10
    "bidcnt10",       # 매수호가건수10
    "totofferrem",    # 매도호가총수량
    "totbidrem",      # 매수호가총수량
    "totoffercnt",    # 매도호가총건수
    "totbidcnt",      # 매수호가총건수
    "danhochk",       # 단일가호가여부
    "alloc_gubun",    # 배분적용구분
]
STOCK_FUTURES_ORDER_BOOK_COLUMNS = [
    "system_time",
    *STOCK_FUTURES_ORDER_BOOK_FIELDS
]
