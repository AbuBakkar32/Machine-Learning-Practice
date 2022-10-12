try:
    import time
    from autoscraper import AutoScraper
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
except Exception as e:
    print("Some modules are missing {}".format(e))

options = Options()
options.add_argument("user-data-dir=C:/Users/ASL/AppData/Local/Google/Chrome/User Data/Default")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(service=Service("F:/software/Machine-Learning-Practice/Automation/driver/chromedriver.exe"),
                          options=options)
driver.maximize_window()

# Open the URL you want to execute JS
url = 'https://stake.com/casino/games/evolution-stake-exclusive-roulette-1'
driver.get(url)
time.sleep(5)

# It is switching to second tab now
driver.execute_script("window.open('about:blank', 'secondtab')")
driver.switch_to.window("secondtab")

url = 'https://babylonstk.evo-games.com/frontend/evo/r2/#category=roulette'
driver.get(url)
time.sleep(900000)

# data = driver.find_element(By.CLASS_NAME, 'notranslate desktop en SmartLobby--34c4e')
# print(data)


# url = 'https://babylonstk.evo-games.com/frontend/evo/r2/#category=roulette&game=roulette'
# scraper = AutoScraper()
# get the HTML from the site
# result = scraper.build(url, ['USA', '98,555,072', '1,087,880', '95,729,329', '1,737,863', '2,609', '294,365', '3,249',
#                              '1,121,944,996', '3,351,037', '334,805,269'])
