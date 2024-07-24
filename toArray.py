import json
from os import listdir
from os.path import isfile, join

str = """
https://www.mediafire.com/file/5r2hnttlc86jstt/Umeko+J+-+Arlecchino+(mitaku.net).rar/file,
https://www.mediafire.com/file/j04e5iio9hbf4vn/Umeko+J+-+Arlecchino+(Video)+(mitaku.net).rar/file,
https://www.mediafire.com/file/jdwsgrxt691mo5r/Umeko+J+-+Purah+(mitaku.net).rar/file,
https://www.mediafire.com/file/ukudb56sinak7jd/Umeko+J+-+Purah+(Video)+(mitaku.net).rar/file,
https://www.mediafire.com/file/tz0ulp5wyujng7n/Umeko_J_-_Tamaki_Kotatsu_%28mitaku.net%29.rar/file,
https://www.mediafire.com/file/e0w2nmc52dk11g3/Umeko+J+-+Tamaki+Kotatsu+(Video).rar/file,
https://www.mediafire.com/file/dpiqqm4lfzc8xjh/Umeko+J+-+Yae+Miko+Bikini+(mitaku.net).rar/file,
https://www.mediafire.com/file/d7f9l5t922lp6t3/Umeko+J+-+Yae+Miko+Bikini+(Video)+(mitaku.net).rar/file,
https://www.mediafire.com/file/2kb5v7ld1mpeg8u/Umeko+J+-+Rupee+(NIKKE)+(mitaku.net).rar/file,
https://www.mediafire.com/file/nv0l3l675n1crku/Umeko+J+-+Rupee+(NIKKE)+(Video)+(mitaku.net).rar/file,
https://www.mediafire.com/file/aotzskx6dfbkfiw/Umeko+J+-+Ahri+(mitaku.net).rar/file,
https://www.mediafire.com/file/64xjgsjnmtqiy0q/Umeko+J+-+Ahri+(Video)+(mitaku.net).rar/file,
https://www.mediafire.com/file/qfw4gc0007bqoi0/Umeko+J+-+Tifa+Swimsuit+(mitaku.net).rar/file,
https://www.mediafire.com/file/j5edyflayqt3yfd/Umeko+J+-+Tifa+Swimsuit+(Video)+(mitaku.net).rar/file,
https://www.mediafire.com/file/ixlyruylzr2qyxp/Umeko+J+-+Roxy+Migurdia+(mitaku.net).rar/file,
https://www.mediafire.com/file/4j7rjr735mvu2ow/Umeko+J+-+Yor+Forger+Red+Sweater+(mitaku.net).rar/file,
https://www.mediafire.com/file/htpn3v0l9no9uk1/Umeko+J+-+Yor+Forger+Red+Sweater+(Video)+(mitaku.net).rar/file,
https://www.mediafire.com/file/2n8o88w8kjq4xe6/Umeko_J_-_Yuzuriha_%28Jigokuraku%29_%28mitaku.net%29.rar/file,
https://www.mediafire.com/file/clnzkkhoicb3f1e/Umeko_J_-_Yuzuriha_%28Jigokuraku%29_%28Video%29_%28mitaku.net%29.rar/file,
"""

