from django.test.testcases import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字.models import 用字表


class 用字試驗(TestCase):

    def test_字物件(self):
        self.assertTrue(用字表.有這个字無(字('來', 'lai5')))

    def test_輕聲有(self):
        self.assertTrue(用字表.有這个字無(字('來', '0lai5')))

    def test_無輕聲(self):
        self.assertFalse(用字表.有這个字無(字('巧', '0khiau2')))

    def test_干焦輕聲(self):
        self.assertTrue(用字表.有這个字無(字('矣', '0ah4')))

    def test_無實調(self):
        self.assertTrue(用字表.有這个字無(字('矣', 'ah4')))

    def test_羅馬字佮羅馬字(self):
        self.assertFalse(用字表.有這个字無(字('lai5', 'lai5')))
