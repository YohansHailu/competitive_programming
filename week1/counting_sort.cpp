vector<int> countingSort(vector<int> arr) {
    vector<int> count(100,0);
    for(int i=0;i<arr.size();i++)
    {
        count[arr[i]]++;
        
    }

    return count;
}
