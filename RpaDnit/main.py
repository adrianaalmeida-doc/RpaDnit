import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    # Inicializa o WebDriver 
    driver = webdriver.Chrome()

    # URL do site
    url = "https://servicos.dnit.gov.br/multas/"

    # Abre a página
    driver.get(url) 

    # Aguarda o carregamento da página
    time.sleep(5)

    # Preenche os campos
    driver.findElement(By.xpath(""))
    placa_input = driver.find_element(By.xpath ("placa"))
    renavam_input = driver.find_element(By.NAME, "renavam")

    placa_input.send_keys("ABC1234")  # Substituir
    renavam_input.send_keys("12345678901")  # Substituir

    # Submete o formulário
    renavam_input.send_keys(Keys.RETURN)

    # Aguarda o resultado ser carregado
    time.sleep(5)

    # Coleta os dados da tabela de resultados usando Pandas
    table = driver.find_element(By.ID, "tabela")
    df = pd.read_html(table.get_attribute('outerHTML'))[0]

    # Imprime o DataFrame com os dados
    print(df) 

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    # Fecha o navegador
    if 'driver' in locals():
        driver.quit()
