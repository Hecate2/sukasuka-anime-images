import os
import traceback
import random
from http.server import HTTPServer, BaseHTTPRequestHandler

urls = [
    'http://sukasuka-anime.com/core_sys/images/main/cont/hero_chara_character.png',
    'http://sukasuka-anime.com/core_sys/images/contents/00000018/block/00000062/00000049.png',
    'http://sukasuka-anime.com/core_sys/images/contents/00000020/block/00000066/00000053.png',
    'http://sukasuka-anime.com/core_sys/images/contents/00000021/block/00000068/00000055.png',
    'http://sukasuka-anime.com/core_sys/images/contents/00000029/block/00000084/00000071.png',
]
urls += [
    'http://sukasuka-anime.com/core_sys/images/main/cont/hero_chara_staffcast.png',
    'http://sukasuka-anime.com/core_sys/images/main/cont/hero_chara_bluraydvd.png',
    'http://sukasuka-anime.com/core_sys/images/main/cont/hero_chara_goods.png',
]


class Redirect(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(302)
        self.send_header('Location', random.choice(urls))
        self.end_headers()


port = int(os.environ.get('PORT', 8080))
try:
    HTTPServer(("", port), Redirect).serve_forever()
except:
    traceback.print_exc()
