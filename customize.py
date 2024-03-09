from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import sys
import os
import names

chrome_driver_path = './chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location =r"C:\Program Files\Google\Chrome\Application\chrome.exe"

chrome_options.add_argument("webdriver.chrome.driver=" + chrome_driver_path)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header'

def gerar_nome():
    with open('nomes.txt', 'r') as f:
        nomes = f.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista

    nome_aleatorio = random.choice(nomes).strip()  # Remove qualquer espaço em branco ou nova linha
    
    return nome_aleatorio

def trocarnomefoto():
    driver.find_element(By.XPATH, '//*[@id="account_pulldown"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[1]').click()
    sleep(5)
    try:
        driver.find_element(By.XPATH, '//*[@id="btn"]/a/span').click()
    except:
        driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[3]/div[2]/a/span').click()   
    sleep(5)
    name = names.get_full_name()
    nome = driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[2]/form/div[3]/div[2]/div[1]/label/div[2]/input')
    nome.clear()
    nome.send_keys(name)
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[2]/form/div[7]/button[1]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[1]/a[2]').click()
    sleep(5)
    numero = random.randint(1, 4)
    if numero == 1: 
        driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[2]/div/div[1]/div[4]/div[2]/div/div[1]/img').click()
    if numero == 2:
        driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[2]/div/div[1]/div[4]/div[2]/div/div[3]/img').click()
    if numero == 3:
        driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[2]/div/div[1]/div[4]/div[2]/div/div[5]/img').click()
    if numero == 4:
        driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[2]/div/div[1]/div[4]/div[2]/div/div[7]/img').click()

    # //*[@id="react_root"]/div[3]/div[2]/div/div[1]/div[4]/div[3]/button (Ver todos)
    
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="react_root"]/div[3]/div[2]/div/div[2]/button[1]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="account_pulldown"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[4]').click()
    
 
    
# Função para fazer login com as credenciais fornecidas
def fazer_login(usuario, senha):
    sleep(5)
    driver.get(url)
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input').send_keys(usuario)
    driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input').send_keys(senha)
    driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button').click()
    sleep(5)  # Aguarda a página carregar
    trocarnomefoto()

# Função para ler as credenciais do arquivo .txt e fazer login com cada uma delas
def fazer_login_com_credenciais(arquivo):
    with open(arquivo, 'r') as f:
        for linha in f:
            # Divide a linha do arquivo em login e senha, usando ':' como separador
            credenciais = linha.strip().split(':')

            # Pega apenas a primeira parte da string como login e a segunda parte como senha
            usuario = credenciais[0]
            senha = credenciais[1].split(' ')[0]  # Ignora qualquer informação adicional após o espaço

            # Faz login com as credenciais
            fazer_login(usuario, senha)

# Arquivo .txt contendo as credenciais
arquivo_credenciais = 'contas.txt'

# Faz login com as credenciais do arquivo .txt
fazer_login_com_credenciais(arquivo_credenciais)