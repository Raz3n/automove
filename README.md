# Automove
A program that automates finding properties on rightmove and then fills out a google form with property information.

## Motivation
Automation is an area of interest to me and I wanted to find ways to implement what I have learned.  
Seeing friends spend afternoons combing through properties on different websites and creating lists of the properties they liked, sparked the idea of automating the entire process, using the tools I had been learning.  
This also provided the opportunity to work on creating ReadMe's which is an area I realize need some more work.

## Built with:
* **Python**
    - **BeautifulSoup**
* **ChromeDriver**
* **Selenium**
* **Google Forms**

## Requirements
1. Some version of **Python3** preferably. (Python 2.7 doesn't have anymore support so I don't know what could happen). 

2. **ChromeDriver**. Can be found at https://chromedriver.chromium.org/. (It is important that your version of ChromeDriver matches the version of google chrome that you are using. Apologies if you're using a different a using browser.)

3. **Selenium WebDriver**. Can be found at https://www.selenium.dev/downloads/.

## How to use:
Once you have the requirements set up, you need to add the path to where your chromedriver is located on your machine, which is in line 45 of the code in main.py.

Create a google form with only one question and select the short answer option. The xpath should be fine for the input but if not you can always use the chrome devtools to find the required xpath.  
The link to your google form should be added to the driver.get("") in line 50 of main.py.

The program can then be run by either:  
- using the command *python3 main.py* in the terminal   
or  
- using the run button in whichever editor or IDE you are using.  

I apologise for these instructions, but it is something I am working on.

## Closing









