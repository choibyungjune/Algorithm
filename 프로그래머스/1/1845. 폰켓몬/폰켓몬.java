import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int numLength = nums.length / 2;
        HashSet<Integer> uniqueElements = new HashSet<>();
        for (int num : nums) {
            uniqueElements.add(num);
        }
        
        int uniqueElement  = uniqueElements.size();
        answer = Math.min(numLength, uniqueElement);
        
        return answer;
    }
}