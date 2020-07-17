/*ISOGRAMS
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
isIsogram "Dermatoglyphics" == true
isIsogram "moose" == false
isIsogram "aba" == false
CODE#*/
public class isogram {
    public static boolean  isIsogram(String str) {
        int i=0,j=0;
        str=str.toLowerCase();
        char[] ch=str.toCharArray();
        for(i=0;i<str.length();i++)
        { for(j=i+1;j<str.length();++j)
          { 
            if(ch[i]==ch[j])
            {return false;}
    } 
}
return true;
}
}
