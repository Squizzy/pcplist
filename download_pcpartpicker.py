from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    print("Extracts the Saved List from PCPartPicker\n\
    given the URL of the list in the form:\n\
        https://uk.pcpartpicker.com/user/<user name>/saved/#view=<list code>\n\
    eg: https://uk.pcpartpicker.com/user/imapcmaker/saved/#view=dk9XlL\n\n\
    OF NOTE: This script tequires selenium which will open the Chrome Browser (other browsers possible by modifing the .py)\n\n")
        
    pcpurl = input("Enter the complete url: ")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.page_load_strategy = "none"

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.get(pcpurl)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "partlist_render"))
        )
    except Exception:
        print("Problem: Could not find the list\n")
        return 1
    finally:
        print("Great, list found!\n")

    td_names_e = element.find_elements(By.CLASS_NAME, "td__name")
    td_components_e = element.find_elements(By.CLASS_NAME, "td__component")
    td_names = list(
        map(lambda x: x.text.removeprefix("From parametric selection:\n"), td_names_e)
    )
    td_components = list(map(lambda x: x.text, td_components_e))

    listitems = {}
    for i in range(len(td_names)):
        listitems[td_components[i]] = td_names[i]

    print("\n".join(f"{k}\t\t{v}" for k, v in listitems.items()))


if __name__ in "__main__":
    main()
