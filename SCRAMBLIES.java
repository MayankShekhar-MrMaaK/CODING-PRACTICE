/*SCRAMBLIES
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
CODE#*/
public class Scramblies {
    public static boolean scramble(String str1, String str2) {
    int i=0;
		boolean v=false;
		if(str1.length()>=str2.length()) { 
    while(i<str2.length())
		{
			if  (str1.contains(String.valueOf(str2.charAt(i)))) { 
				str1=str1.replaceFirst(String.valueOf(str2.charAt(i))," ");
				str1=str1.trim();
				v=true;}
			else { v=false;break;}
			i++;
		}}
		else v=false;
		return v;
    }
}
