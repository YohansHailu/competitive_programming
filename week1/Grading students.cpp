vector<int> gradingStudents(vector<int> grades) {
    
    for(int i = 0;i<grades.size();i++)
    {
        if(grades[i]<38)
            continue;
            
        int count = 0;
        while(count<2 &&grades[i]%5 != 0)
        {
            grades[i]++;
            count++;
        }
        if(grades[i]%5  != 0  )
        {
            grades[i] -= 2;
        }
        
        
    }

    return grades;
}
