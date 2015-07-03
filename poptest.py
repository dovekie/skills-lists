test_list = ["hello", "hey", "spam", "spam", "bacon", "bacon"]

for item in test_list:
	print item,
	print len(item)
	if len(item) == 4:
		test_list.remove(item)
	# if len(item) <= 4:
		# print len(item)
		# test_list.remove(item)
	# else:
		# print len(item)
		# pass
		
print test_list