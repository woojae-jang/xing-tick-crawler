from enum import Enum


class DataType(Enum):
    KOSPI_ORDER_BOOK = 1
    KOSPI_TICK = 2

    KOSDAQ_ORDER_BOOK = 3
    KOSDAQ_TICK = 4

    STOCK_FUTURES_ORDER_BOOK = 5
    STOCK_FUTURES_TICK = 6

    KOSPI_AFTER_MARKET_ORDER_BOOK = 7
    KOSPI_AFTER_MARKET_TICK = 8

    KOSDAQ_AFTER_MARKET_ORDER_BOOK = 9
    KOSDAQ_AFTER_MARKET_TICK = 10

    STOCK_VI_ON_OFF = 11


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
STOCK_FUTURES_TICK_COLUMNS = [
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

AFTER_MARKET_TICK_FIELDS = [
    "shcode",              # 단축코드
    "danchetime",          # 시간외단일가체결시간
    "dansign",             # 시간외단일가전일대비구분
    "danchange",           # 시간외단일가전일대비
    "dandrate",            # 시간외단일가등락율
    "danprice",            # 시간외단일가현재가
    "danopentime",         # 시간외단일가시가시간
    "danopen",             # 시간외단일가시가
    "danhightime",         # 시간외단일가고가시간
    "danhigh",             # 시간외단일가고가
    "danlowtime",          # 시간외단일가저가시간
    "danlow",              # 시간외단일가저가
    "dancgubun",           # 시간외단일가체결구분
    "dancvolume",          # 시간외단일가체결량
    "danvolume",           # 시간외단일가누적거래량
    "danvalue",            # 시간외단일가누적거래대금
    "danmdvolume",         # 시간외단일가매도누적체결량
    "danmdchecnt",         # 시간외단일가매도누적체결건수
    "danmsvolume",         # 시간외단일가매수누적체결량
    "danmschecnt",         # 시간외단일가매수누적체결건수
    "danprevolume",        # 시간외단일가직전거래량
    "danprecvolume",       # 시간외단일가직전체결수량
    "dancpower",           # 시간외단일가체결강도
    "danstatus",           # 시간외단일가장정보
]

AFTER_MARKET_TICK_COLUMNS = [
    "system_time",
    *AFTER_MARKET_TICK_FIELDS
]

AFTER_MARKET_ORDER_BOOK_FIELDS = [
    "shcode",                    # 단축코드
    "dan_hotime",                # 시간외단일가호가시간
    "dan_hstatus",               # 시간외단일가장구분
    "dan_offerho1",              # 시간외단일가매도호가1
    "dan_bidho1",                # 시간외단일가매수호가1
    "dan_offerrem1",             # 시간외단일가매도호가잔량1
    "dan_bidrem1",               # 시간외단일가매수호가잔량1
    "dan_preoffercha1",          # 시간외단일가직전매도대비수량1
    "dan_prebidcha1",            # 시간외단일가직전매수대비수량1
    "dan_offerho2",              # 시간외단일가매도호가2
    "dan_bidho2",                # 시간외단일가매수호가2
    "dan_offerrem2",             # 시간외단일가매도호가잔량2
    "dan_bidrem2",               # 시간외단일가매수호가잔량2
    "dan_preoffercha2",          # 시간외단일가직전매도대비수량2
    "dan_prebidcha2",            # 시간외단일가직전매수대비수량2
    "dan_offerho3",              # 시간외단일가매도호가3
    "dan_bidho3",                # 시간외단일가매수호가3
    "dan_offerrem3",             # 시간외단일가매도호가잔량3
    "dan_bidrem3",               # 시간외단일가매수호가잔량3
    "dan_preoffercha3",          # 시간외단일가직전매도대비수량3
    "dan_prebidcha3",            # 시간외단일가직전매수대비수량3
    "dan_offerho4",              # 시간외단일가매도호가4
    "dan_bidho4",                # 시간외단일가매수호가4
    "dan_offerrem4",             # 시간외단일가매도호가잔량4
    "dan_bidrem4",               # 시간외단일가매수호가잔량4
    "dan_preoffercha4",          # 시간외단일가직전매도대비수량4
    "dan_prebidcha4",            # 시간외단일가직전매수대비수량4
    "dan_offerho5",              # 시간외단일가매도호가5
    "dan_bidho5",                # 시간외단일가매수호가5
    "dan_offerrem5",             # 시간외단일가매도호가잔량5
    "dan_bidrem5",               # 시간외단일가매수호가잔량5
    "dan_preoffercha5",          # 시간외단일가직전매도대비수량5
    "dan_prebidcha5",            # 시간외단일가직전매수대비수량5
    "dan_totofferrem",           # 시간외단일가총매도호가잔량
    "dan_totbidrem",             # 시간외단일가총매수호가잔량
    "dan_preoffercha",           # 시간외단일가직전매도호가총대비수량
    "dan_prebidcha",             # 시간외단일가직전매수호가총대비수량
    "dan_yeprice",               # 시간외단일가예상체결가격
    "dan_yevolume",              # 시간외단일가예상체결수량
    "dan_preysign",              # 시간외단일가예상가직전가대비구분
    "dan_preychange",            # 시간외단일가예상가직전가대비
    "dan_jnilysign",             # 시간외단일가예상가전일가대비구분
    "dan_jnilychange",           # 시간외단일가예상가전일가대비
]

AFTER_MARKET_ORDER_BOOK_COLUMNS = [
    "system_time",
    *AFTER_MARKET_ORDER_BOOK_FIELDS
]

STOCK_VI_ON_OFF_FIELDS = [
    "shcode",            # 단축코드(KEY)
    "vi_gubun",          # 구분(0:해제 1:정적발동 2:동적발동)
    "svi_recprice",      # 정적VI발동기준가격
    "dvi_recprice",      # 동적VI발동기준가격
    "vi_trgprice",       # VI발동가격
    "ref_shcode",        # 참조코드
    "time",              # 시간
]

STOCK_VI_ON_OFF_COLUMNS = [
    "system_time",
    *STOCK_VI_ON_OFF_FIELDS
]

TR_CODE_TICK_TYPE_MAP = {
    "H1_": DataType.KOSPI_ORDER_BOOK,                   # 코스피 호가
    "S3_": DataType.KOSPI_TICK,                         # 코스피 체결
    "HA_": DataType.KOSDAQ_ORDER_BOOK,                  # 코스닥 호가
    "K3_": DataType.KOSDAQ_TICK,                        # 코스닥 체결
    "JH0": DataType.STOCK_FUTURES_ORDER_BOOK,           # 주식선물 호가
    "JC0": DataType.STOCK_FUTURES_TICK,                 # 주식선물 체결
    "DH1": DataType.KOSPI_AFTER_MARKET_ORDER_BOOK,      # 코스피 시간외 단일가 호가
    "DS3": DataType.KOSPI_AFTER_MARKET_TICK,            # 코스피 시간외 단일가 체결
    "DHA": DataType.KOSDAQ_AFTER_MARKET_ORDER_BOOK,     # 코스닥 시간외 단일가 호가
    "DK3": DataType.KOSDAQ_AFTER_MARKET_TICK,           # 코스닥 시간외 단일가 체결
    "VI_": DataType.STOCK_VI_ON_OFF,                    # 주식 VI 발동해제
}

TR_CODE_FIELDS_LIST_MAP = {
    "H1_": ORDER_BOOK_FIELDS,                     # 코스피 호가
    "S3_": TICK_FIELDS,                           # 코스피 체결
    "HA_": ORDER_BOOK_FIELDS,                     # 코스닥 호가
    "K3_": TICK_FIELDS,                           # 코스닥 체결
    "JH0": STOCK_FUTURES_ORDER_BOOK_FIELDS,       # 주식선물 호가
    "JC0": STOCK_FUTURES_TICK_FIELDS,             # 주식선물 체결
    "DH1": AFTER_MARKET_ORDER_BOOK_FIELDS,        # 코스피 시간외 단일가 호가
    "DS3": AFTER_MARKET_TICK_FIELDS,              # 코스피 시간외 단일가 체결
    "DHA": AFTER_MARKET_ORDER_BOOK_FIELDS,        # 코스닥 시간외 단일가 호가
    "DK3": AFTER_MARKET_TICK_FIELDS,              # 코스닥 시간외 단일가 체결
    "VI_": STOCK_VI_ON_OFF_FIELDS,                # 주식 VI 발동해제
}
