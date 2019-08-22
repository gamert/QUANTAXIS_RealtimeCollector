import json

import pandas as pd

from QAPUBSUB.consumer import subscriber
from QAPUBSUB.producer import publisher_routing
from QUANTAXIS.QAEngine import QA_Thread, QA_Task

# 接受并分析


class client(QA_Thread):

    def __init__(self):
        super().__init__(name='qasubclient', daemon=False)

        self.req = publisher_routing(
            exchange='QARealtime_Market', routing_key='stock')
        self.last_ab = pd.DataFrame()
        self.sub = subscriber(exchange='stocktransaction')
        self.sub.callback = self.callback

    def subscribe(self, code='000007'):
        req.pub(json.dumps({'topic': 'subscribe', 'code': code}),
                routing_key='stock')

    def callback(self, b, c, data):
        data = json.loads(data)

        data = pd.DataFrame(data).set_index(['code']).loc[:, [
            'ask_vol2', 'ask2', 'ask_vol1', 'ask1', 'price', 'bid1', 'bid_vol1', 'bid2', 'bid_vol2']]

        self.put({'topic': 'new_data',
                  'data': data})

    def run(self):
        threading.Thread(target=self.sub.start, daemon=True).start()
        try:
            data = self.queue.get_nowait()

        except Exception as e:
            print(e)
