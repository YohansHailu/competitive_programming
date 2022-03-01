class Solution:
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        for i in range(len(employees)):
            if id == employees[i].id:
                index = i 
                
        sub_sum = 0 
        for sub_id in employees[index]. subordinates:
            sub_sum += self.getImportance(employees, sub_id)
        
        return employees[index].importance + sub_sum
        
