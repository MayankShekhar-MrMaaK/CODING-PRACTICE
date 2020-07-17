public class cows { 
    public static void main(String[] args){
		int arr[]={1,2,4,8,9,12,16};
		int c=4, n=arr.length, best=0;
		int high=arr[n-1], low=arr[0], mid;
		while (low<=high){
			mid=(low+high+1)/2;
			int left=0,cnt=1;
			for (int i=1; i<n&&cnt<c; i++){
				if (arr[i]-arr[left]>=mid){
					left=i;
					cnt++;
				}
			}
			if (cnt>=c){
				best=mid;
				low=mid+1;
			}
			else
				high=mid-1;
		}
		System.out.println(best);
	}
}