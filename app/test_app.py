import unittest
from app import App

class TestMousePressed(unittest.TestCase):

    # app.mouse_pressed should be True after mouseDown()
    def setUp(self):
        self.app = App()

    def test_mouseDown(self):
        self.app.mouseDown()
        self.assertTrue(self.app.mouse_pressed)
        self.app.mouseUp()
        self.assertFalse(self.app.mouse_pressed)

if __name__ == '__main__':
    unittest.main()