nums = [1,2,3,4,5,7,8,9,10]

target = int(input('Digite o valor alvo: '))

par_encontrados = 0
pares = []
for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
        soma = nums[i] + nums[j]
        if soma == target:
            par_encontrados += 1
            pares.append((nums[i], nums[j]))       

            
print('\n========== RESULTADO ==========')
print(f'Lista analisada: {nums}')
print(f'Valor alvo: {target}')
print(f'Quantidade de pares: {par_encontrados}')

for par in pares:
    print(f'  {par[0]} + {par[1]} = {target}')

print('================================')
