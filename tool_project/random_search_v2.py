from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import random
import string
import time


def generate_random_search_term(length=5):
    """Tạo một từ khóa tìm kiếm ngẫu nhiên."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def bing_search_with_chrome():
    """Sử dụng Chrome để thực hiện tìm kiếm Bing."""
    # Thiết lập Chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    # Thêm các tùy chọn để tránh phát hiện tự động hóa
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Khởi tạo driver
    driver = webdriver.Chrome(options=chrome_options)

    # Giả mạo thông tin navigator.webdriver
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

    try:
        # Truy cập Bing
        driver.get("https://www.bing.com/")

        # Thực hiện 30 lần tìm kiếm
        for i in range(30):
            try:
                # Đợi trang tải xong
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )

                # Tạo từ khóa tìm kiếm ngẫu nhiên
                search_term = generate_random_search_term(random.randint(3, 10))
                print(f"Search {i + 1}/30: '{search_term}'")

                # Xóa nội dung hiện tại trong thanh tìm kiếm
                search_box.clear()

                # Nhập từ khóa mới
                search_box.send_keys(search_term)
                search_box.send_keys(Keys.RETURN)

                # Đợi kết quả tìm kiếm hiển thị
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "b_results"))
                )

                # Đợi 5 giây trước khi tìm kiếm tiếp
                time.sleep(6)

            except WebDriverException as e:
                print(f"Lỗi trong quá trình tìm kiếm: {e}")
                # Thử truy cập lại Bing
                driver.get("https://www.bing.com/")
                time.sleep(2)

    except Exception as e:
        print(f"Lỗi: {e}")

    finally:
        print("Hoàn thành tất cả các tìm kiếm!")
        driver.quit()


def try_undetected_chrome():
    """Sử dụng undetected_chromedriver để tránh phát hiện."""
    try:
        # Cài đặt nếu chưa có: pip install undetected-chromedriver
        import undetected_chromedriver as uc

        # Khởi tạo undetected_chromedriver
        driver = uc.Chrome()
        driver.maximize_window()

        # Truy cập Bing
        driver.get("https://www.bing.com/")

        # Thực hiện 30 lần tìm kiếm
        for i in range(30):
            try:
                # Đợi trang tải xong
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )

                # Tạo từ khóa tìm kiếm ngẫu nhiên
                search_term = generate_random_search_term(random.randint(3, 10))
                print(f"Search {i + 1}/30: '{search_term}'")

                # Xóa nội dung hiện tại trong thanh tìm kiếm
                search_box.clear()

                # Nhập từ khóa mới
                search_box.send_keys(search_term)
                search_box.send_keys(Keys.RETURN)

                # Đợi kết quả tìm kiếm hiển thị
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "b_results"))
                )

                # Đợi 5 giây trước khi tìm kiếm tiếp
                time.sleep(5)

            except WebDriverException as e:
                print(f"Lỗi trong quá trình tìm kiếm: {e}")
                # Thử truy cập lại Bing
                driver.get("https://www.bing.com/")
                time.sleep(2)

    except ImportError:
        print("Bạn cần cài đặt undetected_chromedriver: pip install undetected-chromedriver")
        bing_search_with_chrome()  # Thử với Chrome thông thường nếu không có undetected_chromedriver

    except Exception as e:
        print(f"Lỗi: {e}")
        bing_search_with_chrome()  # Thử với Chrome thông thường nếu có lỗi

    finally:
        print("Hoàn thành tất cả các tìm kiếm!")
        try:
            driver.quit()
        except:
            pass


if __name__ == "__main__":
    print("Bắt đầu thực hiện tự động tìm kiếm Bing...")

    # Thử sử dụng undetected_chromedriver trước
    try:
        import undetected_chromedriver

        print("Sử dụng undetected_chromedriver...")
        try_undetected_chrome()
    except ImportError:
        # Sử dụng Chrome thông thường nếu không có undetected_chromedriver
        print("Sử dụng Chrome thông thường...")
        bing_search_with_chrome()