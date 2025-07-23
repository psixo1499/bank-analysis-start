import datetime


def mask_card_number(card: str) -> str:
    return "**** masked card ****"

def mask_account_number(card: str) -> str:
    return "**** masked account ****"


result = mask_card_number("Visa Platinum 1234567890123456")
print(result)

def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO-формата в формат 'ДД.ММ.ГГГГ'.

    Args:
        date_str (str): строка вида '2024-03-11T02:26:18.671407'

    Returns:
        str: строка в формате '11.03.2024'
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")

def mask_account_card(item: str) -> str:
    """
    Маскирует номер карты или счёта из входной строки.

    Args:
        item (str): строка вида 'Visa Platinum 1234567890123456' или 'Счет 73654108430135874305'

    Returns:
        str: строка с замаскированным номером
    """
    if item.startswith("Счет"):
        return mask_account_number(item)
    else:
        return mask_card_number(item)
