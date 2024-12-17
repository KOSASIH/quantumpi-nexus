# src/tests/test_education.py

import unittest
from main.education import TutorialManager, WebinarManager

class TestEducation(unittest.TestCase):
    def setUp(self):
        self.tutorial_manager = TutorialManager()
        self.webinar_manager = WebinarManager()

    def test_add_tutorial(self):
        self.tutorial_manager.add_tutorial("Python Basics", "Learn Python from scratch.", "Alice")
        self.assertEqual(len(self.tutorial_manager.tutorials), 1)

    def test_get_tutorial(self):
        self.tutorial_manager.add_tutorial("Python Basics", "Learn Python from scratch.", "Alice")
        tutorial = self.tutorial_manager.get_tutorial("Python Basics")
        self.assertIsNotNone(tutorial)
        self.assertEqual(tutorial.title, "Python Basics")

    def test_list_tutorials(self):
        self.tutorial_manager.add_tutorial("Python Basics", "Learn Python from scratch.", "Alice")
        self.tutorial_manager.add_tutorial("Advanced Python", "Deep dive into Python.", "Bob")
        self.assertEqual(len(self.tutorial_manager.list_tutorials()), 2)

    def test_schedule_webinar(self):
        self.webinar_manager.schedule_webinar("Blockchain 101", "2023-10-01", "Charlie", "Introduction to Blockchain.")
        self.assertEqual(len(self.webinar_manager.webinars), 1)

    def test_display_webinar(self):
        self.webinar_manager.schedule_webinar("Blockchain 101", "2023-10-01", "Charlie", "Introduction to Blockchain.")
        webinar = self.webinar_manager.get_webinar("Blockchain 101")
        self.assertIsNotNone(webinar)
        self.assertEqual(webinar.title, "Blockchain 101")

if __name__ == '__main__':
    unittest.main()
