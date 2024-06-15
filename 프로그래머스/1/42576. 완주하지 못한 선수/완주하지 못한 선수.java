import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> participantMap = new HashMap<>();
        
        for (String part : participant) {
            participantMap.put(part, participantMap.getOrDefault(part, 0) + 1);

        }
        
        for (String comp : completion) {
            participantMap.put(comp, participantMap.getOrDefault(comp, 0) - 1);
        }
        
        for (Map.Entry<String, Integer> entry : participantMap.entrySet()){
            if (entry.getValue() > 0){
                return entry.getKey();
            }
        }
        
        return "";
        
        
        
    }
}