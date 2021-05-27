def mergeSort(numbers, start, end): #сортировка слиянием
	if end - start > 1: #длина массива позволяет работать?
		middle = (start + end) // 2 #середина массива
		mergeSort(numbers, start, middle) #рекурсивные вызовы
		mergeSort(numbers, middle, end)
		left = numbers[start: middle] #левый массив
		right = numbers[middle: end] #правый массив
		internalSort(numbers, left, right, start) 
		print(start + 1, end, numbers[start], numbers[end - 1]) #выводим слитые массивы

def internalSort(arr, left, right, start): #переставляем элементы
	i = j = 0
	k = start
	while i < len(right) and j < len(left):
		if left[j] > right[i]:
			arr[k] = right[i]
			i += 1
		else:
			arr[k] = left[j]
			j += 1
		k += 1
	while j < len(left):
		arr[k] = left[j]
		j += 1
		k += 1
	while i < len(right):
	    arr[k] = right[i]
	    i += 1
	    k += 1

def main():
	m = int(input()) #вводим кол-во элементов
	numbers = list(map(int, input().split(maxsplit = m))) #вводим элементы
	mergeSort(numbers, 0, len(numbers)) #вызываем сортировку
	print(*numbers) #выводим получившийся массив
	
main()