# Auto checker for nearby NHS COVID Vaccine appointments (UK)

For if you can't seem to find a vaccine appt near ya.

Leave this running in the background and it'll find a vaccine appointment place down the road, in like 2 minutes.

### What he do tho
It fills in the entire [NHS Vaccine Booking form](https://www.nhs.uk/book-a-coronavirus-vaccination) and checks for nearby appointments every 3 seconds. Alerts you with text-to-speech.

## Requirements
- [Chrome](https://www.google.com/intl/en_uk/chrome/)
- [Python](https://www.python.org/downloads/)
- [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/)
- [Selenium](https://pypi.org/project/selenium/)

## Installation

1. Install [**Python**](https://www.python.org/downloads/)
2. Install [**Pip**](https://pip.pypa.io/en/stable/installing/)
3. If you're computer isn't MacOS or has the M1 chip, [download the right **Chromedriver**](https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/) and replace the current Chromedriver file in this project with that
4. Install **Selenium**: `pip3 install selenium`
## How to run

1. Download this project
2. Open main.py and **fill in your personal details**.
- *(Note: The data stays on that file. No-one else has it unless you specifically share)*
![Example of Personal Details to put](example-of-personal-details.png)
3. Run main.py in Python. 
```
python main.py
```
