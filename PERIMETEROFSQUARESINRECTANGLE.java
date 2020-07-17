/*Perimeter of squares in a rectangle
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 
Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing: 

#Hint: See Fibonacci sequence
#Ref: http://oeis.org/A000045
The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.
perimeter(5)  should return 80
perimeter(7)  should return 216
CODE#*/
import java.math.BigInteger;
public class SumFct {
	public static BigInteger perimeter(BigInteger n) {
		BigInteger a,temp,out,sum,i;
    a=BigInteger.valueOf(1);temp=BigInteger.valueOf(0);out=BigInteger.valueOf(0);
    sum  = BigInteger.valueOf(0);i = BigInteger.valueOf(0);
    while(i.compareTo(n)<0){ 
        out=a.add(temp);
        temp=a;
        a=out;
        sum=sum.add(out);
        i=i.add(BigInteger.valueOf(1));}
  return (sum.add(BigInteger.valueOf(1))).multiply(BigInteger.valueOf(4));
}}
