import json


class Document:

    def __init__(self, id, language, text):
        self.id = id
        self.language = language
        self.text = text

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)