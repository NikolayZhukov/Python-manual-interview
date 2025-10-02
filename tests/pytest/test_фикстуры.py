import pyte?st

# фикстура
@pytest.fixture
def sample_data():
    print("\nВыполняется фикстура перед тестом")  # выполняется перед тестом
    data = [1, 2, 3]
    return data

# тест с использованием фикстуры
def test_sum(sample_data):
    assert sum(sample_data) == 6




