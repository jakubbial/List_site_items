from selenium import webdriver


def open_browser(browser, web_page="None"):
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "explorer":
        driver = webdriver.ie()

    if web_page != "None":
        driver.get(web_page)

    return driver


def kill_browser(handler):
    handler.close()


def close_rodo(handler):
    rodo_popup = '/html/body/div[3]/div[12]/div/div/a'
    rodo_guzior = handler.find_element_by_xpath(rodo_popup)
    rodo_guzior.click()


def fulfill_indicator(handler, xpath, value):
    try:
        lower_price = handler.find_element_by_xpath(xpath[0])
        lower_price.click()
    except Exception as e:
        print(e)

    try:
        lower_price2 = handler.find_element_by_xpath(xpath[1])
        lower_price2.send_keys(value)
    except Exception as e:
        print(e)


def click_button(handler, xpath):
    try:
        button = handler.find_element_by_xpath(xpath)
        button.click()
    except Exception as e:
        print(e)


low_price_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[4]/span[1]/span[1]/span',
                   '/html/body/span/span/span[1]/input']
low_price_value = "5000"

high_price_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[4]/span[2]/span[1]/span',
                    '/html/body/span/span/span[1]/input']
high_price_value = "10000"

yr_of_prod_from_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[5]/span[1]/span[1]/span',
                         '/html/body/span/span/span[1]/input']
yr_of_prod_from_value = "2008"

yr_of_prod_to_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[5]/span[2]/span[1]/span',
                       '/html/body/span/span/span[1]/input']
yr_of_prod_to_value = "2015"

button_xpath = '/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/button[1]'

web_browser_handler = open_browser("firefox", "http://www.otomoto.pl")

close_rodo(web_browser_handler)
fulfill_indicator(web_browser_handler, low_price_xpath, low_price_value)
fulfill_indicator(web_browser_handler, high_price_xpath, high_price_value)
fulfill_indicator(web_browser_handler, yr_of_prod_from_xpath, yr_of_prod_from_value)
fulfill_indicator(web_browser_handler, yr_of_prod_to_xpath, yr_of_prod_to_value)
click_button(web_browser_handler, button_xpath)

#kill_browser(web_browser_handler)
