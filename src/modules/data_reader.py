import os.path
import json
import random
import sys


class MaidDataReader:
    PATH = os.path.join(os.path.dirname(__file__), "..", "..", "resources", "data.json")

    def __init__(self):
        self.data = None
        with open(MaidDataReader.PATH, "r") as f:
            content = f.read()
            self.data = json.loads(content)

        if self.data is None:
            sys.exit("Could not read JSON data.")

        rare_color_count = len(self.data["common"]["colors"]["rare"])
        self.color_random_max = rare_color_count + 2 * len(self.data["common"]["colors"]["double_chance"])
        self.rare_color_start_index = self.color_random_max - rare_color_count

    def get_random_color(self):
        index = random.randrange(self.color_random_max)
        if index >= self.rare_color_start_index:
            return self.data["common"]["colors"]["rare"][index - self.rare_color_start_index]

        return self.data["common"]["colors"]["double_chance"][int(index / 2)]
