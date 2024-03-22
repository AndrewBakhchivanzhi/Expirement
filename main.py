names = ["Кларисса", "Мелисса", "Лариса", "Алиса", "Лариса", "Мама Бориса"]

def look_for_alice(names):
    for name in names:
        if name == "Алиса":
            return True
    return False


print(look_for_alice(names))