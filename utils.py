import re

def normalize_text(text):
    """
    تقوم هذه الدالة بتنسيق النص بإزالة الأحرف والعلامات غير الضرورية
    وتوحيد الأحرف المتشابهة مثل (ا، أ، آ، ...) إلى الحرف الأساسي.
    """
    # إزالة العلامات الخاصة
    text = re.sub(r"[.,!؛:؟',?!;:'\"()&_%«»~•$#]", "", text)
    # توحيد الأحرف
    text = text.replace("ا", "أ").replace("آ", "أ").replace("إ", "أ")
    text = text.replace("ى", "ي").replace("ئ", "ي").replace("ء", "ي")
    text = text.replace("ظ", "ض").replace("ة", "ه").replace("ث", "ت")
    text = text.replace("و", "ؤ")
    # توحيد الفواصل العربية والإنجليزية
    text = text.replace("،،", ",")
    # إزالة المسافات الزائدة
    text = re.sub(r"\s+", " ", text).strip()
    return text