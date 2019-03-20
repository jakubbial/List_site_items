from selenium import webdriver


def open_browser(browser, web_page="None"):
    try:
        if browser == "firefox":
            handler = webdriver.Firefox()
        elif browser == "chrome":
            handler = webdriver.Chrome()
    except Exception as e:
        print(e)
        return 0

    if web_page != "None":
        handler.get(web_page)

    return handler


def kill_browser(handler):
    handler.close()


def close_rodo(handler):
    rodo_popup = '/html/body/div[4]/div[15]/div/div/a'
    # rodo button xpath for main page:
    # rodo_popup = '/html/body/div[3]/div[12]/div/div/a'

    rodo_button = handler.find_element_by_xpath(rodo_popup)
    rodo_button.click()


def read_object_value(handler, xpath):
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
        xpath_engine = xpath + '/div[2]/ul/li[4]/span'
        xpath_mileage = xpath + '/div[2]/ul/li[2]/span'


        try:
            title = handler.find_element_by_xpath(xpath_title).text
            price = handler.find_element_by_xpath(xpath_price).text
            year = handler.find_element_by_xpath(xpath_year).text
            engine = handler.find_element_by_xpath(xpath_engine).text
            mileage = handler.find_element_by_xpath(xpath_mileage).text
            print(title, ';', price, ';', year, ';', engine, ';', mileage)
        except Exception as e:
            print(e)


def click_button(handler, xpath):
    try:
        next_button = handler.find_element_by_xpath(xpath)
        next_button.click()
    except Exception as e:
        print(e)


def list_items(handler, number_of_subsites):
    number_of_items_on_site = 32
    next_butt_xpath1 = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[7]/a'
    next_butt_xpath2 = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[8]/a'
    next_butt_xpath3 = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[8]/a'
    next_butt_xpath4 = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[10]/a'

    for i in range(1, number_of_subsites):
        if i == 1:
            list_offers(handler, number_of_items_on_site)
            click_button(handler, next_butt_xpath1)

        if i == 2:
            list_offers(handler, number_of_items_on_site)
            click_button(handler, next_butt_xpath2)

        if i == 3:
            list_offers(handler, number_of_items_on_site)
            click_button(handler, next_butt_xpath3)

        if i >= 4:
            list_offers(handler, number_of_items_on_site)
            click_button(handler, next_butt_xpath4)
