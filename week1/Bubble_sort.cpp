void countSwaps(vector<int> a) {
    
    bool swaped = true;
    int count = 0;
    while(swaped)
    {
        swaped = false;
        for(int i=0;i<a.size()-1;i++)
        {
            if(a[i+1]<a[i])
            {
                count++;
                swaped = true;
                
                // swape them
                int temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
            }
            
        }
        
    }
    cout<<"Array is sorted in "<< count <<" swaps."<<endl;
    cout<<"First Element: "<< a[0]<<endl;
    cout<<"Last Element: "<< a[a.size()-1] <<endl;
}
