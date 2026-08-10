# Two Sum — Python

Implementação do problema **Two Sum** em Python, desenvolvida como parte dos meus estudos de lógica de programação.

## 📌 Sobre o problema

Dada uma lista de números e um valor alvo (`target`), o objetivo é encontrar os pares de números cuja soma seja igual ao valor alvo.

### Exemplo

```text
Lista: [1, 2, 3, 4, 5]
Target: 7
```

Resultado:

```text
2 + 5 = 7
3 + 4 = 7
```

## 🧠 Minha solução

A solução utiliza dois loops `for` para comparar cada número com os números seguintes da lista.

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        soma = nums[i] + nums[j]
```

O `i + 1` faz com que:

* Um número não seja comparado com ele mesmo.
* O mesmo par não seja verificado duas vezes.

Quando a soma encontrada é igual ao `target`, o par é armazenado:

```python
if soma == target:
    pares.append((nums[i], nums[j]))
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

## 📚 Conceitos praticados

* Listas
* Índices
* `for`
* `range()`
* `if`
* `input()`
* Conversão de tipos com `int()`
* Tuplas
* `append()`
* Contadores
* `f-strings`
* Lógica de comparação

## ⏱️ Complexidade

A solução utiliza dois loops aninhados.

**Complexidade de tempo:**

`O(n²)`

Isso acontece porque, no pior caso, cada elemento precisa ser comparado com vários outros elementos da lista.

**Complexidade de espaço:**

`O(n)`

No pior caso, a lista `pares` pode armazenar vários resultados.

## 🚀 Próximos passos

Pretendo futuramente comparar essa solução com uma implementação mais otimizada utilizando um **dicionário (`dict`)**, reduzindo a complexidade de tempo de `O(n²)` para aproximadamente `O(n)`.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar **Python, lógica de programação e resolução de problemas**, servindo também como registro da minha evolução nos estudos.

---

**Status:** ✅ Concluído

**Linguagem:** Python

**Tipo:** Exercício de lógica / Algoritmos
