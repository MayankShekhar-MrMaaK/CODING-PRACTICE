/*SIMPLE PIG LATIN
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples
Kata.PigIt("Pig latin is cool"); // igPay atinlay siay oolcay
Kata.PigIt("Hello world !");     // elloHay orldway !
CODE#*/
public class PigLatin {
    public static String pigIt(String str) {
		String out="";
		String[] s=str.split(" ");
		for(int i=0;i<s.length;i++)
		{   String sa=s[i];
			  char s1=sa.charAt(0);
			  if(sa.contains("!")||sa.contains("?")) {
				    out=out+" "+s1;
				    continue;}
			  sa=sa.substring(1,sa.length());
			  sa=sa+s1+"ay";
			  out=out+" "+sa;
			  out=out.trim();
		}
		return out;
    }
}
