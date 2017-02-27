public class Solution {
    public int findComplement(int num) {
        String binary_num = Integer.toString(num, 2);

		String[] array_num = binary_num.split("");

		int[] ans_array = new int[array_num.length];
		for (int i = 0; i < array_num.length; i++) {
			if (Integer.parseInt(array_num[i]) == 1)
				ans_array[i] = 0;
			else
				ans_array[i] = 1;
		} 

		StringBuilder sb = new StringBuilder(ans_array.length);
		for (int i = 0; i < ans_array.length; i++) {
			sb.append(ans_array[i]);
		}

		String ans_string = sb.toString();

		int ans = Integer.parseInt(ans_string,2);
		
		return ans;
    }
}