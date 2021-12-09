/// array of Us and Ds
/// where is D 1 step downward 
int countingValleys(int steps, string path) {
    int level = 0;
    int count = 0;
    for( int i=0;i<path.size();i++)
    {
        int plevel = level;
        if(path[i] == 'D')
            level--;
        else level++;
        
        if(level == 0 && plevel<0)
            count++;
    }
    
    return count;
}
