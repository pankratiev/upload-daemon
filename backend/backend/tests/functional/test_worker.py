from backend.tests import *

class TestWorkerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='worker', action='index'))
        # Test response...
