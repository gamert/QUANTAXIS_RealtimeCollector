__version__ = '0.0.10'
__author__ = 'yutiansut'

import re

import click
import threading
from QARealtimeCollector.clients import QARTC_Clients
from QARealtimeCollector.collectors import (QARTC_CtpBeeCollector,
                                            QARTC_CTPTickCollector,
                                            QARTC_RandomTick, QARTC_Stock,
                                            QARTC_WsCollector)
from QARealtimeCollector.connector.QATdx_adv import QA_Tdx_Executor
from QARealtimeCollector.datahandler import QARTC_Resampler
from QARealtimeCollector.utils.common import str_eval


@click.command()
@click.option('--code', default='rb2106')
def start(code):
    r = QARTC_CtpBeeCollector(code)
    r.start()


@click.command()
@click.option('--code', default='rb2106')
def start_ctp(code):
    r = QARTC_CTPTickCollector(code)
    r.start()


@click.command()
@click.option('--code', default='rb2106')
def faststart(code):
    r = QARTC_CtpBeeCollector(code)
    r.start()
    # r1 = QARTC_Resampler(code, '1min', 'tb')
    # r1.start()
    r2 = QARTC_Resampler(code, '5min', 'tb')
    r2.start()
    # r3 = QARTC_Resampler(code, '15min', 'tb')
    # r3.start()
    # r4 = QARTC_Resampler(code, '30min', 'tb')
    # r4.start()
    # r5 = QARTC_Resampler(code, '60min', 'tb')
    # r5.start()


@click.command()
@click.option('--code', default='rb2106')
@click.option('--freq', default='5min')
@click.option('--model', default='tb')
def resample(code, freq, model):
    r = QARTC_Resampler(code, freq, model)
    r.start()


@click.command()
@click.option('--code', default='rb2106')
@click.option('--date', default='20210202')
@click.option('--price', default=3646)
@click.option('--interval', default=0)
def random(code, date, price, interval):
    print(code, date, price, interval)
    r = QARTC_RandomTick(code, date, price, interval)
    r.start()


def stock_collector():
    QARTC_Stock().start()

if __name__ == "__main__":
    # 监听ctp tick,转发...
    code = '"OKEX.1INCH-USDT"'
    code = str_eval(code)
    code = str_eval(code)
    if re.search(r'[a-zA-z]+\.[0-9a-zA-z]+\-[0-9a-zA-z]+', code):
        print(code," is CRYPTOCURRENCY")
    #code = "rb2106"
    r = QARTC_CTPTickCollector(code)
    r.start()
    #start_ctp()

    #启动随机行情()
    #random()
    #
    #faststart()
