import requests
from bs4 import BeautifulSoup


def get_link_with_aria_label(url, aria_label):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.content, 'html.parser')

        link = soup.find('a', attrs={'aria-label': aria_label})
        if link:
            return link['href']
        else:
            return None
    except Exception as e:
        print(e)
        return None


urls = ['https://www.mediafire.com/file/5r2hnttlc86jstt/Umeko+J+-+Arlecchino+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/j04e5iio9hbf4vn/Umeko+J+-+Arlecchino+(Video)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/jdwsgrxt691mo5r/Umeko+J+-+Purah+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/ukudb56sinak7jd/Umeko+J+-+Purah+(Video)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/tz0ulp5wyujng7n/Umeko_J_-_Tamaki_Kotatsu_%28mitaku.net%29.rar/file',
        'https://www.mediafire.com/file/e0w2nmc52dk11g3/Umeko+J+-+Tamaki+Kotatsu+(Video).rar/file',
        'https://www.mediafire.com/file/dpiqqm4lfzc8xjh/Umeko+J+-+Yae+Miko+Bikini+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/d7f9l5t922lp6t3/Umeko+J+-+Yae+Miko+Bikini+(Video)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/2kb5v7ld1mpeg8u/Umeko+J+-+Rupee+(NIKKE)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/nv0l3l675n1crku/Umeko+J+-+Rupee+(NIKKE)+(Video)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/aotzskx6dfbkfiw/Umeko+J+-+Ahri+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/64xjgsjnmtqiy0q/Umeko+J+-+Ahri+(Video)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/qfw4gc0007bqoi0/Umeko+J+-+Tifa+Swimsuit+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/j5edyflayqt3yfd/Umeko+J+-+Tifa+Swimsuit+(Video)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/ixlyruylzr2qyxp/Umeko+J+-+Roxy+Migurdia+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/4j7rjr735mvu2ow/Umeko+J+-+Yor+Forger+Red+Sweater+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/htpn3v0l9no9uk1/Umeko+J+-+Yor+Forger+Red+Sweater+(Video)+(mitaku.net).rar/file',
        'https://www.mediafire.com/file/2n8o88w8kjq4xe6/Umeko_J_-_Yuzuriha_%28Jigokuraku%29_%28mitaku.net%29.rar/file',
        'https://www.mediafire.com/file/clnzkkhoicb3f1e/Umeko_J_-_Yuzuriha_%28Jigokuraku%29_%28Video%29_%28mitaku.net%29.rar/file'
        ]
aria_label = "Download file"
final_links = []
for url in urls:
    link = get_link_with_aria_label(url, aria_label)
    if link:
        final_links.append(link)
    else:
        print(f"No link with aria-label '{aria_label}' found in {url}")

#toJson
for link in final_links:
    print(link+",")