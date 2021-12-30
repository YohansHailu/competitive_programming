class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        int in = matrix.size();
        int jn = matrix[0].size();
        vector<int> result;

        int jend = jn-1;
        int iend = in-1;
        int start=0;
        while( start <= iend&&jend>=start)
        {

          int i = start; int j = start;
          if(i==start && j==start){
            for(;j<jend;j++)
            {
              result.push_back(matrix[i][j]);
            }
          }

          if(i==start && j==jend) {
            for(;i<iend;i++)
            {
              result.push_back(matrix[i][j]);
            }
          }

          if(i==iend && j==jend) {
            for(;j>start;j--)
            {
              result.push_back(matrix[i][j]);
            }
          }

          if(i==iend && j==start) {
            for(;i>start;i--)
            {
              result.push_back(matrix[i][j]);
            }
          }
          if(start==jend)
              result.push_back(matrix[i][j]);
          start++;
          jend--;
          iend--;
        }
        result.resize(in*jn);
        return result;
        
    }
};
