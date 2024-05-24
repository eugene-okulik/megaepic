import re
from playwright.sync_api import Page, Route
import json


def test_new(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = 'яблокофон 15 про'
        print(body)
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('/step0_iphone/'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone = page.locator('.rf-hcard-copy').nth(0)
    iphone.click()
