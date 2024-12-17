# src/main/education/tutorials.py

class Tutorial:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"Tutorial(title={self.title}, author={self.author})"


class TutorialManager:
    def __init__(self):
        self.tutorials = []

    def add_tutorial(self, title, content, author):
        """Add a new tutorial."""
        tutorial = Tutorial(title, content, author)
        self.tutorials.append(tutorial)
        print(f"Tutorial '{title}' added successfully.")

    def get_tutorial(self, title):
        """Retrieve a tutorial by its title."""
        for tutorial in self.tutorials:
            if tutorial.title == title:
                return tutorial
        return None

    def list_tutorials(self):
        """List all available tutorials."""
        return [tutorial.title for tutorial in self.tutorials]

    def display_tutorial(self, title):
        """Display the content of a tutorial."""
        tutorial = self.get_tutorial(title)
        if tutorial:
            print(f"Title: {tutorial.title}\nAuthor: {tutorial.author}\nContent:\n{tutorial.content}")
        else:
            print(f"Tutorial '{title}' not found.")
