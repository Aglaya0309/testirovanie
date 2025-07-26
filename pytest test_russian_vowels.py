import pytest
from test_russian_vowels import count_russian_vowels

def test_only_russian_vowels():
    """Тест для строки, содержащей только гласные"""
    assert count_russian_vowels("аеёиоуыэюя") == 10
    assert count_russian_vowels("ааа") == 3
    assert count_russian_vowels("ёё") == 2

def test_no_russian_vowels():
    """Тест для строки без гласных"""
    assert count_russian_vowels("бвгджзклмнпрстфхцчшщ") == 0
    assert count_russian_vowels("12345") == 0
    assert count_russian_vowels("!@#$%") == 0

def test_mixed_russian_text():
    """Тест для смешанных строк с разным регистром"""
    assert count_russian_vowels("Привет, мир!") == 3
    assert count_russian_vowels("Съешь ещё этих мягких французских булок") == 12
    assert count_russian_vowels("Программирование - это интересно") == 13
    assert count_russian_vowels("АаАбБбЯяЯ") == 6