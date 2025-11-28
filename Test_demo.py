# step 2
import allure
import pytest

@allure.epic("Web UI")
@allure.feature("Login")
@allure.story("Valid Login")
@pytest.mark.smoke
def test_google_search(page):
    page.goto("https://google.com")
    page.fill("textarea[name='q']", "Playwright + Allure is awesome")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")
    
    # This will fail on purpose to show you the screenshot
    assert "GitHub" in page.title()  # ← intentional fail
