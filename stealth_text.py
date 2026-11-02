# -*- coding: utf-8 -*-
"""
Модуль для замены русских букв на визуально идентичные Unicode-символы
для обхода фильтров Telegram
"""

# Маппинг русских букв на латинские/другие Unicode символы, которые выглядят так же
STEALTH_MAP = {
    # Строчные
    'а': 'a',  # латиница
    'е': 'e',  # латиница
    'о': 'o',  # латиница
    'р': 'p',  # латиница
    'с': 'c',  # латиница
    'у': 'y',  # латиница
    'х': 'x',  # латиница
    
    # Заглавные
    'А': 'A',  # латиница
    'В': 'B',  # латиница
    'Е': 'E',  # латиница
    'К': 'K',  # латиница
    'М': 'M',  # латиница
    'Н': 'H',  # латиница
    'О': 'O',  # латиница
    'Р': 'P',  # латиница
    'С': 'C',  # латиница
    'Т': 'T',  # латиница
    'Х': 'X',  # латиница
}


def make_stealth_text(text: str, replace_percent: int = 50) -> str:
    """
    Заменяет часть русских букв на визуально идентичные символы
    
    Args:
        text: Исходный текст
        replace_percent: Процент букв для замены (0-100)
        
    Returns:
        Текст с замененными символами
    """
    import random
    
    result = []
    for char in text:
        if char in STEALTH_MAP and random.randint(1, 100) <= replace_percent:
            result.append(STEALTH_MAP[char])
        else:
            result.append(char)
    
    return ''.join(result)


def make_full_stealth_text(text: str) -> str:
    """
    Заменяет ВСЕ возможные русские буквы на визуально идентичные символы
    
    Args:
        text: Исходный текст
        
    Returns:
        Текст с максимальной заменой символов
    """
    result = []
    for char in text:
        result.append(STEALTH_MAP.get(char, char))
    
    return ''.join(result)


def make_pattern_stealth_text(text: str, pattern: str = "alternate") -> str:
    """
    Заменяет буквы по определенному паттерну
    
    Args:
        text: Исходный текст
        pattern: Паттерн замены:
            - "alternate": заменять через одну
            - "vowels": заменять только гласные
            - "consonants": заменять только согласные
            
    Returns:
        Текст с замененными символами по паттерну
    """
    vowels = {'а', 'е', 'о', 'у', 'А', 'Е', 'О'}
    consonants = {'р', 'с', 'х', 'В', 'К', 'М', 'Н', 'Р', 'С', 'Т', 'Х'}
    
    result = []
    replaceable_count = 0
    
    for i, char in enumerate(text):
        should_replace = False
        
        if char in STEALTH_MAP:
            if pattern == "alternate":
                should_replace = (replaceable_count % 2 == 0)
                replaceable_count += 1
            elif pattern == "vowels":
                should_replace = char in vowels
            elif pattern == "consonants":
                should_replace = char in consonants
        
        if should_replace:
            result.append(STEALTH_MAP[char])
        else:
            result.append(char)
    
    return ''.join(result)


if __name__ == "__main__":
    # Примеры использования
    test_text = "Это тестовое сообщение для проверки"
    
    print("Оригинал:")
    print(test_text)
    print()
    
    print("50% замена (случайная):")
    print(make_stealth_text(test_text, 50))
    print()
    
    print("Полная замена:")
    print(make_full_stealth_text(test_text))
    print()
    
    print("Замена через одну:")
    print(make_pattern_stealth_text(test_text, "alternate"))
    print()
    
    print("Замена только гласных:")
    print(make_pattern_stealth_text(test_text, "vowels"))
    print()
