from unittest.case import TestCase
from 用字.規範 import 教典
from 臺灣言語工具.基本物件.字 import 字


class 用字試驗(TestCase):

    def test_字物件(self):
        self.assertTrue(教典.有這个字無(字('來', 'lai5')))

    def test_輕聲有(self):
        self.assertTrue(教典.有這个字無(字('來', '0lai5')))

    def test_無輕聲(self):
        self.assertFalse(教典.有這个字無(字('巧', '0khiau2')))

    def test_干焦輕聲(self):
        self.assertTrue(教典.有這个字無(字('啦', '0lah4')))

    def test_無實調(self):
        self.assertFalse(教典.有這个字無(字('啦', 'lah4')))

    def test_羅馬字佮羅馬字(self):
        self.assertFalse(教典.有這个字無(字('lai5', 'lai5')))

    def test_又音(self):
        self.assertTrue(教典.有這个字無(字('觸', 'tau2')))

    def test_例句(self):
        self.assertTrue(教典.有這个字無(字('𪜶', '0in1')))

    def test_附錄提掉(self):
        self.assertFalse(教典.有這个字無(字('醫', 'penn7')))
