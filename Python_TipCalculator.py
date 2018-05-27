meal = 44.50
tax = 6.75 / float(100)
tip = 15 / float(100)
meal = meal + meal * tax
total = meal + meal * tip
print total