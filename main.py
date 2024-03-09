from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import sys
import os

# Define uma função para gerar um e-mail aleatório
def gerar_email():
    caracteres = string.ascii_lowercase + string.digits
    email = ''.join(random.choice(caracteres) for _ in range(12))
    return email

# Define uma função para gerar uma senha aleatória
def gerar_senha():
    caracteres = string.ascii_lowercase + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(12))
    return senha + 'SNK'

def gerar_nome():
    caracteres = string.ascii_lowercase + string.digits
    nome = ''.join(random.choice(caracteres) for _ in range (10))
    return nome

os.system('cls')
print('\n')
print('*' * 50)
print('snkdev - Starting...')
print('*' * 50)

# Define o caminho para o ChromeDriver
chrome_driver_path = './chromedriver.exe'

# Configura as opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Adiciona o caminho do ChromeDriver diretamente nas opções do Chrome
chrome_options.add_argument("webdriver.chrome.driver=" + chrome_driver_path)

# Inicializa o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Define a URL da página que deseja abrir
url = 'https://store.steampowered.com/join/'

while True:
    # Abre a página no navegador
    driver.get(url)

    # Tempo de 5 segundos antes de 
    sleep(5) 

    email = gerar_email()
    email_completo = email + '@tuamaeaquelaursa.com'

    # Encontra o campo de e-mail e envia o e-mail aleatório gerado
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email_completo)
    driver.find_element(By.XPATH, '//*[@id="reenter_email"]').send_keys(email_completo) # Colar o email na confirmacao de email
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i_agree_check"]').click() # Clica na confirmação de 13 anos

    # Aguarda sinal de que o procedimento deve ser continuado após realização do CAPTCHA
    input(' \n\n\n Pressione ENTER quando terminar de realizar o CAPTCHA... \n\n\n')

    driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()

    # Espera um tempo para a nova guia ser aberta
    sleep(2)


    # Executa um script JavaScript para abrir uma nova guia
    driver.execute_script("window.open('');")

    # Obtém todas as alças de janela abertas pelo driver
    janelas_abertas = driver.window_handles

    # Alterna para a nova guia (última na lista)
    driver.switch_to.window(janelas_abertas[-1])

    # Define a URL do site a ser navegado
    url_nova_aba = f'https://tuamaeaquelaursa.com/{email}'

    # Navega até a nova URL
    driver.get(url_nova_aba)

    sleep(8)

    driver.find_element(By.XPATH, '/html/body/div/section/div/div/div').click()
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/section/main/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a').click()
    sleep(5)

    # Obtém todas as alças de janela abertas pelo driver
    janelas_abertas = driver.window_handles

    # Fecha todas as abas, exceto a primeira
    for handle in janelas_abertas[1:]:
        driver.switch_to.window(handle)
        driver.close()

    # Alterna de volta para a primeira aba
    driver.switch_to.window(janelas_abertas[0])

    sleep(10)

    nome = gerar_nome()
    senha = gerar_senha()

    # Encontra o campo de usuario e cola o usuario gerado em gerar_nome()
    driver.find_element(By.XPATH, '//*[@id="accountname"]').send_keys(nome)
    sleep(2)

    # Encontra o campo de senha e cola a senha gerado em gerar_senha()
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)

    # Insere a senha na confirmação de senha
    driver.find_element(By.XPATH, '//*[@id="reenter_password"]').send_keys(senha)

    sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
    sleep(5)
    with open('contas.txt', 'a') as arquivo:
        # Escreve os dados da conta no arquivo
        arquivo.write(f'{nome}:{senha} >> {email_completo} \n')

