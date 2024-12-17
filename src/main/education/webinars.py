# src/main/education/webinars.py

from datetime import datetime

class Webinar:
    def __init__(self, title, date, host, description):
        self.title = title
        self.date = date
        self.host = host
        self.description = description

    def __repr__(self):
        return f"Webinar(title={self.title}, date={self.date}, host={self.host})"


class WebinarManager:
    def __init__(self):
        self.webinars = []

    def schedule_webinar(self, title, date, host, description):
        """Schedule a new webinar."""
        webinar = Webinar(title, date, host, description)
        self.webinars.append(webinar)
        print(f"Webinar '{title}' scheduled successfully for {date}.")

    def get_webinar(self, title):
        """Retrieve a webinar by its title."""
        for webinar in self.webinars:
            if webinar.title == title:
                return webinar
        return None

    def list_webinars(self):
        """List all scheduled webinars."""
        return [webinar.title for webinar in self.webinars]

    def display_webinar(self, title):
        """Display the details of a webinar."""
        webinar = self.get_webinar(title)
        if webinar:
            print(f"Title: {webinar.title}\nDate: {webinar.date}\nHost: {webinar.host}\nDescription:\n{webinar.description}")
        else:
            print(f"Webinar '{title}' not found.")
