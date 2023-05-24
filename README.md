# Exercitando_args_e_kwargs

Introdução
Nessa atividade exercitaremos o conteúdo visto sobre packing e unpacking.

Ao final do desafio, terá uma seção de consulta com a solução de cada um dos tópicos. Para não sabotar seu próprio aprendizado, não a consulte na primeira dificuldade que aparecer, tente raciocinar e pesquisar formas de executar o que é pedido.

Exercitando packing e unpacking
Defina as seguintes funções, observando os exemplos de retorno de cada uma:

sum_numbers
Parâmetro:
*args: Quantidade indefinida de parâmetros numéricos inteiros.
Procedimento: Somar cada um dos valores recebidos em args.
Retorno: A soma de cada um dos valores recebidos em args.
# Exemplo
numbers = [1, 2, 3, 4, 5, 6]

result = sum_numbers(*numbers)
print(result)
# 21

get_multiplied_amount
Parâmetros:
multiplier: Número inteiro utilizado como multiplicador;
*args: Quantidade indefinida de parâmetros numéricos inteiros;
Procedimento: Somar cada um dos valores recebidos em args e multiplicar essa soma por multiplier.
Retorno: O resultado das operações como valor numérico.
# Exemplo
numbers = [1, 2, 3]
multiplier = 2

result = get_multiplied_amount(multiplier, *numbers)
print(result)
# 12

word_concatenator
Parâmetros:
*args: Quantidade indefinida de palavras;
Procedimento: Concatenar cada uma das palavras recebidas em args aplicando um espaço como separador. Não pode haver espaço após a última palavra;
Retorno: Uma string contendo todas as palavras concatenadas;
# Exemplo
words = ["Tá", "pegando", "fogo", "bicho!!!"]
concatenated_words = word_concatenator(*words)
print(concatenated_words)
# "Tá pegando fogo bicho!!!"

inverted_word_factory
Parâmetros:
*args: Quantidade indefinida de palavras;
Procedimento: Concatenar cada uma das palavras recebidas em args, porém cada palavra deve estar invertida, assim como a ordem das palavras;
Retorno: Uma string contendo todas as palavras concatenadas, porém, cada uma delas devem estar invertidas, inclusive a ordem das palavras;
# Exemplo
words = ["eae", "amigão", "belezinha?"]

inverted_words = inverted_word_factory(*words)
print(inverted_words)
# "?ahnizeleb oãgima eae"

dictionary_separator
Parâmetros:
**kwargs: Dicionário contendo uma quantidade indefinida de itens;
Procedimento:
Agrupar em uma lista todas as chaves do dicionário kwargs;
Agrupar em uma lista todas as valores do dicionário kwargs;
Retorno: Retornar uma tupla de duas posições, na primeira posição a lista de chaves do dicionário kwargs, na segunda posição uma lista de valores do dicionário kwargs;
# Exemplo
user = {"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}

items = dictionary_separator(**user)
print(type(items))
<class 'tuple'>
print(items[0])
# ["name", "age", "favorite word"]
print(items[1])
# ["Naruto", 16, "Ichiraku Ramen"]

dictionary_creator
Parâmetros:
*args: Quantidade indefinida de valores (podem ser inteiros ou string);
**kwargs: Dicionário contendo uma quantidade indefinida de itens.
Procedimento:
Uma chave na posição 2 do dicionário, deve ser substituída pelo valor de posição 2 dentro da tupla args, essa ordem deve ser seguida de forma respectiva;
Caso a quantidade de valores dentro da tupla args seja maior que a quantidade de itens no dicionário, ignorar os valores excedentes em args;
Retorno:
Retornar None, caso a quantidade de valores dentro da tupla args seja menor que a quantidade de itens em kwargs.
Retornar um dicionário, caso a quantidade de valores dentro da tupla args seja igual ou maior a quantidade de itens em kwargs.
# Exemplo
change_keys = ["username", "password", "address"]
user = {"name": "Williams", "some_key": "1234"}

modified_user = dictionary_creator(*change_keys, **user)
print(modified_user)
# {"username": "Williams", "password": "1234"}

purchase_logger(**kwargs)
Parâmetros: 
**kwargs: Dicionário contendo uma quantidade indefinida de itens.
Procedimento: Formar uma string contendo as informações do produto;
Retorno: String formada com quantidade, nome do produto e seu preço;
# Exemplo
purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}

purchase_log = purchase_logger(**purchase)
print(purchase_log)
# "4 washing powder bought by 6.7"

world_cup_logger(country, *args)
Parâmetros:
country: Uma string representando um país;
*args: Anos das copas do mundo em que o país foi campeão (lista de números inteiros);
Procedimento: Formar uma string com o nome do país e os anos em que foi campeão, em ordem crescente;
Retorno: String formada com o nome do país e os anos em que foi campeão, exatamente como no exemplo;
# Exemplo
country = 'Alemanha'
year_list = [2014, 1990, 1974, 1954]

log = world_cup_logger(country, *year_list)
print(log)
# "Alemanha - 1954, 1974, 1990 e 2014"

