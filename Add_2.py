# Напишите программу, которая подсчитает и выведет сумму квадратов 
# всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию 
# функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

list_1 = list(filter(lambda x: x % 9 == 0, range(10,100)))
list_2 = list(map(lambda x: x*x, list_1))
print(*list_1)
print(*list_2)