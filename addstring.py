''' Add 2 numbers represented as string / Sum of two large numbers
Given two numbers as strings. The numbers may be very large (may not fit in long long int), the task is to find sum of these two numbers.
Examples:
Input  : str1 = "3333311111111111", 
         str2 =   "44422222221111"
Output : 3377733333332222

Input  : str1 = "7777555511111111", 
         str2 =    "3332222221111"
Output : 7780887733332222'''
def addstring(num1,num2):
	# n2 must be greater than n1
	if len(num1)>len(num2):
		temp=num1
		num1=num2
		num2=temp
	diff=len(num2)-len(num1)
	carry=0
	out=""
	#for sum
	for i in range(len(num1)-1,-1,-1):   
		sum=((ord(num1[i])-ord('0'))+int((ord(num2[i+diff])-ord('0'))) + carry) 
		out=out+str(sum%10)
		carry=sum//10
	# Add remaining digits of str2[] 
	for i in range(diff-1,-1,-1):
		sum=ord(num2[i])-ord('0')+carry
		out=out+str(sum%10)
		carry=sum//10
	if carry:
		out=out+str(carry)
	return out[::-1]
print (addstring("9","9"))
