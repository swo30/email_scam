from selenium import webdriver
import json
import random
import threading

num_threads = 5


def do_request():
    while True:
        rand = random.randint(0, 49)
        with open('last_names.txt') as f:
            last_name = f.readlines()[rand].strip('\n')

        rand = random.randint(0, 99)
        with open('first_names.txt') as f:
            first_name = f.readlines()[rand].strip('\n')

        with open('common-passwords.json') as f:
            passwords_list = json.loads(f.readlines()[0])
            rand = random.randint(0, len(passwords_list)) - 1
            password = passwords_list[rand]

        url = 'https://hot1mail.weebly.com/'
        driver = webdriver.Chrome(
            executable_path='/media/simon/Hard Drive/Users/Simon/Downloads/Programming/Random/hotmail_scam/chromedriver')
        driver.get(url)

        email_field = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[3]/form/div[1]/ul/div[1]/div/div[1]/input')
        password_field = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[3]/form/div[1]/ul/div[2]/div/div[1]/input')
        rand_email = random.randint(1969, 2000)

        separator = [".", "-", "_"]
        email_service = ["gmail.com", "yahoo.com", "sympatico.com", "hotmail.com", "outlook.com"]
        rand_separator = random.randint(0, 2)
        rand_service = random.randint(0, 4)
        email_address = f"{first_name.lower()}{separator[rand_separator]}{last_name.lower()}{rand_email}@{email_service[rand_service]}"
        email_field.send_keys(email_address)
        password_field.send_keys(f"{password}{random.randint(3, 99)}")

        driver.find_element_by_xpath('//*[@id="form-659144235420711208"]/div[3]/a').click()
        driver.close()


threads = []
for i in range(num_threads):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(num_threads):
    threads[i].start()

for i in range(num_threads):
    threads[i].join()
