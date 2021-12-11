void print_array(int n, vector<int> arr)
{
    for(int i = 0;i<n;i++)
    {
         cout<<arr[i]<<" ";
    }
    cout<<endl;
    
}
void insertionSort1(int n, vector<int> arr)
{
    int i = n-1;
    while (i>=1)
    {
        int item = arr[i];   
        int j = i-1;
        while (j>=0 && item<arr[j])
        {
            arr[j+1] = arr[j];
            print_array(n,arr);
            j--;
            
        }
        
        if(j+1 != i )
        {
            arr[j+1] = item; 
            print_array(n,arr);
        }else {
            i--;
        }
        
        
    }

}
