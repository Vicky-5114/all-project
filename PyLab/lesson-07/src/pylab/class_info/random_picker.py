import json
import random
from typing import Any, Union

from pylab.class_info.class_member import Person


class RandomPicker:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.data: dict = self.load_members_from_file()

    def load_members_from_file(self) -> dict:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return data

    def get_random_member(self, role=None) -> Union[Person, Any]:
        members = self.data["members"]
        if role:
            # Filter members by role
            filtered_members = [member for member in members if member["role"] == role]
        else:
            # If no role specified, use all members
            filtered_members = members

        if filtered_members:  # Ensure there are members to choose from
            member = RandomPicker.convert_keys(random.choice(filtered_members))
            return Person(**member)

        else:
            return None

    @staticmethod
    def convert_keys(d):
        if not isinstance(d, dict):
            return d
        return {k.replace("-", "_"): RandomPicker.convert_keys(v) for k, v in d.items()}


if __name__ == "__main__":
    picker = RandomPicker(file_path="data/class_members.json")
    picker.get_random_member()
