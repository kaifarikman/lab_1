import builtins
import src.main as main_module


def test_main_happy_path(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "3 4 +")
    result = main_module.main()
    assert result == 7.0


def test_main_handles_invalid_token(monkeypatch):
    # если в calculator_job возникает ValueError, main должен вернуть 'Ошибка!'
    monkeypatch.setattr(builtins, "input", lambda: "3 x +")
    result = main_module.main()
    assert result == 'Ошибка!'


def test_main_handles_division_by_zero(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "3 0 /")
    result = main_module.main()
    assert result == 'Ошибка!'


def test_main_single_number(monkeypatch):
    # Ввод одиночного числа
    monkeypatch.setattr(builtins, "input", lambda: "5")
    result = main_module.main()
    assert result == 5.0


def test_main_empty_input(monkeypatch):
    # Пустой ввод
    monkeypatch.setattr(builtins, "input", lambda: "")
    result = main_module.main()
    assert result == 'Ошибка!'
