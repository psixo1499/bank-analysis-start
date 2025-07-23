from src.widget import get_date, mask_account_card


def test_get_date():
    date = "2024-03-11T02:26:18.671407"
    assert get_date(date) == "11.03.2024"


def test_mask_account_card_with_card():
    card_info = "Visa Classic 1234567812345678"
    masked = mask_account_card(card_info)
    # Проверим, что маскировка сохранила тип и заменила цифры
    assert masked.startswith("Visa Classic")
    assert masked.endswith("5678")
    assert "*" in masked or "****" in masked


def test_mask_account_card_with_account():
    account_info = "Счет 73654108430135874305"
    masked = mask_account_card(account_info)
    assert masked.startswith("Счет")
    assert masked.endswith("4305")
    assert "**" in masked
