from bs4 import BeautifulSoup
import re


def main():
    print("Extracts the saved list from PCPartPicker\n\
    Needs:  The complete webpage saved as a .htm in a folder pcplist/\n\
            Complete means the option offered by the browser when right clicking on the page and selecting save\n\
            Also, the username as the page saves with the username included in the .htm title\n\n")
    
    username = input("Username: ")
    filename = f"pcplist/{username} - Saved Part Lists - PCPartPicker.htm"

    regex_component = r'^<td class="td__component">\n<a.*>\n *\n *(.*)\n *</a>\n</td>$'
    regex_name = r'^<td class="td__name">\n.*">(.*)</a>\n</td>$'
    regex_name_parametric = r'^<td class="td__name">(?:.|\n)*parametric--parts">(?:.|\n)*">(.*)</a>(?:.|\n)*</td>$'

    with open(filename, "r") as f:
        soup = BeautifulSoup(f, features="html.parser")
        soup.find_all("div", id="partlist_render")

        td_component = soup.find_all("td", "td__component")
        components = list(
            map(lambda x: re.match(regex_component, str(x)).group(1), td_component)
        )

        td_name = soup.find_all("td", class_="td__name")
        names = list(
            map(
                lambda x: (
                    re.match(regex_name, str(x)).group(1)
                    if (re.match(regex_name, str(x)))
                    else re.match(regex_name_parametric, str(x)).group(1)
                ),
                td_name,
            )
        )

    partslist = {}
    for i in range(len(names)):
        partslist[components[i]] = names[i]

    print(partslist)


if __name__ in "__main__":
    main()
