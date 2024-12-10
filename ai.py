import json

class AI:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def add_word(self, word, meaning, response):
        self.data[word] = {'meaning': meaning, 'response': response}
        self.save_data()

    def remove_word(self, word):
        if word in self.data:
            del self.data[word]
            self.save_data()
            return True
        return False

    def edit_word(self, old_word, new_word):
        if old_word in self.data:
            self.data[new_word] = self.data.pop(old_word)
            self.save_data()
            return True
        return False

    def get_all_data(self):
        return self.data

    def clear_all_words(self):
        self.data.clear()
        self.save_data()
        return True

    def get_response(self, user_input):
        return self.data.get(user_input, {}).get('response', None)

    def get_meaning(self, word):
        return self.data.get(word, {}).get('meaning', None)

    def calculate_expression(self, expression):
        try:
            return eval(expression)
        except:
            return "Oss: خطأ في الحساب."