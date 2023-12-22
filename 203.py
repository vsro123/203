from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time
import threading
from selenium.webdriver.firefox.options import Options

# Tạo chuỗi ngẫu nhiên với chữ và số
def random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    while True:
        result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
        if (any(c.isalpha() for c in result_str) and any(c.isdigit() for c in result_str)):
            return result_str

# Tạo số điện thoại ngẫu nhiên
def random_phone():
    return '0' + ''.join(random.choice(string.digits) for _ in range(9))

# Hàm đăng ký tài khoản
def register_account():
    # Khởi tạo trình duyệt
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    # Lấy thời gian bắt đầu
    start_time = time.time()

    # Thời gian tự động ngưng chạy (tính bằng giây)
    auto_stop_time = 3600  # Thay đổi thời gian này theo yêu cầu của bạn

    # Khởi tạo biến đếm
    success_count = 0

    while True:
        # Kiểm tra thời gian đã trôi qua
        elapsed_time = time.time() - start_time
        if elapsed_time > auto_stop_time:
            print("Đã đạt đến thời gian tự động ngưng chạy. Dừng chương trình.")
            break

        username = random_string(10)
        email = username + "@example.com"
        Password = random_string(10)
        password2 = random_string(10)
        phone = random_phone()

        # Truy cập trang đăng ký
        driver.get('http://203.86.232.68/index2.php?mod=register')
        
        # Đợi một lúc trước khi bắt đầu đăng ký
        time.sleep(0.1)  # Thêm thời gian chờ ở đây   
        # Tìm và điền thông tin vào các trường
        username_field = driver.find_element(By.NAME, 'username')
        username_field.send_keys(username)

        email_field = driver.find_element(By.NAME, 'sdt')
        email_field.send_keys(phone)

        password1_field = driver.find_element(By.NAME, 'password')
        password1_field.send_keys(Password)

        password1_repeat_field = driver.find_element(By.NAME, 'repassword')
        password1_repeat_field.send_keys(Password)

        password2_field = driver.find_element(By.NAME, 'password2')
        password2_field.send_keys(password2)
        
        password1_repeat_field = driver.find_element(By.NAME, 'repassword2')
        password1_repeat_field.send_keys(password2)
        
        phone_field = driver.find_element(By.NAME, 'email')
        phone_field.send_keys(email)

        # Nhấn nút đăng ký
        register_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
        register_button.click()

        # Kiểm tra đăng ký thành công
        try:
            success_message = driver.find_element(By.XPATH, '//font[@color="green"]')  # Thay đổi XPath này để khớp với thông báo thành công trên trang web của bạn
            print("Đăng ký thành công: ", success_message.text)
            success_count += 1
            print("Số lượng tài khoản đã đăng ký thành công: ", success_count)
        except:
            print("Đăng ký không thành công")

        # Đợi một lúc trước khi đăng ký tài khoản tiếp theo
        time.sleep(0.2)  # Thay đổi thời gian chờ ở đây

    driver.quit()

# Số lượng trình duyệt đăng ký cùng lúc
num_browsers = 2  # Thay đổi số lượng này theo yêu cầu của bạn

# Tạo và khởi động các luồng
for _ in range(num_browsers):
    threading.Thread(target=register_account).start()
