#first
import pytest
from allure_commons.types import AttachmentType
import allure

# Optional: make Allure save results in a folder
def pytest_configure(config):
    config.option.allure_report_dir = "allure-results"   # <-- important line

# Auto-attach screenshot on failure (the thing managers love)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            page = item.funcargs.get("page")
            if page:
                screenshot = page.screenshot()
                allure.attach(
                    screenshot,
                    name="screenshot",
                    attachment_type=AttachmentType.PNG
                )
        except Exception:
            pass
