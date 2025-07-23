from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    mask_card = get_mask_card_number(1234567890123456)
    mask_account = get_mask_account(1234567890123456)
    print(mask_card)
    print(mask_account)

if __name__ == "__main__":
    from src.processing.operations import filter_by_state, sort_by_date

    data = [
        {"date": "2022-07-04", "state": "EXECUTED"},
        {"date": "2022-05-17", "state": "CANCELED"},
        {"date": "2022-08-20", "state": "EXECUTED"},
    ]

    filtered = filter_by_state(data)
    sorted_data = sort_by_date(filtered)

    print("Фильтрованные:")
    print(filtered)

    print("\nОтсортированные:")
    print(sorted_data)
