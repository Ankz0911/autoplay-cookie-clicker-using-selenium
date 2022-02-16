# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# functions
def current_bank():
    current_money2 = driver.find_element_by_id("money")
    current_money2 = current_money2.text
    current_money = current_money2.replace(",", "")
    current_money = int(current_money)
    return current_money


def evaluate():
    global final_elements
    global final_values

    # preparing the list of elements
    final_elements = []
    final_values = []
    elements = driver.find_elements_by_css_selector("#store")
    elements_text = [element.text for element in elements]
    elements_text = [element.split("\n") for element in elements_text]
    elements_text = elements_text[0]

    # removing the integer value from the elements list
    final_exception_values = [str(item) for item in range(0, 50)]
    for element in elements_text:
        if element in final_exception_values:
            elements_text.remove(element)
        else:
            pass

    # slicing the required portions from elements_text
    elements_text = elements_text[::2]

    # finalising the list of elements and their values
    for element in elements_text:
        to_be_added = element.split("-")
        # preparing the final list of elements
        final_elements.append(to_be_added[0])

        # preparing the final list of their values
        to_be_added[1] = to_be_added[1].replace(",", "")
        final_values.append(int(to_be_added[1]))


def final_click(target_buying):
    click_element = driver.find_element_by_xpath(x_paths[target_buying])
    click_element.click()


# constants
x_paths = ['//*[@id="buyCursor"]', '//*[@id="buyGrandma"]', '//*[@id="buyFactory"]', '//*[@id="buyMine"]',
           '//*[''@id="buyShipment"]', '//*[@id="buyAlchemy lab"]', '//*[@id="buyPortal"]',
           '//*[@id="buyTime machine"]']

final_elements = []
final_values = []

# initialising the selenium driver
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# the final process
timer_min = 300
cookie_click = driver.find_element_by_id("cookie")
to_be_stopped = time.time() + timer_min
current_time = time.time()

while time.time() < to_be_stopped:
    cookie_click.click()
    timer_sec = 5
    to_be_stopped_2 = current_time + timer_sec
    evaluation_list = []
    if time.time() > to_be_stopped_2:
        money = current_bank()
        evaluate()
        for i in final_values:
            if i < money and i not in evaluation_list:
                evaluation_list.append(i)

        to_be_bought = max(evaluation_list)
        to_be_bought_index = evaluation_list.index(to_be_bought)
        final_click(to_be_bought_index)
        current_time = time.time()
    else:
        pass
else:
    money = current_bank()
    print(money)

driver.quit()


event_times = driver.find_elements_by_css_selector(".event-widget time")
event_final_times = []
for time in event_times:
    event_final_times.append(time.text)

event_final_links = []
event_links = driver.find_elements_by_css_selector(".event-widget a")
del event_links[0]

for links in event_links:
    event_final_links.append(links.text)
# print(event_final_links)
# print(event_final_times)
driver.quit()

final_dict = {}
for i in range(0,5):
    first_dict = {}
    first_dict["time"] = event_final_times[i]
    first_dict["name"] = event_final_links[i]
    final_dict[i] = first_dict
print(final_dict)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# service = Service("C:\Development\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
#
# driver.get("https://yahoo.co.in")
