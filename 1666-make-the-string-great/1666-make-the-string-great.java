class Solution {
    public String makeGood(String s) {
        if (s.length() == 1) return s;
        var stack = new StringBuilder();

        var chars = s.toCharArray();

        for (var c : chars) {
          // 65 - A
          // 97 - a
          // diff - 32
          if (stack.length() > 0) {
            if (Math.abs((int) c - (int) stack.charAt(stack.length() - 1)) == 32) {
              stack.deleteCharAt(stack.length() - 1);
            } else stack.append(c);
          } else stack.append(c);
        }

        return stack.toString();
    }
}