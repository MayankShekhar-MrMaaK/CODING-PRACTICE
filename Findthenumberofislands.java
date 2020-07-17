/*
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands
Example:
Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1} 
Output : 5
CODE:-*/
public class island {
	 static final int ROW = 5, COL = 5; 
	public static void main(String[] args) {
	
		 int m[][] = new int[][] { { 1, 1, 0, 0, 0 }, 
             { 0, 1, 0, 0, 1 }, 
             { 1, 0, 0, 1, 1 }, 
             { 0, 0, 0, 0, 0 }, 
             { 1, 0, 1, 0, 1 } }; 
         System.out.println("Number of Island are "+count(m));
         

	}
	 static int count(int m[][])
	{	int c=0;
		boolean visited[][]=new boolean[ROW][COL];
		for(int i=0;i<ROW;i++)
			for(int j=0;j<COL;j++)
			{if(m[i][j]==1&&!visited[i][j])
				{
					DFS(m,i,j,visited);
					++c;
				}
			}
		return c;
	}
	 static void DFS(int m[][],int row,int col,boolean[][] visited)
	 {
		 int r[]= {0,0,-1,-1,-1,1,1,1};
		 int c[]= {1,-1,0,-1,1,0,-1,1};
		 visited[row][col]=true;
		 for(int k=0;k<8;++k) 
		 {	
		    if(isTrue(m,row+r[k],col+c[k],visited))
		    	DFS(m,row+r[k],col+c[k],visited);
		 }
		 
	 }
	 static boolean isTrue(int m[][],int row,int col,boolean[][] visited) {
		return row>0&&row<ROW&&col>0&&col<COL&&(m[row][col]==1&&!visited[row][col]);
	}
}
