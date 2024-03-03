import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

"""
In order to run tests: 
go to ../tests/
in CMD:
type command pytest test_main_menu.py --gameenv= --browser= 
OR to run only a single test type pytest -k test_MMenu_0001 -v test_main_menu.py --gameenv= --browser=

gameenv = dev / prod
browser = chrome / firefox / edge
"""

def pytest_addoption(parser):
    parser.addoption(
        "--gameenv", action="store", default="dev", help="Env: dev or prod"
    )

    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser: chrome, edge, firefox"
    )

@pytest.fixture
def gameenv(request) -> str:
    return request.config.getoption('--gameenv')

@pytest.fixture
def browser(request) -> str:
    return request.config.getoption('--browser')

@pytest.fixture
def driver(gameenv: str, browser: str):
    driver = None

    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    if driver:

        if gameenv == 'dev':
            driver.get('http://localhost:5173/')
        elif gameenv == 'prod': 
            driver.get('https://tombs-of-cherem.vercel.app/')
        else:
            raise ValueError(f"Unsupported game environment: {gameenv}")
        
        driver.maximize_window()
        
        yield driver
        
        driver.quit()
