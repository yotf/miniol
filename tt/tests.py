from django.test import TestCase
from django.test import LiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver


from selenium import webdriver

class NewVisitorTest(TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_login(self):
        # Student hoce da pristupi kursu 'Programski Prevodioci' i svom
        # profilu, pa ode na homepage
        
        self.browser.get('http://localhost:8000/tt')
        # Primecuje rec Programski prevodioci u title-u
        self.assertIn("Programski prevodioci - dobrodosli",self.browser.title)
        
        self.fail("Finish writting tests!")
        # 1. Nije ulogovan i zeli da se uloguje
        #    a) Vidi login formular sa desne strane
        #    b) Kuca username i password
        #    c) Pritiska submit dugme ili kucka Enter
        #    d) i. Pogresan login - stranica updejtovana sa error messages
        #       ii.Uspesan login - stranica updejtovana i sada je customizovana za studenta
        #          I. Student primecuje:
        #            1)U title se pojavljuje ime studenta
        #            2) Navbar sadrzi njegovu sliku i notifikacije, i mozda jos nesto
        #            3) Progress bar sa kompletiranim aktivnostima
        #            4) Customizovan comment box
        #         II.Sledece akcije:
        #            1)Student hoce da vidi detalje svog profila
        #            2)Student hoce da ukuca komentar
        #              i)Student kuca komentar i pritiska post ili Enter
        #                 a)Student nije ukucao nista - disejblovano post dugme
        #                 b)I kad pritisne enter mu izadje greska
        #              ii)Student primecuje da je njegov komentar dodat
        #            3)Student hoce da uradi aktivnost
        #              i) Student bira jednu od aktivnosti iz bilo kog modula
        #              ii) Browser ode na stranicu aktivnosti








# class ViewTests(TestCase):
    
#     def test_index_returns_correct_html(self):
#         request = HttpRequest
        
# class MySeleniumTests(LiveServerTestCase):
#     fixtures = ['user-data.json']

#     @classmethod
#     def setUpClass(cls):
#         cls.selenium = WebDriver()
#         super(MySeleniumTests,cls).setUpClass()

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super(MySeleniumTests,cls).tearDownClass()


    # def test_test(self):
    #     from time import sleep
    #     self.selenium.get('%s%s' % (self.live_server_url,'/tt/'))
    #     sleep(4)
    #     username_input = self.selenium.find_element_by_name("username")
    #     username_input.send_keys("john")
    #     username_input = self.selenium.find_element_by_name("password")
    #     username_input.send_keys("john")
    #     self.selenium.find_element_by_css_selector("input[type=submit]").click()
        
