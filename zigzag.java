public class zigzag
{
	public static void main(String[] args){
		String out=convert("PAYPALISHIRING",3);
		System.out.print(out);
	}
	public static String convert(String s, int numRows){
		char[] arr= new char[s.length()];
		int count=0, interval = 2*numRows-2;
		for (int i=0;i<numRows;i++){
			int step=interval-2*i;
			for (int j=i;j<s.length();j+=interval){
				arr[count]=s.charAt(j);
				count++;
				if (step>0 && step<interval && j+step<interval){
					arr[count]=s.charAt(j+step);
					count++;
				}
			}
		}
		return new String(arr);
	}
}