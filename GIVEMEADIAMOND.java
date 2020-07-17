/*Give me a Diamond
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.
Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
Examples
A size 3 diamond:
 *
***
 *
...which would appear as a string of " *\n***\n *\n"
A size 5 diamond:
  *
 ***
*****
 ***
  *
...that is: " *\n ***\n*****\n ***\n *\n"
CODE#*/
class Diamond {
  public static String print(int n) {
  String str="";
  int i=1,j=1;
  if((n%2==0)||n<0){return null;}
  else{
  for(i=1;i<=((n+1)/2);i++)
   {   for(j=1;j<=((n+1)/2-i);j++)
         str=str.concat(" ");   
       for(j=1;j<=(2*i-1);j++)
         str=str.concat("*");   
       str=str.concat("\n");
    }
    for(i=((n+1)/2-1);i>=1;i--)
    {
       for(j=1;j<=((n+1)/2-i);j++)
         str=str.concat(" ");
       for(j=1;j<=2*i-1;j++)
         str=str.concat("*");
       str=str.concat("\n");
    }}
    return str;}}
