from ._base import BaseImage

import requests


class Pulsar(BaseImage):
    name = 'pulsar'
    port = 8080

    def check(self):
        url = f'http://{self.host}:{self.get_port()}/'
        try:
            resp = requests.options(url)
            if 200 <= resp.status_code < 500:
                return True
        except Exception:
            pass
        return False


pulsar_image = Pulsar()
