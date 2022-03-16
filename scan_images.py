import os
import re

urls = ['core_sys/images/main/cont/hero_chara_character.png']

base_dir = 'raw/sukasuka-anime-images/sukasuka-anime.com/chara'
html_files = [os.path.join(base_dir, file) for file in os.listdir(base_dir) if file.endswith(".html")]

for file in html_files:
    with open(file, encoding='utf-8') as f:
        content = f.read()
        new_urls = re.findall('''<div class="block line_02">[\s\S]*<div class="img_l [\s\S]*<div class="ph"><img src="\.\./(.*)\.png.*" alt="" title="" /></div>''', content)
        new_urls = [url[:-4] + '.png' for url in new_urls]
        urls += new_urls
urls = [os.path.join('http://sukasuka-anime.com', i).replace('\\', '/') for i in urls]
print(urls)
