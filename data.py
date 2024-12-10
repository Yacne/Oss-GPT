import json

class DataManager:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
    
    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
    
    def search_word(self, word):
        return self.data.get(word, None)
    
    def add_word(self, word, meaning, response):
        self.data[word] = {"meaning": meaning, "response": response}
        self.save_data()
    
    def get_all_data(self):
        return self.data