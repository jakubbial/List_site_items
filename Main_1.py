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


# def kill_browser(handler):
#     handler.close()
#

def close_rodo(handler):
    rodo_popup = '/html/body/div[4]/div[15]/div/div/a'
    #rodo_popup = '/html/body/div[3]/div[12]/div/div/a'
    rodo_guzior = handler.find_element_by_xpath(rodo_popup)
    rodo_guzior.click()

#
# def fulfill_indicator(handler, xpath, value):
#     try:
#         lower_price = handler.find_element_by_xpath(xpath[0])
#         lower_price.click()
#     except Exception as e:
#         print(e)
#
#     try:
#         lower_price2 = handler.find_element_by_xpath(xpath[1])
#         lower_price2.send_keys(value)
#     except Exception as e:
#         print(e)
#
#
# def click_button(handler, xpath):
#     try:
#         button = handler.find_element_by_xpath(xpath)
#         button.click()
#     except Exception as e:
#         print(e)
#
#
# low_price_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[4]/span[1]/span[1]/span',
#                    '/html/body/span/span/span[1]/input']
# low_price_value = "5000"
#
# high_price_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[4]/span[2]/span[1]/span',
#                     '/html/body/span/span/span[1]/input']
# high_price_value = "10000"
#
# yr_of_prod_from_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[5]/span[1]/span[1]/span',
#                          '/html/body/span/span/span[1]/input']
# yr_of_prod_from_value = "2008"
#
# yr_of_prod_to_xpath = ['/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/div[5]/span[2]/span[1]/span',
#                        '/html/body/span/span/span[1]/input']
# yr_of_prod_to_value = "2015"
#
# button_xpath = '/html/body/div[3]/main/div[2]/div/div[1]/div[2]/ul/li[1]/form/button[1]'


def read_value(handler, xpath):
    try:
        text_find = handler.find_element_by_xpath(xpath)
        output_text = text_find.text
        return output_text
    except Exception as e:
        print("Error:")
        print(e)


def list_offers(handler, number_of_offers):
    xpath_base = '/html/body/div[4]/div[2]/section/div[2]/div[1]/div/div[1]/div[5]/article'
    for i in range(1, number_of_offers+1):
        xpath = xpath_base + '[' + str(i) + ']'
        xpath_title = xpath + '/div[2]/div[1]/h2'
        xpath_price = xpath + '/div[2]/div[2]/div/span[1]'
        xpath_year = xpath + '/div[2]/ul/li[1]'

        try:
            title = handler.find_element_by_xpath(xpath_title).text
            price = handler.find_element_by_xpath(xpath_price).text
            year = handler.find_element_by_xpath(xpath_year).text
            print(title, ' ', price, ' ', year)
        except Exception as e:
            print(e)


def next_page(handler, xpath):
    try:
        next_button = handler.find_element_by_xpath(xpath)
        next_button.click()
    except Exception as e:
        print(e)


list_length = 32
number_of_subsites_xpath = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[6]'
webpage = "https://www.otomoto.pl/osobowe/od-2008/?search%5Bfilter_float_price%3Afrom%5D=5000&search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_float_year%3Ato%5D=2015&search%5Bnew_used%5D=on"

web_browser_handler = open_browser("firefox", webpage)
close_rodo(web_browser_handler)

next_butt_xpath1 = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[7]/a'
next_butt_xpath2 = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[8]/a'
next_butt_xpath3 = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[10]/a'

list_offers(web_browser_handler, list_length)
next_page(web_browser_handler, next_butt_xpath1)

list_offers(web_browser_handler, list_length)
next_page(web_browser_handler, next_butt_xpath2)

list_offers(web_browser_handler, list_length)
next_page(web_browser_handler, next_butt_xpath2)

for i in range (0, 10):
    list_offers(web_browser_handler, list_length)
    next_page(web_browser_handler, next_butt_xpath3)


# fulfill_indicator(web_browser_handler, low_price_xpath, low_price_value)
# fulfill_indicator(web_browser_handler, high_price_xpath, high_price_value)
# fulfill_indicator(web_browser_handler, yr_of_prod_from_xpath, yr_of_prod_from_value)
# fulfill_indicator(web_browser_handler, yr_of_prod_to_xpath, yr_of_prod_to_value)
# click_button(web_browser_handler, button_xpath)
# kill_browser(web_browser_handler)

# 3 /html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[8]/a
# 4 /html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[10]/a
