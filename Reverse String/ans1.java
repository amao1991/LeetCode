public class Solution {
    public String reverseString(String s) {
		char[] b = s.toCharArray();
		char[] reverseArray = new char[b.length];
		
		for (int i = 0; i < b.length; i++){
			reverseArray[b.length - 1 - i] = b[i];
		}
		String ans = new String(reverseArray);
		return ans;
    }
}