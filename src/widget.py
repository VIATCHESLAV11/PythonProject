def get_date(date: str) -> str:
    """Функция для сокращения даты"""
    new_data = date[8:10] + "." + date[5:7] + "." + date[0:4]
    return new_data


print(get_date("2024-03-11T02:26:18.671407"))
