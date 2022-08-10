import time
import requests
from utility import *
from page_object.question_page_elements import *


class QuestionListingPage:
    def __init__(self, object):
        self.driver = object  # pass driver into this class
        self.common = Common(driver=self.driver, maxWaitTime=10)

    def checkApiAvailability(self, type, URL):

        if type == "GET":
            r = requests.get(URL)

        assert r.status_code == 200

    def checkTagVisibility(self, tags):
        try:
            for i in tags:
                self.common.visibility(questionPageOject["Tags"](i))
        except Exception as msg:
            print("Exception", msg)
            raise

    def clickOnTag(self, tags):
        try:
            for i in tags:
                self.common.click(questionPageOject["Tags"](i))
                print("click", questionPageOject["Tags"](i))
        except Exception as msg:
            print("Exception", msg)
            raise

    def countTagsNumbers(self, count):
        try:
            print(len(self.common.elementsList(questionPageOject["TagsItems"])))
            assert len(self.common.elementsList(questionPageOject["TagsItems"])) == count
        except Exception as msg:
            print("Exception", msg)
            raise

    def checkDefaultTagSelected(self, cssProperty, highlight, unhighlight):

        list = self.common.elementsList(questionPageOject["TagsCss"])
        print(list)
        print(len(list))
        for i in range(len(list)):
            try:
                if i == 0:
                    assert self.common.elementsAttribute(selector=list[i],
                                                         cssProperty=cssProperty,
                                                         selectorType="webElement") == highlight

                else:
                    assert self.common.elementsAttribute(selector=list[i],
                                                         cssProperty=cssProperty,
                                                         selectorType="webElement") == unhighlight

            except Exception as msg:
                print("Exception", msg)
                raise

    def checkTagRoundCorner(self, cssProperty, expectedResult):
        try:
            Result = self.common.elementsAttribute(selector=questionPageOject["TagsCss"], cssProperty=cssProperty)
            print(Result)
            assert Result == expectedResult
        except Exception as msg:
            print("Exception", msg)
            raise

    def checkPositionSticky(self, cssProperty, expectedResult):
        try:
            Result = self.common.elementsAttribute(selector=".chakra-stack.css-18zmxcd", cssProperty=cssProperty)
            print(Result)
            assert Result == expectedResult
        except Exception as msg:
            print("Exception", msg)
            raise

    def checkScollingLazyLoad(self, scollingTimes, tags):
        try:
            for i in tags:
                self.common.clearReuests()
                self.common.click(questionPageOject["Tags"](i))

                if i == "c#":
                    i = "c%23"
                elif i == "c++":
                    i = "c%2B%2B"

                self.common.waitForRequest(
                    f"https://api.stackexchange.com/2.2/questions\?pageSize=20&site=stackoverflow&tagged={i}")

                for j in range(2, (2 + scollingTimes)):
                    self.common.executeScript("window.scrollTo(0, document.body.scrollHeight);")
                    self.common.waitForRequest(
                        f"https://api.stackexchange.com/2.2/questions\?page={j}&pageSize=20&site=stackoverflow&tagged={i}")
                    print("scolling", i, j)
                    self.common.executeScript("window.scrollTo(0, 0);")

        except Exception as msg:
            print("Exception", msg)
            raise
