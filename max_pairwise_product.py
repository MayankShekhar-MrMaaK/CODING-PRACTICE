# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    maxxx=max(numbers[0],numbers[1])
    maxx=min(numbers[0],numbers[1])
    for i in range(2,n):
    	if numbers[i]>=maxxx:
    		maxx=maxxx
    		maxxx=numbers[i]
    	else :
    		if numbers[i]>=maxx:
    			maxx=numbers[i]
    		else:
    			pass
    max_product=maxx*maxxx

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
