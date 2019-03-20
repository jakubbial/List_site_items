import Site_objects_functions


webpage = "https://www.otomoto.pl/osobowe/skoda/superb/ii-2008/?search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_no_accident%5D=1&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D="
number_of_all_subsites_xpath = '/html/body/div[4]/div[2]/section/div[2]/div[2]/ul/li[6]'

web_browser_handler = Site_objects_functions.open_browser("firefox", webpage)


Site_objects_functions.close_rodo(web_browser_handler)
number_of_subsites = Site_objects_functions.read_object_value(web_browser_handler, number_of_all_subsites_xpath)
print('Number of Subsites: ' + number_of_subsites)

Site_objects_functions.list_items(web_browser_handler, int(number_of_subsites))
Site_objects_functions.kill_browser(web_browser_handler)
