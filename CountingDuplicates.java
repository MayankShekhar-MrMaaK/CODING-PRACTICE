/*Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
CODE#*/
public class CountingDuplicates {
  public static int duplicateCount(String text) {
    int i=0,j=0,c=0,a=0;
    text=text.toLowerCase();
    for(i=0;i<text.length();i++)
    {for(j=0;j<text.length();j++)
    {
      if(text.charAt(i)==text.charAt(j))
      {c++;}
    }
    if(c>1){a++;}
    String d= String.valueOf(text.charAt(i)).trim();
    text=text.replaceAll(d,"");
    c=0;
    i=0;
    j=0;
    }
  return a;
}
}
