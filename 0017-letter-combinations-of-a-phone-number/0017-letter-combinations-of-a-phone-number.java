class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.length() == 0) return result;
        
        String[] digitToLetters = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        backtrack(digits, 0, new StringBuilder(), result, digitToLetters);
        return result;
    }
    
    private void backtrack(String digits, int index, StringBuilder current, List<String> result, String[] digitToLetters) {
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }
        
        String letters = digitToLetters[digits.charAt(index) - '0'];
        for (char letter : letters.toCharArray()) {
            current.append(letter);
            backtrack(digits, index + 1, current, result, digitToLetters);
            current.deleteCharAt(current.length() - 1);
        }
    }
}