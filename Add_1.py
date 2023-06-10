# 2. Дан список, вывести отдельно буквы и цифры.

# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

a = ( "a", 'b', '2', '3' ,'c')
nums = list(map(str,range(0,10)))
b = list(filter(lambda x: x not in nums, a))
c = list(filter(lambda x: x in nums, a))
print(*b)
print(*c)