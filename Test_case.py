import requests
import time
from seleniumwire import webdriver
# from selenium import webdriver
import pytest
from test_function.question_page_function import *


class TestClass_case_questionPage:
    @classmethod
    # @pytest.fixture(autouse=True)
    def setup_class(self):
        self.driver = webdriver.Firefox(executable_path="./geckodriver.exe")
        self.questionListingPage = QuestionListingPage(self.driver)
        self.driver.get("http://localhost:3000")

    @classmethod
    def teardown_class(self):
        self.driver.close()

    # @pytest.fixture()
    # def resource(self):
    #     self.driver.get("http://localhost:3000")
    #     yield
    #     self.driver.close()
    #     print("teardown - close webdriver")

    def test_case_apiAvailability(self):
        self.questionListingPage.checkApiAvailability(type="GET",
                                                      URL='https://api.stackexchange.com/2.2/tags?pageSize=10&site=stackoverflow')
        self.questionListingPage.checkApiAvailability(type="GET",
                                                      URL='https://api.stackexchange.com/2.2/questions?pageSize=20&site=stackoverflow&tagged=javascript')

    def test_case_trendingTags(self):
        time.sleep(1)

        tagsList = ['javascript', 'python', 'java', 'c#', 'php', 'android', 'html', 'jquery', 'c++', 'css']
        self.questionListingPage.checkTagVisibility(tagsList)
        self.questionListingPage.checkDefaultTagSelected(cssProperty="color", highlight="rgb(255, 255, 255)",
                                                         unhighlight="rgb(49, 151, 149)")
        self.questionListingPage.checkTagRoundCorner(cssProperty="--chakra-radii-md", expectedResult="0.375rem")
        self.questionListingPage.clickOnTag(tagsList)
        self.questionListingPage.countTagsNumbers(len(tagsList))

    def test_case_questionListing(self):
        time.sleep(1)
        self.questionListingPage.checkScollingLazyLoad(scollingTimes=3, tags=['javascript', 'python'])
        self.questionListingPage.checkPositionSticky(cssProperty="position", expectedResult="sticky")
