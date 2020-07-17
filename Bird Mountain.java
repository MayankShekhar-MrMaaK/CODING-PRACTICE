/*Kata Task
A bird flying high above a mountain range is able to estimate the height of the highest peak.

Can you?

Example
The birds-eye view
^^^^^^
 ^^^^^^^^
  ^^^^^^^
  ^^^^^
  ^^^^^^^^^^^
  ^^^^^^
  ^^^^
The bird-brain calculations
111111
 1^^^^111
  1^^^^11
  1^^^1
  1^^^^111111
  1^^^11
  1111
  ----------------------------
111111
 12222111
  12^^211
  12^21
  12^^2111111
  122211
  1111
  ------------------------------
111111
 12222111
  1233211
  12321
  12332111111
  122211
  1111
Height = 3*/
public class birdmountain {
	public static void main(String[] args) {
		char[][] mountains={
			      "^^^^^^        ".toCharArray(),
			      " ^^^^^^^^     ".toCharArray(),
			      "  ^^^^^^^     ".toCharArray(),
			      "  ^^^^^       ".toCharArray(),
			      "  ^^^^^^^^^^^ ".toCharArray(),
			      "  ^^^^^^      ".toCharArray(),
			      "  ^^^^        ".toCharArray()
			    };      
		int my=mountains.length;
		int mx=mountains[0].length;
		char[][] arr=mountains.clone();
		int height=0;
		boolean f;
		do {
			f=false;
			char[][] next=new char[my][mx];
			for (int y = 0; y < my; y++) 
			{
		        for (int x = 0; x < mx; x++) 
		        {
		          next[y][x] = arr[y][x];
		          if (arr[y][x] == '^' && (y == 0 ||  x == 0 || y == my-1 || x == mx-1 ||
		            arr[y-1][x] == ' ' || arr[y+1][x] == ' ' || arr[y][x-1] == ' ' || arr[y][x+1] == ' ')) 
		          		{
				            f = true;
				            next[y][x] = ' ';
				          }
		        	}
		      }
		if(f) { height++; arr=next;}
		}while (f);
		System.out.println(height);
	}

}