str2 = """
https://download2346.mediafire.com/wa2xpi2e775gfXR5CkFD4jP62S5WF5lmYtQ-vlv7Qe9HAa2SbspjfV4XZlaaVriK0rmDfiq4RkcqvFPA04yMzJZaTcsqrBEyXofO30NsvW9KKU-xMFDR3nGxZdlmohfh6jYA1FmJBIIJdih9dNbLMdvtdmqDNi_YcyGgQYn2lQwLbOg/5r2hnttlc86jstt/Umeko+J+-+Arlecchino+%28mitaku.net%29.rar,
https://download2302.mediafire.com/fcobu0q9qgtgeuMtw1Lyjr0maUCFhzZmGTNI8KQLbz30X515N8plQ9adU_q2I1FrzSCdJ0b9hXfrLtgF4JS4gW4_UlXT0AUITJMZIOfaM8LXZZaHR1kb7yIhB26XmPWFFY3HNxeUbq8Eze25Um8YrN4KEuJAlEetn3p2pu4yMa6BteQ/j04e5iio9hbf4vn/Umeko+J+-+Arlecchino+%28Video%29+%28mitaku.net%29.rar,
https://download1507.mediafire.com/9wk1n24xqedgnj2tw4PsyxGzXhOtZQWV1RzASXAnLnBHiSNKZAv2rObusZppCimxlKspCA9scyyo3IRzwrGlwsESwGhP0H9EVX5hCPlRB1c95RgzCYaeZILL97OOd-tVEJqegoEdDeLCcwpQ5HryA6fnBB4cbhh-J_KWpkBgyYI7cnM/jdwsgrxt691mo5r/Umeko+J+-+Purah+%28mitaku.net%29.rar,
https://download2278.mediafire.com/1y2iajyozw0gmDJW9F5tDQdNnp3Bz6UZJX2gT5a5d6JHIcIleL1hDNY2BC0hi8_MZRJpA8DEOjaYEEYqFwD6oXZhJTEKdt2dMsL0gzPZyYbeuIOpm6daHqVSayUT1zvQQv6Obh0Jy5kuSEaz15rYA4eZ6ZaQlK1XM8Lv8u1Sw-VlV7c/ukudb56sinak7jd/Umeko+J+-+Purah+%28Video%29+%28mitaku.net%29.rar,
https://download2293.mediafire.com/fe7eneebaivgiUhU_sZUSIfMUTrrl9NzzdUcPC3jyy_pyxSgv28WPYqBPZimF-AD57TOUhDP2Nk0PLvMtkvBSWOjTSqDcUpOHA-TMHH64q-95Js1vc29gOC-VTboFAJafFj4wgFO1S5Uf-sjFw-B9Vy7UvQ4EBZ_RakGeclS7aCl8G8/tz0ulp5wyujng7n/Umeko+J+-+Tamaki+Kotatsu+%28mitaku.net%29.rar,
https://download2392.mediafire.com/9q187y65m1jg1R9DWlu1QYTleMJY5jkTm_aRwWGS6v5tptF-98EKiaH3ZHsI4O96uui4VsOiCMwSXnsoPQsIWW2gbOBUGUmt4Usa3KPAGMvxebi9kzh6kWPxRlD8SPfBs5SqRKik1zsbYvmT-HUb5lIVX4yonM0MLlTFnUBXang0XCU/e0w2nmc52dk11g3/Umeko+J+-+Tamaki+Kotatsu+%28Video%29.rar,
https://download1503.mediafire.com/c30dtbtb0xegVDtdQiZCDxF1yql0FXgYc_U-d1IfYAQ597ZkAHvNdAwKDRiEx3O0ds6jVytGrdfKl8We5U14iP6jzxh7Z6Z7xk-lN1P1RhfHkag-1KbIKCyjX5Nk59HetxxEAZcGKPkjVnmB-HWrt0wZW3_YaYvMHSJW0q7_c3MSbFw/dpiqqm4lfzc8xjh/Umeko+J+-+Yae+Miko+Bikini+%28mitaku.net%29.rar,
https://download2292.mediafire.com/4m0xfg84njzgVfYyTjNwzz5pLso3t0hmZ48aHUr_vt0CdbrVEdxU68qbwwY4fZ8aOvLiuBZrvwKc6TaJIsObA1-sz894CnO3rgD2GtbaLMmePhE9srh67-NVFiNzXyU4pGr20RZn_iaP_COLD5V5ETy_lFciXuuFDRlO76YQW7BwC_U/d7f9l5t922lp6t3/Umeko+J+-+Yae+Miko+Bikini+%28Video%29+%28mitaku.net%29.rar,
https://download1334.mediafire.com/o6k31pmio7dgpxnEWMqOLiFbbrICuecM5vqHuTnYu3K3VeMXrDEtFGgajm09BTVZgzFGKKtwRLOoZlp4lxUczI61NupoE8PEBNkZ_H4b6S8jfYmtx6rz90ckPw5G-_FjaItXvlePDvwNSihIVaFXX2Brya05x9_x8k3mAAJ1l1q3y4s/2kb5v7ld1mpeg8u/Umeko+J+-+Rupee+%28NIKKE%29+%28mitaku.net%29.rar,
https://download2278.mediafire.com/jmw68uav0r5gqZtfGYwTqzbYfNjlWdc9aLXT0UpH3iyM-7dRP1cioHPcWQQ5BKMIemgsFD2aBuNFIOqT4aMp88Z9kVKvoRngTvuxuiaLg4RmyfYM0plLjgJncH9D7wbcKKXASG1PfJ1t0t945llDYYRUBaN_h-H4_J8RSou2GWJFJHU/nv0l3l675n1crku/Umeko+J+-+Rupee+%28NIKKE%29+%28Video%29+%28mitaku.net%29.rar,
https://download856.mediafire.com/0uq48pyqm20g7JEpElIdOCK1_ZAArCgA0P66ZQWdKgCGYTDODL9FMnQLFndvRRPxNHkbll2MWqgBpqk_gDohB1GKYiypCAjYZKOEe-Qhm3XpUZgnecTwyTPPVLtYnrvoluNDkVLKejZe32jh6ybFyaoRt97Sa0uq5yQV27T2uKXo4J0/aotzskx6dfbkfiw/Umeko+J+-+Ahri+%28mitaku.net%29.rar,
https://download1321.mediafire.com/ckds2q4gkzvguqH75RnsRhHuIHSNwu78THlLYh1f05sugAns4x7_Kq7KJA7NUHqmARwIg_EgGMk85pRx3fVdlpGWZDgx96rGcKtJ80ukLtySGZQzJnXUoMEtXuNlW_cdFVY3YtHlsS8h_LB2_6-ejaZA1CbcdG0em_6WrQiaLQ8UsoI/64xjgsjnmtqiy0q/Umeko+J+-+Ahri+%28Video%29+%28mitaku.net%29.rar,
https://download2287.mediafire.com/5dtts361082gkvtweK2a6lLJsVxNllpDGGIjrYV8LkXY_qFJ1bc38t-nsR8pysQOFF5qk-_18b4QmTK-WigdfgAhnEE-W-IGuBMBRThZ0X7qngYkEQXk8xc36vouqU0QaaWqyDOlgGCzN-MI626Kd3uHrIdHPI6cLoiXvYx0m8Yd5w/qfw4gc0007bqoi0/Umeko+J+-+Tifa+Swimsuit+%28mitaku.net%29.rar,
https://download2303.mediafire.com/0hfy7tocielgPK071L_T3SEWbMh5z4hcDuwz-8d70n9PcWXDWQ6jGwGOJY5JA8V9w1rQ3TXt0apkA23qmCy9G-qqR6I-Q1Psqu7Vo4DWdBPdQgkpd-zj5ha1-Esu_5EwHSPaH0u5H03_AqUHyy7OH_kAWTdHo5zGO9-Z91pOKDrd/j5edyflayqt3yfd/Umeko+J+-+Tifa+Swimsuit+%28Video%29+%28mitaku.net%29.rar,
https://download1514.mediafire.com/b8rdqsgm4dcgNay1rY-aDQ2i_bqmlja7dSgpU4jAMefkCmWvxFWFtX9WfkC1hSn3EM3qeJsDe1TymjFUCCVZMylncuu9qZ2Ab4rL6DXQcaVQQ8e7f6cpVzmOkqXJzSXmAS2nKMDPBt3JBvjfu7WKFoLQ3FY8LqdOrayP0-GvFG_6r6M/ixlyruylzr2qyxp/Umeko+J+-+Roxy+Migurdia+%28mitaku.net%29.rar,
https://download1593.mediafire.com/r2q11l3rcfugrTV81aK2lmTzMQvA9iShF0N_6yYH9z5cdto1-sB_spVKW-1k5fvBWqXD6l-leA9YZsmVuMvkXkKLg4g2j2x9ekblywEHc3k-xRj3cANSxkKW3grT9bZsodKetR-vh3Vo5MCizAlHdiuDXtr0-5VFetNPkGl014Qh0uc/4j7rjr735mvu2ow/Umeko+J+-+Yor+Forger+Red+Sweater+%28mitaku.net%29.rar,
https://download948.mediafire.com/kjrvpx9nr6hgpYsc75iUvLB_nYfmxf2TwRYB4YtXvlsOKJ-6liVa2OedSSLlnpQtYlSxwgFe3rsgS2S7PcUHw3gNZ9HzFzIDu1qVvr-v1HgtWeyroM9iN8Vy3CS2EPwJPg68MVyOAHNUhj2bySjm2c7ipvhosg9JjbgpOiBpgaI2hY4/htpn3v0l9no9uk1/Umeko+J+-+Yor+Forger+Red+Sweater+%28Video%29+%28mitaku.net%29.rar,
https://download850.mediafire.com/bklb5ccdgvng53pgDe5kGZDdL-5wcdRwRvTSHxz7eSSRvbSQ36AxZAkU5wUtKoxoJxi48Brb4KibUYBP_E48VHwglVyE00yJtHvR6dV-Ecv5G18Kv1db3JOc-ldDQCxdThs8SSTqO9CV8eN8_TDnxy_YIo8ZC9G0kIw5B0LQ2uao24E/2n8o88w8kjq4xe6/Umeko+J+-+Yuzuriha+%28Jigokuraku%29+%28mitaku.net%29.rar,
https://download1336.mediafire.com/96rhwzxl6jpgZRaR9NVpEaJ9ayEECXgYHkpYIr42QidI83TEQUlcYCXM3PAdfL1ZyV3FTQkbyrf25iewEO7zo4jMJQILHlYMyGXfrU7JNeRXACPRkR1Lo1tm1DVPBKU_jIutTNw5wFfDaT9NqWvSeDCvaBqiTkoV61uOIPaTZn4Ntdk/clnzkkhoicb3f1e/Umeko+J+-+Yuzuriha+%28Jigokuraku%29+%28Video%29+%28mitaku.net%29.rar,
"""


#read string from txt file and split by comma
def readStringFromFile(fileName):
    with open(fileName, 'r') as f:
        return f.read().split(',')


#write list to txt file
def writeListToFile(fileName, lst):
    with open(fileName, "w") as file:
        json.dump(lst, file)


#read all tmp*.txt files then split by comma and write to final*.txt
def readTmpFilesAndWriteToFinalFile():
    #find all tmp*.txt files in current path
    files = [f for f in listdir(".") if isfile(join(".", f)) and f.endswith(".txt")]

    for i in files:
        finalList = readStringFromFile(i)
        writeListToFile(f"{i}_final.txt", finalList)


readTmpFilesAndWriteToFinalFile()
