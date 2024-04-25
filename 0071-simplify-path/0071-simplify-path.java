class Solution {
    public String simplifyPath(String path) {
        var stack = new Stack<String>();
        var chars = path.toCharArray();
        var l = chars.length;
        if (l == 1)
            return path;

        var curr = new StringBuilder();
        // first item is always /
        for (int i = 1; i < l; i++) {
            var c = chars[i];
            if (c == '/') {
                addToStack(stack, curr);
                curr = new StringBuilder();
            } else
                curr.append(c);
        }

        if (curr.length() > 0)
            addToStack(stack, curr);

        return "/" + String.join("/", stack);
    }

    private void addToStack(Stack<String> stack, StringBuilder curr) {
        var str = curr.toString();
        if ("..".equals(str)) { // first item is /
            if (stack.size() > 0)
                stack.pop();
        } else if (!".".equals(str) && !"".equals(str)) {
            stack.push(str);
        }
    }
}