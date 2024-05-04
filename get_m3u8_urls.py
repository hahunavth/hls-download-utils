from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_urls():
    return [f"https://www.phimmoivl.net/xem-phim/cay-tao-no-hoa-tap-{i}" for i in range(40, 72)]


urls = get_urls()

options = Options()
options.binary_location = "chrome-linux64/chrome"
driver = webdriver.Chrome(chrome_options=options,
                          executable_path="chromedriver-linux64/chromedriver")

with open("urls2.txt", "w") as f:
    for url in urls:
        print(url)
        driver.get(url)
        driver.implicitly_wait(5)
        title = driver.title
        iframe = driver.find_element(
            By.XPATH, "//iframe[contains(@src, 'm3u8')]")
        src = iframe.get_attribute("src")
        print(f"{title},{src}")
        f.write(f"{title},{src}" + "\n")
