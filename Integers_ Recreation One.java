package javas;
/*Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]*/
import java.util.ArrayList;
public class recreationinteger {

	public static void main(String[] args) {
		ArrayList<Long> divisors = new ArrayList<Long>();
        ArrayList<ArrayList<Long>> res = new ArrayList<ArrayList<Long>>();
        long m=1,n=42;
        for (long c = m; c <= n; c++)
        {
            divisors.clear();
            for (long i = 1; i <= c / 2; i++) 
            {
                if (c % i == 0) 
                    divisors.add(i);
            }
            divisors.add(c);
            long sum = new Long(0);
            for (int i = 0; i < divisors.size(); i++) {
                sum += (long) Math.pow(divisors.get(i).longValue(), 2);
            }
            Double d = new Double(Math.sqrt(sum));
            if (d.toString().substring(d.toString().indexOf('.')).equals(".0")) 
            {
                ArrayList<Long> r = new ArrayList<Long>();
                r.add(c);
                r.add(sum);
                res.add(r);
            }
        }
        System.out.println(res);
	}
}
