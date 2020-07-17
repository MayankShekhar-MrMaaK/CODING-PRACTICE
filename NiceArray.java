/*Nice Array
A Nice array is defined to be an array where for every value n in the array, there is also an element n-1 or n+1 in the array.
example:
[2,10,9,3] is Nice array because

2=3-1
10=9+1
3=2+1
9=10-1
Write a function named isNice/IsNice that returns true if its array argument is a Nice array, else false. You should also return false if input array has no elements. */

import java.util.ArrayList;
public class nicearray {
	public static void main(String[] args) {
	Integer[] arr= {2,10,9,3};
	System.out.println(st(arr));
	}
	private static boolean st(Integer[] arr) {
		 ArrayList<Integer> ar=new ArrayList<Integer>();
		 ArrayList<Integer> ar2=new ArrayList<Integer>();
		 for(int i=0;i<arr.length;i++)  ar.add(arr[i]);
		 for(int k=0;k<arr.length;k++) 
				if(ar.contains(arr[k]+1)||ar.contains(arr[k]-1)) ar2.add(arr[k])  ;
	     if(!(ar2.size()==arr.length)||arr.length==0) return false;
	     else  return true;
	} }
