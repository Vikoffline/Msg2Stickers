import json

# 1 - токен сообщества вк    
# 2 - префикс команды
# 3 - разделитель кода id и сообщения
# 4 - словарь user_id: token, содержащий пользователей от имени которых могут отправляться сообщения
# 5 - словарь сокращение:user_id для удобства   
# 6 - Это не трогай

config = {
    "token": "token",
    "code": "стк",
    "sep": "/",
    "ids": {"id": "токен"},
    "shortcuts": {"сокр1": "id1", "сокр2": "id2", "беседа": "2000000000+id беседы"},
    "alph": {"а": "91641", "б": "91642", "в": "91643", "г": "91644", "д": "91645", "е": "91646", "ё": "91647", "ж": "91648", "з": "91649", "и": "91650", "й": "91651", "к": "91652", "л": "91653", "м": "91654", "н": "91655", "о": "91656", "п": "91657", "р": "91658", "с": "91659", "т": "91660", "у": "91661", "ф": "91662", "х": "91663", "ц": "91664", "ч": "91665", "ш": "91666", "щ": "91667", "ъ": "91668", "ы": "91669", "ь": "91670", "э": "91671", "ю": "91672", "я": "91673", "1": "91674", "2": "91675", "3": "91676", "4": "91677", "5": "91678", "6": "91679", "7": "91680", "8": "91681", "9": "91682", "0": "91683", "!": "91684", "?": "91685", ": ": "91686", ",": "91687", ".": "91688"}
}

with open("config.json", "w") as conf: 
    json.dump(config, conf)