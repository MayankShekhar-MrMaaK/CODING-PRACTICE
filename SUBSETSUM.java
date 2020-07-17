/*Subset Sum Problem[DYNAMIC PROGRAMMING]
 * Problem Statement:-
 * Given a set of non-negative integers, and a value sum, 
 * determine if there is a subset of the given set with sum equal to given sum.
 * Example:
Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
 */
public class subsetsum {
	public static void main(String[] args) {
		int[] arr= {3, 34, 4, 12, 5, 2}; 
		int target=9;
		boolean[][] table=new boolean[arr.length+1][target+1];
		for(int i =0;i<=target;i++) 
			table[0][i]=false;
		for(int i =0;i<=arr.length;i++) 
			table[i][0]=true;
		for(int i=1;i<=arr.length;i++) {
			for(int j=1;j<=target;j++) {
				table[i][j]=table[i-1][j];//copying data from top
				if(table[i][j]==false&&j>=arr[i-1]) 
					table[i][j]= table[i][j] || table[i-1][j-arr[i-1]];
			}
		}
		System.out.println(table[arr.length][target]);
		}
}
/* TRUTH TABLE LOOKS LIKE
      0     1      2      3      4      5      6      7      8      9
0   true  false  false  false  false  false  false  false  false  false  
3   true  false  false  true   false  false  false  false  false  false  
34  true  false  false  true   false  false  false  false  false  false  
4   true  false  false  true   true   false  false  true   false  false  
12  true  false  false  true   true   false  false  true   false  false  
5   true  false  false  true   true   true   false  true   true   true  
2   true  false  true   true   true   true   true   true   true   true  
*/
