from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

navegador = Chrome()
navegador.get("https://consultacnpj.com/cnpj/")
navegador.maximize_window()

cnpjs = ["45997418000153", "72273196001090", "33000167000101"]

for cnpj in cnpjs:
    input = navegador.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div/div/div[2]/div/div/input')
    input.clear()
    input.send_keys(cnpj)
    t.sleep(5)
    texto = navegador.find_element_by_xpath('//*[@id="company-data"]')
    with open(f'{str(cnpj)}.csv', 'w', encoding="UTF-8") as csv:
        csv.write(texto.text)
    t.sleep(2)

navegador.quit()


