import pytest

def search_python_tutorials():
    # Заглушка для поиска
    return ['Python tutorial', 'Python documentation', 'Python examples', 'Python tips']


def test_search_results():
    # Ожидаемые результаты поиска
    expected_results = ['Python tutorial', 'Python documentation', 'Python examples']

    # Фактические результаты (имитация поиска)
    actual_results = search_python_tutorials()

    # Проверяем, что все ожидаемые результаты присутствуют
    for expected in expected_results:
        assert expected in actual_results, f"Результат '{expected}' не найден"

    # # Проверяем количество результатов
    # assert len(actual_results) >= len(expected_results)



