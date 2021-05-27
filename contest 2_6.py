n = int(input()) #виды товаров
n_c = list(map(int, input().split()))[:n] #их кол-во
k = int(input()) #заказы
k_p = list(map(int, input().split()))[:k] #их кол-во
q = [0] * (n + 1) 
for i in k_p:
	q[i] += 1 #ведём подсчёт заказов клиентов
for i in range(n):
	if q[i + 1] > n_c[i]: #проверяем достаточно ли товаров каждого вида сравнивая кол-во заказанного товара каждого вида с имеющимся
		print('yes') #недостаточно
	else:
		print('no') #достаточно