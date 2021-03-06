# -*- coding: utf-8 -*-
import json
from os.path import join, abspath, dirname
from 教典.匯入甘字典 import 甘字典字物件
from 教典.匯入資料 import 教典字物件
from 教典.匯入教典名姓 import 教典名姓字物件


def main():
    產生教典json()
    產生教典名姓json()
    產生甘字典json()


def 產生教典json():
    教典檔名 = join(dirname(abspath(__file__)), '用字', '教典.json')

    全部用字 = set()
    for 字物件 in 教典字物件.全部資料():
        字物件.輕聲標記 = False
        全部用字.add(
            字物件.看分詞()
        )
    with open(教典檔名, 'w') as 檔案:
        json.dump(
            sorted(全部用字), 檔案,
            indent=2,
            ensure_ascii=False
        )



def 產生教典名姓json():
    教典名姓檔名 = join(dirname(abspath(__file__)), '用字', '教典名姓.json')

    全部用字 = set()
    for 字物件 in 教典名姓字物件.全部資料():
        字物件.輕聲標記 = False
        全部用字.add(
            字物件.看分詞()
        )
    with open(教典名姓檔名, 'w') as 檔案:
        json.dump(
            sorted(全部用字), 檔案,
            indent=2,
            ensure_ascii=False
        )


def 產生甘字典json():
    檔名 = join(dirname(abspath(__file__)), '用字', '甘字典.json')

    全部用字 = set()
    for 字物件 in 甘字典字物件().詞目():
        全部用字.add(
            字物件.看分詞()
        )
    with open(檔名, 'w') as 檔案:
        json.dump(
            sorted(全部用字), 檔案,
            indent=2,
            ensure_ascii=False
        )


if __name__ == '__main__':
    main()
