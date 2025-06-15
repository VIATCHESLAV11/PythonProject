def get_mask_card(card_number: str) -> str:
    """Маскировка номера карты"""

    mask_card = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:16]

    return mask_card


# print(get_mask_card("7000792289606361"))

# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


def get_mask_account(account_number: str) -> str:
    """Маскировки номера банковского счета"""

    mask_account = "**" + account_number[-4:]
    return mask_account


# print(get_mask_account("73654108430135874305"))

# 73654108430135874305  # входной аргумент
# **4305  # выход функции
