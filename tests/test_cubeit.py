from playwright.sync_api import *

def test_cube(page:Page):
    num = "10"
    page.goto("http://127.0.0.1:8000/")
    number = page.get_by_placeholder("Enter a number")
    number.fill(num)
    cta_btn = page.get_by_role("button", name="Calculate Cube")
    cta_btn.click()
    result = page.locator("p#result")
    expect(result).to_have_text("The cube of 10 is: 1000 ")
    page.close()