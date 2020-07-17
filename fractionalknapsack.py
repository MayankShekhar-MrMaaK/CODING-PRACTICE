import sys
from collections import namedtuple
Item = namedtuple("Item", "value weight")
def get_optimal_value(capacity, weights, values):
	value=0
	weight_value_pairs = sorted([Item(v, w) for v, w in zip(values, weights)],key=lambda i: i.value / i.weight,reverse=True)
	current_weight=0
	final_value=0.0
	for i in weight_value_pairs:
		if current_weight+i.weight<=capacity:
			current_weight+=i.weight
			final_value+=i.value
		else:
			remain=capacity-current_weight
			final_value+=i.value*(remain/i.weight)
			break
	return final_value
capacity=50
values=[60,100,120]
weights=[20,50,30]
print(get_optimal_value(capacity,weights,values))