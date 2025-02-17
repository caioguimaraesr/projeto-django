from selenium.webdriver.common.by import By
from .base import RecipeBaseFunctionalTest
import pytest

@pytest.mark.functional_test
class RecipeHomePageFunctionaTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn("", body.text)
