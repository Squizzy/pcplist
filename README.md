# Extract a Saved List from PCPartPicker
The two options are complementary, so only one needs to be run (results should be the same if you run both)

## download_pcpartpicker.py
- Requires selenium
```pip install selenium```
### Execution:
- type ```python3 download_pcpartpicker.py```
- enter the URL of your list
- the list gets printed in the terminal (it is stored as a dictionary internally)

## parse_pcp_htm.py
- requires bs4 (BeautifulSoup)
```pip install bs4```
- also requires re (for regex) but this should come with python by default
### Execution:
- go to the pcpartpicker page of the list you want to parse in your browser
- right click an empty area of the page and select save
- select "download all" or such like, and save under a folder called "pcplist" besides this python file
- execute ```python3 parse_pcp_htm.py```
- enter your pcpartpicker username for that list
- the list gets printed in the terminal (it is stored as a dictionary internally)
