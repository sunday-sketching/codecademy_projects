dinner = ['Curry', 'Burrito', 'Pizza', 'Korean Food', 'Pork Cutlet', 'Yakiniku', 'Others']

tell_me = raw_input("Tell me what you want to eat for dinner: ")
print tell_me

for f in dinner:
  if tell_me == 'Curry':
    print "That's what I want to eat!"
    break
  
else: 
  print "Well... I'm not in that mood"
