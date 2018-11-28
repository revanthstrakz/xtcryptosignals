__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import settings as s
from binance.client import Client
from binance.exceptions import BinanceAPIException


class Binance:
    def __init__(self):
        self.client = Client(
            s.BINANCE_API_KEY, s.BINANCE_API_SECRET
        )

    def get_ticker(self, symbol):
        _symbol = ''.join(symbol)
        try:
            return self.client.get_ticker(symbol=_symbol)
        except BinanceAPIException:
            raise ValueError(
                'Invalid Symbol: {}'.format(_symbol)
            )
        except Exception as err:
            raise ValueError(str(err))
