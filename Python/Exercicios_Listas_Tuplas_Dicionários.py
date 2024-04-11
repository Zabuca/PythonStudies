### Aqui estão 10 exercícios sobre tuplas, dicionários e listas em Python:

### Exercícios Fáceis:
"""
1. **Tupla com cores:** Crie uma tupla chamada `cores` com três cores diferentes. Em seguida, imprima cada cor em uma linha separada.
   
   Exemplo de saída:
   ```
   Vermelho
   Verde
   Azul

cores = ("vermelho", 'verde', "azul")
print(cores[0])
print(cores[1])
print(cores[2])


2. **Dicionário de Estudante:** Crie um dicionário chamado `estudante` com as chaves "nome", "idade" e "curso". Preencha essas chaves com informações fictícias de um estudante e depois imprima o dicionário.

   Exemplo de saída:
   ```
   {'nome': 'Maria', 'idade': 20, 'curso': 'Engenharia'}

   estudante = {
    "nome": 'José Josué João',
    "idade": '22 anos',
    "curso": 'Contabilidade',
}

print(estudante["nome"], estudante["idade"], estudante["curso"])
"""

"""

3. **Lista de Números Pares:** Crie uma lista chamada `numeros_pares` que contenha os números pares de 0 a 10. Em seguida, imprima a lista.

   Exemplo de saída:
   ```
   [0, 2, 4, 6, 8, 10]
   ```

numeros_pares = [num for num in range(0,11) if num % 2 == 0]
print(numeros_pares)
"""

"""
4. **Adicionar Elemento em Lista:** Crie uma lista chamada `frutas` com algumas frutas. Adicione uma nova fruta à lista e depois imprima-a.

   Exemplo de saída:
   ```
   ['Maçã', 'Banana', 'Morango', 'Uva', 'Abacaxi']

# Criando a lista de frutas
frutas = ['Maçã', 'Banana', 'Morango', 'Uva', 'Abacaxi']

# Pedindo ao usuário para inserir uma nova fruta
nova_fruta = input("Digite o nome de uma nova fruta: ")

# Adicionando a nova fruta à lista
frutas.append(nova_fruta)

# Imprimindo a lista de frutas atualizada
print(frutas)
   ```
"""

"""
5. **Obter Valor de Dicionário:** Crie um dicionário chamado `pessoa` com as chaves "nome" e "idade". Em seguida, imprima o valor da chave "nome".

   Exemplo de saída:
   ```
   João
   ```
   pessoa  {
   'nome' : 'João Pessoa',
   'idade' : '22',
}

print(pessoa['nome'])
"""

"""
### Exercícios Médios:

6. **Remover Elemento de Lista:** Crie uma lista chamada `numeros` com os números de 1 a 5. Remova o número 3 da lista e depois imprima-a.

   Exemplo de saída:
   ```
   [1, 2, 4, 5]
   ```

7. **Atualizar Valor de Dicionário:** Crie um dicionário chamado `pessoa` com as chaves "nome" e "idade". Atualize o valor da chave "idade" para 30 e depois 
imprima o dicionário.

   Exemplo de saída:
   ```
   {'nome': 'Maria', 'idade': 30}
   ```

8. **Inverter Ordem de Lista:** Crie uma lista chamada `nomes` com alguns nomes. Inverta a ordem dos nomes na lista e depois imprima-a.

   Exemplo de saída:
   ```
   ['Ana', 'João', 'Pedro', 'Maria']
   ```

### Exercícios Difíceis:

9. **Cópia Profunda de Dicionário:** Crie um dicionário chamado `pessoa` com as chaves "nome" e "idade". Faça uma cópia profunda deste dicionário e, em seguida, 
altere o valor da chave "idade" na cópia para 35. Imprima tanto o dicionário original quanto a cópia.

   Exemplo de saída:
   ```
   Dicionário Original: {'nome': 'Carlos', 'idade': 30}
   Cópia Profunda: {'nome': 'Carlos', 'idade': 35}
   ```

10. **Contagem de Palavras em uma Lista:** Crie uma lista chamada `frase` com algumas palavras. Conte quantas vezes cada palavra aparece na lista e armazene esta
informação em um dicionário. Em seguida, imprima o dicionário.

   Exemplo de saída:
   ```
   {'Eu': 2, 'amo': 1, 'Python': 3}
   ```

Espero que estes exercícios sejam úteis para praticar o uso de tuplas, dicionários e listas em Python! Se precisar de mais ajuda ou tiver alguma dúvida, sinta-se 
à vontade para perguntar.

"""
x = int(input('Qual é o seu número? '))
print(x)