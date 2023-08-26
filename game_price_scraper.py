from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd

Pesquina = input("Digite um titulo ")
#Define a variavel como sendo uma pagina de Edge
preco_steam_texto = " "
edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')

browser = wd.Edge(options=edge_options) #options=edge_options

def steam():
  

  global nome_jogo
  global preco_steam_texto
  #Abre o link
  browser.get('https://store.steampowered.com/')
  #encontra o elemento do site pelo id htlm
  pesquisa_steam = browser.find_element('id','store_nav_search_term')
  pesquisa_steam.send_keys(Pesquina)
  sleep(3)
  try:
   #pesquisa_steam.send_keys(Keys.DOWN)
   #pesquisa_steam.send_keys(Keys.ENTER)
   preco_steam = browser.find_element('class name', 'match_subtitle')
   nome_steam= browser.find_element('class name', 'match_name ')
   nome_jogo= nome_steam.text
   preco_steam_texto = preco_steam.text
  except:
    preco_steam_texto == "Ausente"
def microsoft_store():
  global nome_microsoft_texto
  global preco_microsoft_texto
  browser.get('https://www.microsoft.com/pt-br/store/collections/pcgavtaz')
  botao_microsoft = browser.find_element('id', 'search')
  botao_microsoft.click()
  pesquisa_microsoft = browser.find_element('id', 'cli_shellHeaderSearchInput')
  try:
    pesquisa_microsoft.send_keys(nome_jogo)
    sleep(3)
  except: 
    pesquisa_microsoft.send_keys(Pesquina)
    sleep(3)
    # url_atual = browser.current_url
  (browser.find_element('class name', 'c-menu-item')).click()
  sleep(6)
  try:
      elemento_game_pass = browser.find_element('class name', 'high-contrast')
      preco_microsoft_texto = "29,99/mês (GamePass)"
  except:
    try:
      xpath = "//div[contains(@class, 'ProductDetailsHeader-module__showOnMobileView___uZ1Dz')]//span[contains(@class, 'Price-module__boldText___vmNHu')]"
      div_containing_span = browser.find_element('class name', 'ProductDetailsHeader-module__showOnMobileView___uZ1Dz')
      span = browser.find_element('xpath', xpath)
      preco_microsoft_texto = span.get_attribute('innerText')
    except:
        preco_microsoft_texto = "Ausente"

def GOG():
  global preco_GOG
  browser.get('https://www.gog.com/pt/games')
  xpath= '//*[@id="catalogHeader"]/search/form/input'
  pesquisa_GOG= browser.find_element('xpath', xpath)
  try:
    pesquisa_GOG.send_keys(nome_jogo)
    sleep(3)
  except: 
    pesquisa_GOG.send_keys(Pesquina)
    sleep(3)
  try:
    preco= browser.find_element('xpath', '//*[@id="Catalog"]/div/div[2]/paginated-products-grid/div/product-tile/a/div[2]/div[2]/div/product-price/price-value/span[1]')
    preco_GOG = preco.text
    sleep(3)
  except:
    preco_GOG = "Ausente"
  
def PSN():
  global preco_PSN
  browser.get('https://store.playstation.com/pt-br/pages/latest')
  (browser.find_element('class name', 'shared-nav-search-container')).click()
  pesquisa_PSN = browser.find_element('class name', 'search-text-box__input')
  try:
    pesquisa_PSN.send_keys(nome_jogo)
    sleep(3)
  except: 
    pesquisa_PSN.send_keys(Pesquina)
    sleep(3)
  (browser.find_element('xpath', '/html/body/div[7]/div/div/div/button[2]')).click()
  try:
    preco = browser.find_element('xpath', '//*[@id="main"]/section/div/ul/li[1]/div/a/div/section/div/div/span')
    preco_PSN = preco.text
  except:
    preco_PSN = "Ausente"
steam()
microsoft_store()
GOG()
PSN()
browser.quit()


Dados = pd.DataFrame({
  "Game name": [nome_jogo, " ", " ", " "],
  "Lojas": ["Steam", "Microsoft Store", "GOG", "Playstation Store"],
  "Preço": [preco_steam_texto, preco_microsoft_texto, preco_GOG, preco_PSN]
})
Tabela_dados = pd.DataFrame(Dados)
print(Tabela_dados)

