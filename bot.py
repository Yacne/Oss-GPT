import re
from ai import AI

class Bot:
    def __init__(self):
        self.ai = AI()

    def start(self):
        print("welcom to Oss GPT V.3")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "p.off":
                print("Oss: وداعًا!")
                break
            elif user_input.startswith("add("):
                try:
                    content = user_input[4:-1]
                    word, meaning, response = map(str.strip, content.split(","))
                    self.ai.add_word(word, meaning, response)
                    print(f"Oss: تمت إضافة الكلمة '{word}' بنجاح.")
                except ValueError:
                    print("Oss: تأكد من تنسيق الأمر add(كلمة, معنى, رد).")
            elif user_input.lower() == "data":
                data = self.ai.get_all_data()
                if data:
                    print("الكلمات التي تعرفها:")
                    for word, info in data.items():
                        print(f"{word} - المعنى: {info['meaning']}، الرد: {info['response']}")
                else:
                    print("Oss: لا توجد كلمات محفوظة.")
            elif user_input.lower() == "clear":
                if self.ai.clear_all_words():
                    print("Oss: تم مسح جميع الكلمات.")
                else:
                    print("Oss: لا توجد كلمات لتتم مسحها.")
            elif user_input.startswith("forget("):
                word = user_input[7:-1].strip()
                if self.ai.remove_word(word):
                    print(f"Oss: تم نسيان الكلمة '{word}'.")
                else:
                    print(f"Oss: لا أعرف الكلمة '{word}'.")
            elif user_input.startswith("edit("):
                try:
                    content = user_input[5:-1]
                    old_word, new_word = map(str.strip, content.split(","))
                    if self.ai.edit_word(old_word, new_word):
                        print(f"Oss: تم تعديل الكلمة '{old_word}' إلى '{new_word}'.")
                    else:
                        print(f"Oss: لا أعرف الكلمة '{old_word}'.")
                except ValueError:
                    print("Oss: تأكد من تنسيق الأمر edit(الكلمة القديمة, الكلمة الجديدة).")
            elif user_input.startswith("synonym("):
                try:
                    content = user_input[9:-1]
                    word, *synonyms = map(str.strip, content.split(","))
                    print(f"Oss: مرادفات كلمة '{word}' هي: {', '.join(synonyms)}.")
                except ValueError:
                    print("Oss: تأكد من تنسيق الأمر synonym(الكلمة, مرادف1, مرادف2,...).")
            elif user_input.startswith("opposite("):
                try:
                    content = user_input[9:-1]
                    word, *opposites = map(str.strip, content.split(","))
                    print(f"Oss: أضداد كلمة '{word}' هي: {', '.join(opposites)}.")
                except ValueError:
                    print("Oss: تأكد من تنسيق الأمر opposite(الكلمة, ضد1, ضد2,...).")
            elif user_input.lower().startswith("ما معنى") or user_input.lower().startswith("ما معنى كلمة"):
                word = user_input.split(" ")[-1]
                meaning = self.ai.get_meaning(word)
                if meaning:
                    print(f"Oss: معنى كلمة '{word}' هو: {meaning}")
                else:
                    print(f"Oss: لا أعرف معنى كلمة '{word}'.")
            elif re.match(r"^\d+(\+|\-|\*|\/)\d+$", user_input):
                result = self.ai.calculate_expression(user_input)
                print(f"Oss: {result}")
            elif user_input.lower() == "؟" or user_input.lower() == "help":
                print("""
                قائمة الأوامر المتاحة:
                1. add(k, معنى, رد) - إضافة كلمة جديدة.
                2. forget(k) - نسيان كلمة.
                3. edit(k1, k2) - تعديل كلمة.
                4. synonym(k, مرادف1, مرادف2, ...) - إضافة مرادفات.
                5. opposite(k, ضد1, ضد2, ...) - إضافة أضداد.
                6. data - عرض الكلمات المحفوظة.
                7. clear - مسح جميع الكلمات.
                8. P.off - للخروج.
                9. ما معنى كلمة (الكلمة) - معرفة معنى الكلمة.
                10. العمليات الحسابية مثل 6+4.
                """)
            else:
                response = self.ai.get_response(user_input)
                if response:
                    print(f"Oss: {response}")
                else:
                    print("Oss: لا أعرف هذه الكلمة، هل يمكنك شرحها لي؟")
                    meaning = input("معنى الكلمة: ").strip()
                    reply = input("كيف أرد على هذه الكلمة؟ ").strip()
                    self.ai.add_word(user_input, meaning, reply)
                    print("Oss: شكراً! لقد تعلمت كلمة جديدة.")