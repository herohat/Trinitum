
import TLU as tlu
INIT_TMU = tlu.Init_TLU()

NOT_SET = None
CURRENT_TICK_HOLD = "NO POSITION/HOLD POSITION"
NO_EXIT_POSITIONS = "IN POSITION/NO EXIT POSITIONS"

CRYPTO_TICKERS = {"BTC": "USDT_BTC", "LTC": "USDT_LTC", "ETH": "USDT_ETH", "ETC": "USDT_ETC"}
POLO_PUBLIC_API = (0,0)

DAILY_RISK_FREE_RATE =  ((1+.91/100)**(1/252)-1)