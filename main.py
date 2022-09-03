from time import sleep
from gmail import sendEmail
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

def website():
        urlInvesting = "https://br.investing.com/economic-calendar/"
        driver.get(urlInvesting)
        counter = 1
        counter_news = 0
        dic1 = {}
        delay = 3
        try:
            sleep(5)
            news = driver.find_elements(By.XPATH, '/html/body/div[5]/section/div[6]/table/tbody/tr/td[3]')
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        for new in news:
            level = new.get_attribute("title")
            counter += 1
            if level == "Volatilid. Esperada Alta": # It's mean high volatility in Portuguese
                time = driver.find_element(By.XPATH, f'/html/body/div[5]/section/div[6]/table/tbody/tr[{counter}]/td[1]').text
                currency = driver.find_element(By.XPATH, f'/html/body/div[5]/section/div[6]/table/tbody/tr[{counter}]/td[2]')
                event = driver.find_element(By.XPATH, f'/html/body/div[5]/section/div[6]/table/tbody/tr[{counter}]/td[4]/a')
                dic3 = {"time":time, "currency":currency.text,"event": event.text}
                dic2 = {f"{counter_news}": dic3}
                dic1.update(dic2)
                counter_news += 1
        sendEmail(dic1, counter_news)
website() 



