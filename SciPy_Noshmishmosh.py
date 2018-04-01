import noshmishmosh 
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

baseline_percent = (100 * paying_visitor_count) / total_visitor_count

print(baseline_percent)

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240 / average_payment)

percentage_point_increase = (100 * new_customers_needed) / total_visitor_count
print(percentage_point_increase)

minumum_detactable_effect = (percentage_point_increase / baseline_percent) * 100

print(minumum_detactable_effect)

ab_sample_size = 290