from random import uniform

thresholds = [0.162, 0.53, 0.8]

for threshold in thresholds:
	for k in range(2):
		if k == 1:
			threshold = threshold / 2
		
		average = 0
		for _ in range(1000):
			num = 10000
			lst = [0 for _ in range(num)]
			for i in range(num):
				sample = uniform(0, 1)
				if sample <= threshold:
					lst[i] = 1
				else:
					lst[i] = 0

			i = 0
			count = 0
			while i < num:
				if sum(lst[i : i + 4]) >= 3:
					count += 1
				i += 4

			average += count

		if k == 0:
			sigma = average / 1000
		else:
			sigma_prime = average / 1000
			print(f"Ratio for rho = {threshold * 2}: {sigma / sigma_prime}")
			print(f"Sensitivity: {sigma / (2 * sigma_prime)}")
			print("\n")
