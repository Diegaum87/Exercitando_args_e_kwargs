def sum_numbers(*args):
    result = sum(args)
    return result


numbers = [1, 2, 3, 4, 5, 6]
result = sum_numbers(*numbers)
print(result)

# --------------------------------------------


def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result


numbers = [1, 2, 3, 4, 5, 6]

result = multiply_numbers(*numbers)
print(result)

# --------------------------------------------


def word_concatenator(*args: tuple):
    result = ' '.join(args)
    return result


words = ["Tá", "pegando", "fogo", "bicho!!!"]
result = word_concatenator(*words)
print(result)


# --------------------------------------------


def inverted_word_factory(*args: tuple):
    result = ' '.join(args)[::-1]
    return result


words = ["eae", "amigão", "belezinha?"]
result = inverted_word_factory(*words)
print(result)

# --------------------------------------------


def dictionary_separator(**kwargs):
    return (
        list(kwargs.keys()),
        list(kwargs.values()),
    )


user = {"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}
items = dictionary_separator(**user)
print(items[0])
print(items[1])

# --------------------------------------------


def dictionary_creator(*args: tuple, **kwargs: dict):
    output_dict = {}

    for index, value in enumerate(kwargs.values()):
        new_key = args[index]
        new_value = value
        output_dict[new_key] = new_value

    return output_dict


change_keys = ["username", "password", "address"]
user = {"name": "Williams", "some_key": "1234"}

modified_user = dictionary_creator(*change_keys, **user)
print(modified_user)

# --------------------------------------------


def purchase_logger(**kwargs):
    return f"{kwargs['quantity']} {kwargs['name']} bought by {kwargs['price']}"


purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}

purchase_log = purchase_logger(**purchase)
print(purchase_log)

# -----------------------------------------------


def world_cup_logger(country: str, *args: tuple):
    # Ordena os argumentos em ordem crescente e os converte em strings
    sorted_str_list = [str(arg) for arg in sorted(args)]

    # Junta os elementos da lista por ', ' para formar a string formatada
    formatted_str = ", ".join(sorted_str_list)

    # Splita começando pelo fim a primeira ocorrência de ', '
    reverse_split = formatted_str.rsplit(", ", 1)

    # Monta a string base "country + ' - '"
    # e junta com o split anterior usando ' e '
    return country + " - " + " e ".join(reverse_split)


country = 'Alemanha'
year_list = [2014, 1990, 1974, 1954]

log = world_cup_logger(country, *year_list)
print(log)
