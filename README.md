# python-two-sum
Projeto de estudos
# 🔢 Encontrando Pares com Soma Alvo

Um pequeno projeto em **Python** criado para praticar conceitos básicos de lógica de programação, como listas, loops, condicionais, entrada de dados e armazenamento de resultados.

## 📌 Sobre o projeto

O programa recebe um **valor alvo (`target`)** informado pelo usuário e verifica quais pares de números dentro de uma lista somam exatamente esse valor.

Por exemplo:

```text
Lista: [1, 2, 3, 4, 5]
Valor alvo: 7

2 + 5 = 7
3 + 4 = 7
```

O programa também informa a quantidade de pares encontrados.

## ⚙️ Como funciona

O código utiliza dois loops `for` para comparar os números da lista entre si.

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
```

O `i + 1` faz com que o programa não compare um número com ele mesmo e também evita verificar o mesmo par duas vezes.

Depois, os valores são somados:

```python
soma = nums[i] + nums[j]
```

Quando a soma é igual ao valor informado pelo usuário, o par é armazenado na lista `pares`.

## 🧠 Conceitos praticados

* Listas em Python
* `input()`
* Conversão com `int()`
* Estrutura `for`
* `range()`
* Estrutura condicional `if`
* Índices de listas
* Operadores matemáticos
* Contagem de resultados
* Armazenamento de dados em uma lista
* Tuplas
* Formatação de strings com `f-string`

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta

```bash
cd nome-do-projeto
```

### 3. Execute o programa

```bash
python nome_do_arquivo.py
```

## 💻 Exemplo de execução

```text
Digite o valor alvo: 11

========== RESULTADO ==========
Lista analisada: [1, 2, 3, 4, 5, 7, 8, 9, 10]
Valor alvo: 11
Quantidade de pares: 4
  1 + 10 = 11
  2 + 9 = 11
  3 + 8 = 11
  4 + 7 = 11
================================
```

## 🎯 Objetivo

Este projeto faz parte dos meus estudos de **Python e lógica de programação**.

A ideia é praticar a resolução de problemas utilizando estruturas básicas da linguagem antes de partir para soluções mais avançadas e otimizadas.

## 📚 Próximos passos

Algumas melhorias que podem ser feitas futuramente:

* Permitir que o usuário informe os números da lista.
* Criar uma função para encontrar os pares.
* Melhorar a organização do código.
* Comparar essa solução com uma abordagem utilizando dicionários.
* Analisar e melhorar a complexidade do algoritmo.

---

**Projeto desenvolvido para fins de estudo e prática de Python.**
