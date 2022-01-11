from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# Caminho para pasta onde se encotra o chromedriver
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    return browser

if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)
    browser.get('https://dados.gov.br/dataset/preco-de-medicamentos-no-brasil-consumidor')
    browser.maximize_window()
    sleep(2)
    browser.find_element(By.XPATH, '//*[@id="dataset-resources"]/ul/li[1]/div/a').click()
    sleep(1)
    browser.find_element(By.XPATH, '//*[@id="dataset-resources"]/ul/li[1]/div/ul/li[2]/a').click()
    sleep(20)
    browser.quit()

