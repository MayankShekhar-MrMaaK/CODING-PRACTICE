/*Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:
 
NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
NOTE 2: The 0x0 (empty matrix) is represented as [[]]
------------------------------------
CODE#*/
import java.util.Arrays;
public class Snail {
public static int[] snail(int[][] array) {
    if(array[0].length <= 0)  return new int[0];
    if(array[0].length == 1) { int[] j=new int[1]; j[0]=array[0][0];return j;}
    else{
    int m=array[0].length,k=0,l=0,n=array[1].length,j=0;
    String s="";
    while(k<m&&l<n)
		     {  
		         for(int i=k;i<m;i++) s=s+" "+array[k][i];
		         k++;
		         for(int i=k;i<n;i++) s=s+" "+(array[i][n-1]);
		         n--;
		         if(k<m)
		         {
		        	 for(int i=n-1;i>=l;--i) s=s+" "+(array[m-1][i]);
			         m--;
		         }
		         if(l<n)
		         {
		        	 for(int i=m-1;i>=k;--i) s=s+" "+(array[i][l]);
			         l++;
		         }
		     }
    s=s.trim();
    String[] stra=s.split(" ");
    int[] arra = Arrays.asList(stra).stream().mapToInt(Integer::parseInt).toArray();
    return arra;
   } 
  }
}
