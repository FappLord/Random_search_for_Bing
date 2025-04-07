from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time


def generate_random_search_term(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def setup_edge_driver():
    # Tạo options cho Edge
    edge_options = Options()
    edge_options.add_argument("start-maximized")

    try:
        driver = webdriver.Edge(options=edge_options)
    except:
        edge_driver_path = "PATH_TO_YOUR_EDGE_WEBDRIVER\\msedgedriver.exe"
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service, options=edge_options)

    return driver


def perform_bing_searches(num_searches=30, delay_seconds=6):
    driver = setup_edge_driver()

    try:
        # Mở trang Bing
        driver.get("https://www.bing.com/")

        # Đợi trang tải xong
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        print(f"Bắt đầu {num_searches} lần tìm kiếm...")

        # Thực hiện tìm kiếm nhiều lần
        for i in range(num_searches):
            # Tạo từ khóa tìm kiếm ngẫu nhiên với độ dài ngẫu nhiên từ 3-10 ký tự
            search_term = generate_random_search_term(random.randint(3, 10))
            print(f"Search {i + 1}/{num_searches}: '{search_term}'")

            # Tìm hộp tìm kiếm và nhập từ khóa
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys(search_term)
            search_box.send_keys(Keys.RETURN)

            # Đợi kết quả tìm kiếm hiển thị
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "b_results"))
            )

            # Đợi theo thời gian được chỉ định
            time.sleep(delay_seconds)

    except Exception as e:
        print(f"Lỗi: {e}")

    finally:
        # Đóng trình duyệt sau khi hoàn thành
        print("Done!")


def main():
    perform_bing_searches(30, 6)


if __name__ == "__main__":
    main()