from com.talismanov.TestCase import TestCase
from com.talismanov.WasRun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod " == self.test.log)

    def testSetUp(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)
