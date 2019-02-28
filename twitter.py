from selenium import webdriver
import time
def readurl():
    f = open('./twitterurl.txt')
    while True:
        line = f.readline()
        if not line: break
        driver.get(line)
        time.sleep(3)
        try:
            try:
                try:
                    try:
                        driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[6]/div/div/span[2]/button[1]').click()
                    except:
                        driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[7]/div/div/span[2]/button[1]').click()
                except:
                    driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[5]/div/div/span[2]/button[1]').click()
            except:
                driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[4]/div/div/span[2]/button[1]').click()
        except:
            continue
    f.close()
    driver.quit()
    exit()

def except_login(twitter_id,twitter_pw):
    while True:
        if str(twitter_id).find('@') !=-1:
            split_id = str(twitter_id).split('@')[0]
            split_email = '%40'+str(twitter_id).split('@')[1]
        else:
            split_id = str(twitter_id)
            split_email = ''
        driver.get('https://twitter.com/login/error?username_or_email='+split_id+split_email)
        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(twitter_pw)
        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
        time.sleep(1)
        if driver.current_url == "https://twitter.com/":
            readurl()
        else:
            twitter_id = input("트위터 아이디를 입력하세요 : ")
            twitter_pw = input("트위터 비밀번호를 입력하세요 : ")
            except_login(twitter_id,twitter_pw)

def first_login(twitter_id,twitter_pw):
    while True:
        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys(twitter_id)
        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(twitter_pw)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
        time.sleep(2)
        if driver.current_url == "https://twitter.com":
            break
        else:
            twitter_id = input("트위터 아이디를 입력하세요 : ")
            twitter_pw = input("트위터 비밀번호를 입력하세요 : ")
            except_login(twitter_id,twitter_pw)

twitter_id = input("트위터 아이디를 입력하세요 : ")
twitter_pw = input("트위터 비밀번호를 입력하세요 : ")
driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://twitter.com/login') #트위터 로그인을 위한 메인화면 노출

first_login(twitter_id,twitter_pw)

