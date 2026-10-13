from enum import Enum

# Task 1
def test_info(author, component):
    def decorator(cls):
        cls.author = author
        cls.component = component
        return cls
    return decorator

# Task 2
PAGES = []
def register_page():
    def decorator(cls):
        if cls.__name__ not in PAGES:
            PAGES.append(cls.__name__)
        return cls
    return decorator

# Task 3
class Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, cls):
        cls.tag_name = self.tag_name
        return cls

# Task 4
class Environment(Enum):
    DEV = "https://dev.example.com"
    STAGE = "https://stage.example.com"
    PROD = "https://example.com"