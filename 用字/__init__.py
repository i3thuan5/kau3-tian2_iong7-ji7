import json


from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 用字.公家 import 用字檔名
from 臺灣言語工具.基本物件.字 import 字


with open(用字檔名) as 檔案:
    _全部分詞 = set(json.load(檔案))


class 教典:

    @classmethod
    def 全部分詞(cls):
        return _全部分詞

    @classmethod
    def 有這个字無(cls, 字物件):
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        # 不檢查輕聲符
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0')
        return 字臺羅物件.看分詞() in cls.全部分詞()


class 標點:
    @classmethod
    def 全部標點(self):
        return (
            ("「", '"'),
        )

    @classmethod
    def 提全部標點(self):
        全部用字 = set()
        for 一標點 in self.全部標點():
            全部用字.add(
                字(一標點[0], 一標點[1]).看分詞()
            )
        return 全部用字

    @classmethod
    def 有這个字無(cls, 字物件):
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        # 不檢查輕聲符
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0')
        return 字臺羅物件.看分詞() in cls.提全部標點()
