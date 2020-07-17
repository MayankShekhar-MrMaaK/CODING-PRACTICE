/*Square Every Digit
Welcome. In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
CODE#*/
import java.util.LinkedList;
public class SquareDigit {

  public int squareDigits(int n) {
    String concat="";
    LinkedList<Integer> stack = new LinkedList<Integer>();
    while(n>0)
    { stack.push(n%10);
      n=n/10;
    }
    while(!stack.isEmpty())
    { 
        n=(int) Math.pow(stack.pop(),2);
        concat+= Integer.toString(n);
    }
    return Integer.parseInt(concat);
  }
}
