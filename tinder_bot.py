from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"

class TinderBot():
    def __init__(self, usr: str, psw: str):
        self.username, self.password = usr, psw
        self.cont = True
        options = webdriver.ChromeOptions()
        #options = Options()
        options.add_argument("start-minimized")
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
    # self = TinderBot()
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        p_max = '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
        #p_min = '//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]'
        login_btn = self.driver.find_element(p_max)
        login_btn.click()
        sleep(2)

        fb_button = self.driver.find_element('//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_button.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(2)

        email_in = self.driver.find_element('//*[@id="email"]')
        email_in.send_keys(self.username)

        psd = self.driver.find_element('//*[@id="pass"]')
        psd.send_keys(self.password)

        fb_login_btn = self.driver.find_element('//*[@id="loginbutton"]')
        fb_login_btn.click()

        sleep(1)
        self.driver.switch_to.window(base_window)
        sleep(5)

        allow_btn = self.driver.find_element('//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]')
        allow_btn.click()
        sleep(2)

        notint_btn = self.driver.find_element('//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[2]')
        notint_btn.click()
        sleep(5)

        accept_btn = self.driver.find_element('//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button')
        accept_btn.click()

    def like1(self):
        while True:
            try:
                like_btn = self.driver.find_element('//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
                like_btn.click()
                break
            except:
                sleep(5)


    def like2(self):
        while True:
            sleep(2)
            try:
                lk2 = self.driver.find_element('//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
                lk2.click()
                break
            except:
                try:
                    not_int_btn = self.driver.find_element('//*[@id="o-1335420887"]/div/div/div[2]/button[1]')
                    not_int_btn.click()
                except:
                    try:
                        no_tx_btn = self.driver.find_element_('//*[@id="o-1335420887"]/div/div/button[1]')
                        no_tx_btn.click()
                    except:
                        try:
                            no_tx2 = self.driver.find_element('//*[@id="o-1335420887"]/div/div/button[2]')
                            no_tx2.click()
                        except:
                            try:
                                self.driver.find_element('//*[@id="o-1335420887"]/div/div/div[3]/button[2]').click()
                            except:
                                sleep(5)

    def autoswipe(self):
        self.like1()
        while self.cont:
            self.like2()

if __name__ == '__main__':
    user=input("Introduce your username: ")
    password=input("Introduce your password: ")
    self = TinderBot(user, password)
    self.login()
    self.autoswipe()
