from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

def login(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
    time.sleep(10)

def get_followers(username):
    driver.get(f"https://www.instagram.com/{username}/followers/")
    time.sleep(5)  # Garante que o popup carregue
    print(driver.page_source)  # Mostra o HTML da página
    time.sleep(5)
    scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(5)
        ht = driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight; return arguments[0].scrollHeight;", scroll_box)
    
    followers = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, "._ap3a") if elem.text]
    return followers

# Exemplo de uso
username = "arielsantos074"
password = "ARiel18@#"
login(username, password)
followers_list = get_followers(username)
print(followers_list)

driver.quit()
