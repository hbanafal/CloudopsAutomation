import pytest
from com.cloudops.genericlib.WebdriverFactory import WebDriverFactory
from com.cloudops.genericlib.AdminConsole import AdminConsole
from com.cloudops.pagelib.LoginPage import LoginPage

@pytest.yield_fixture(scope="class")
def launch_browser(request, browser):
    print("Launching Browser")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def login(request):
    print("Login")
    lp = LoginPage(request.cls.driver)
    lp.login("hemant.singh@sd2labs.com", "password")


@pytest.fixture(scope="class")
def create_inr_coupon(request):
    print("Creating INR Coupon")
    admin_console = AdminConsole()
    coupon_code = admin_console.create_new_coupon("INR")

    if request.cls is not None:
        request.cls.coupon_code = coupon_code

@pytest.fixture(scope="class")
def create_usd_coupon(request):
    print("Creating USD Coupon")
    admin_console = AdminConsole()
    coupon_code = admin_console.create_new_coupon("USD")

    if request.cls is not None:
        request.cls.coupon_code = coupon_code

def pytest_addoption(parser):
    parser.addoption("--browser")
    #parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption('--browser')
