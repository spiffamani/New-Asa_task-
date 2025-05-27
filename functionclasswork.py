student_score1 = 50
student_score2 = 50
student_score3 = 50
student_score4 = 50 

scores = [50 , 34 , 45 , 50 , 25]

cart = ['banana' , ' 33 ' ,'juice', 2.5, ['fish', 'palm oil'], True]
print(cart[0].upper())

print("we have", len(scores), " scores")

for score in scores:
	print(score)

for idx in range(len(scores)): 
	print(idx)

for value in enumerate(cart):
	print(value)

#score.append(99)
#score.pop(1)
cart[4].insert(0, 6)
#score.extend([34 ,67, 87, 65])
new_list = cart  + scores
print(scores[0:3])