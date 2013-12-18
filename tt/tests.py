from django.test import TestCase
from django.test import LiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver
from views import index
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_tt_url_resolvers_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func,index)

    def test_index_page_returns_correct_url(self):
        request = HttpRequest()
        request.method = 'GET'
        response = index(request)
        expected_html = render_to_string('index.djhtml')
        # convert response.content bytes to python unicode string
        self.assertEqual(response.content.decode(),expected_html)
        
       
        self.assertIn(b'<title>Programski prevodioci</title>',response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        

        
        
        
class NewVisitorTest(TestCase):
    
    def setUp(self):
                    
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_login(self):
        # Student hoce da pristupi kursu 'Programski Prevodioci' i svom
        # profilu, pa ode na homepage
        
        self.browser.get('http://localhost:8000/')
        # Primecuje rec Programski prevodioci u title-u
        self.assertIn("Programski prevodioci",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Programski prevodioci",header_text)
        
        
        
        # 1. Nije ulogovan i zeli da se uloguje
        #    a) Vidi login formular sa desne strane
        username_input = self.browser.find_element_by_css_selector('input[name=username]')
        
        password_input = self.browser.find_element_by_css_selector('input[name=password]')
        #self.assertEqual(username_input.get_attribute('placeholder'),"Unesite vasu lozinku...")
        #    b) Kuca username i password
        username_input.send_keys("john")
        password_input.send_keys("john")
        #    c) Pritiska submit dugme ili kucka Enter
        self.browser.find_element_by_css_selector("input[name=login-submit]").click()
        #password_input.send_keys(Keys.ENTER)
        #    d) i. Pogresan login - stranica updejtovana sa error messages
        # Proveri da li su se stvorili error tagovi
        #       ii.Uspesan login - stranica updejtovana i sada je customizovana za studenta
        #          I. Student primecuje:
        #            1)U title se pojavljuje ime studenta
        #            2) Navbar sadrzi njegovu sliku i notifikacije, i mozda jos nesto
        #            3) Progress bar sa kompletiranim aktivnostima
        #            4) Customizovan comment box
        comment_input_box = self.browser.find_element_by_css_selector('.comment-placeholder')
        self.assertEqual(comment_input_box.get_attribute('placeholder'),'Write a comment...')
        #         II.Sledece akcije:
        #            1)Student hoce da vidi detalje svog profila
        #            2)Student hoce da ukuca komentar
        #              i)Student kuca komentar i prit        iska post ili Enter
        time.sleep(3)
        comment_input_box.send_keys("Dobar dan svima!")
        self.browser.find_element_by_css_selector("input[name=comment-submit]").click()
        time.sleep(3)
        comment = self.browser.find_element_by_css_selector("div.comment-container:first-child p:nth-of-type(2)")

        self.assertEqual("Dobar dan svima!",comment.text)
        
        #                 a)Student nije ukucao nista - disejblovano post dugme
        #                 b)I kad pritisne enter mu izadje greska
        #              ii)Student primecuje da je njegov komentar dodat
        #            3)Student hoce da uradi aktivnost
        #              i) Student bira jednu od aktivnosti iz bilo kog modula
        #              ii) Browser ode na stranicu aktivnosti
        self.fail("Finish writting tests!")








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
        
