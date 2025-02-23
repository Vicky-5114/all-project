from abc import ABC


class Person(ABC):
    def __init__(self, name: str, github_account: str, role: str):
        self.name = name
        self.role = role
        self.github_account = github_account
