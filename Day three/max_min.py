def find_max_min(list):
	if min(list) == max(list):
		return [len(list)]
	else:
		return [min(list),(max(list))]