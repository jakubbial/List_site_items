import Site_objects_functions


webpage = "https://www.otomoto.pl/osobowe/od-2008/?search%5Bfilter_float_price%3Afrom%5D=5000&search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_float_year%3Ato%5D=2015&search%5Bnew_used%5D=on"
number_of_all_subsites_xpath = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[6]'


web_browser_handler = Site_objects_functions.open_browser("firefox", webpage)
Site_objects_functions.close_rodo(web_browser_handler)
Site_objects_functions.list_items(web_browser_handler, 2)
Site_objects_functions.kill_browser(web_browser_handler)
