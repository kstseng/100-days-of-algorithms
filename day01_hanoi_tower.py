def hanoi(height, left='left', right='right', middle='middle'):
	'''
		step1: 把 n-1 個 disk，從 left 移動到 middle (暫存)
		step2: 把 left (largest) 的 disk，從 left 移到 right
	    step3: 把 middle 的 n-1 個 disk，從 middle 移動到 right (對 middle 的 n-1 個 disk 來說，已全是可移動範圍，因為 right 的 disk 是最大的) ==> Recursive!

		Note: 
		1. Base case: disk 數量為 1，從 left 移到 right
	'''
	if height:
		hanoi(height-1, left, middle, right)
		print(left, '=>', right)
		hanoi(height-1, middle, right, left)

hanoi(3)
