def get_date(date: str) -> str:
    """Функция для сокращения даты"""

    new_data = date[8:10] + "." + date[5:7] + "." + date[0:4]

    return new_data


print(get_date("2024-03-11T02:26:18.671407"))

# 2024-03-11T02:26:18.671407     # входной аргумент
# 11.03.2024  # выход функции



def get_mask_card(card_number: str) -> str:
    """Маскировка номера карты"""

    mask_card = card_number[0:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[12:16]

    return mask_card


print(get_mask_card("7000792289606361"))

# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


def get_mask_account(account_number: str) -> str:
    """Маскировки номера банковского счета"""

    mask_account = "**" + account_number[-4:]
    return mask_account


print(get_mask_account("73654108430135874305"))

# 73654108430135874305  # входной аргумент
# **4305  # выход функции









def mask_account_card(info_card: str) -> str:
    """Функция определяет счет это или номер карты и возвращает замаскированный"""
    info_card_list = info_card.split()
    if "Счет" in info_card_list:
        return f"Счет **{info_card_list[-1][-4:]}"
    else:
        card_name = ' '.join(info_card_list[:-1])
        card_number = info_card_list[-1].replace(' ', '')
        return f"{card_name} {get_mask_card(card_number)}"

print(mask_account_card("Счет 73654108430135874305"))

#Visa Platinum 7000792289606361  # входной аргумент
#Visa Platinum 7000 79** **** 6361  # выход функции

#Счет 73654108430135874305  # входной аргумент
#Счет **4305  # выход функции
