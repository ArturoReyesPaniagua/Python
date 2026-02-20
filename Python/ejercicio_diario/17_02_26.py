nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for n in range(len(nums)):
        if i != n:  
            resultado = nums[i] + nums[n]
            if resultado == target:
                print(f"Los índices son [{i}, {n}]")




nums = [2,7,11,15]
target = 9

numeros_vistos = {}

for i in range(len(nums)):
    complemento = target - nums[i]

    if complemento in numeros_vistos:
        print([numeros_vistos[complemento], i])
    
    numeros_vistos[nums[i]] = i
