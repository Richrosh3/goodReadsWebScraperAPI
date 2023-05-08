from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_reviews():

    # IMPORTANT: Replace your username and password here
    username = "username"
    password = "password"

    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    driver.get("https://www.goodreads.com/ap/signin?language=en_US&openid.assoc_handle=amzn_goodreads_web_na&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.goodreads.com%2Fap-handler%2Fsign-in&siteState=09339b8d7589f52fec5fc8c86b72d0cf")
    driver.find_element(By.ID, "ap_email").send_keys(username)
    driver.find_element(By.ID, "ap_password").send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()

    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    # IMPORTANT: Insert your own personal read shelf url from GoodReads
    driver.get("https://www.goodreads.com/review/list/users_read_shelf")

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "bookalike.review")))
    books = driver.find_elements(By.CLASS_NAME, "bookalike.review")

    review_dict = {}

    for book in books:
        title = book.find_element(By.CLASS_NAME, "field.title").text.strip()
        author = book.find_element(By.CLASS_NAME, "field.author").text.strip()
        rating = book.find_element(By.CLASS_NAME, "field.rating").find_element(By.CLASS_NAME, "value").get_attribute("innerText")
        review = book.find_element(By.CLASS_NAME, "field.review").find_element(By.CSS_SELECTOR, "[id^='freeTextreview']").get_attribute("innerText")
        dateStart = book.find_element(By.CLASS_NAME, "field.date_started").get_attribute("innerText").replace("\n", "").replace("date started", "").strip()
        dateFinish = book.find_element(By.CLASS_NAME, "field.date_read").text

        review_dict[title] = {"author": author, "rating": rating, "review": review, "dateStart": dateStart, "dateFinish": dateFinish}


    driver.quit()

    # print("review_dict")

    return(review_dict)

# scrape_reviews()