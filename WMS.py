import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import unittest
from GlobalLink import Data_WMS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WMS(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_addItems(self):
        driver = self.browser
        driver.get(Data_WMS.link)
        element1 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='sc-124al1g-2 bCLaRj']//button[@class='sc-124al1g-0 jCsgpZ'][normalize-space()='Add to cart']"))
        )
        element1.click()
        element2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='sc-124al1g-2 ddJZtb']//button[@class='sc-124al1g-0 jCsgpZ'][normalize-space()='Add to cart']"))
        )
        element2.click()
        driver.execute_script('scrollBy(0,650)')
        driver.find_element(
            By.XPATH, '//p[@class="sc-124al1g-4 eeXMBo" and text()="Black Batman T-shirt"]').is_enabled()
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, '//div[@class="sc-124al1g-2 dwOYCh"]//div[@class="sc-124al1g-3 bHJSNa" and text()="Free shipping"]'))
            )
            print("Data berhasil ditambahkan")
            time.sleep(2)
        except:
            print("Data tidak berhasil ditambahkan")

    def test_Add_Less_Amount(self):
        driver = self.browser
        driver.get(Data_WMS.link)
        element1 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='sc-124al1g-2 bCLaRj']//button[@class='sc-124al1g-0 jCsgpZ'][normalize-space()='Add to cart']"))
        )
        element1.click()
        plus_value = driver.find_element(
            By.XPATH, '//button[normalize-space()="+"]')
        min_value = driver.find_element(
            By.XPATH, '//button[normalize-space()="-"]')
        quantity = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//p[contains(@class,"sc-11uohgb-3 gKtloF")]'))
        )
        try:
            if "1" in quantity.text:
                print("Data hanya 1, lakukan penambahan...")
                for i in range(2, 5):
                    driver.execute_script(
                        "arguments[0].scrollIntoView", plus_value)
                    time.sleep(1)
                    plus_value.click()
                    time.sleep(2)
                driver.execute_script("arguments[0].scrollIntoView", min_value)
                time.sleep(2)
                min_value.click()
                update_quantity = driver.find_element(
                    By.XPATH, '//p[contains(@class,"sc-11uohgb-3 gKtloF")]').text
                if update_quantity == "1":
                    print("Data hanya ada 1, lakukan penambahan ulang")
                    for i in range(2, 5):
                        driver.execute_script("arguments[0].click", plus_value)
                        time.sleep(3)
                else:
                    print("Data sudah lebih dari 1")
                time.sleep(5)
                # checkout = WebDriverWait(driver, 5).until(
                #     EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-1h98xa9-11 gnXVNU']"))
                # )
                # checkout.click()
                checkOut = driver.find_element(
                    By.XPATH, "//button[@class='sc-1h98xa9-11 gnXVNU']")
                driver.execute_script(
                    "arguments[0].scrollIntoView();", checkOut)
                time.sleep(5)
                checkOut.click()
        except Exception as e:
            print("Terjadi kesalahan", str(e))

    def test_deleteItem(self):
        driver = self.browser
        driver.get(Data_WMS.link)
        element1 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='sc-124al1g-2 bCLaRj']//button[@class='sc-124al1g-0 jCsgpZ'][normalize-space()='Add to cart']"))
        )
        element1.click()
        element2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='sc-124al1g-2 ddJZtb']//button[@class='sc-124al1g-0 jCsgpZ'][normalize-space()='Add to cart']"))
        )
        element2.click()
        try:
            wait = WebDriverWait(driver, 5)
            elements = wait.until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "sc-11uohgb-5.gBQuHE"))
            )

            if not elements:
                print("Tidak ada data yang dihapus")
            else:
                for element in elements:
                    try:
                        wait.until(EC.element_to_be_clickable(element)).click()
                        print("Data berhasil dihapus")
                    except Exception as e:
                        print(f"Gagal menghapus data: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def test_selectSize(self):
        driver = self.browser
        driver.get(Data_WMS.link)
        size_options = ["XS", "S", "M", "ML", "L", "XL", "XXL"]
        for size in size_options:
            try:
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f'//span[text()="{size}"]'))
                ).click()
                print(f"Ukuran {size} berhasil diklik")
            except Exception as e:
                print(f"Gagal mengklik ukuran {size}: {e}")

    def test_visitGit(self):
        driver = self.browser
        driver.get(Data_WMS.link)
        element = driver.find_element(
            By.XPATH, "//*[name()='path' and contains(@d,'M0,0 L115,')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(driver).move_to_element(element).click().perform()
        if not element:
            print("Gagal mengunjungi Github")
        else:
            print("Berhasil mengunjungi Github")

    def tearDown(self):
        self.browser.quit()
