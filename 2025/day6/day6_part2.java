package day6;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day6_part2 {
    static void main() throws IOException {
        List<char[]> input = new LinkedList<>(Files.readAllLines(new File("2025/day6/data.txt").toPath(), Charset.defaultCharset()).stream().map(String::toCharArray).toList());
        long total = 0;

        List<Character> operations = new ArrayList<>();

        for (char c : input.getLast()) {
            if (c != ' ') {
                operations.add(c);
            }
        }
        input.removeLast();

        List<Integer> nums = new ArrayList<>();

        for (int i = input.getFirst().length - 1; i >= 0; i--) {
            // construct num
            StringBuilder newNum = new StringBuilder();
            for (char[] line : input) {
                newNum.append(line[i]);
            }

            // Process if empty column found
            String num = newNum.toString().strip();
            if (!num.isEmpty()) {
                nums.add(Integer.parseInt(num));
            }
            // empty column found or at the end -> process all numbers
            if (num.isEmpty() || (i == 0)){
                char op = operations.getLast();
                operations.removeLast();

                long currtotal = op == '*' ? 1 : 0;
                for (int x : nums) {
                    switch(op) {
                        case '*':
                            currtotal *= x;
                            break;
                        case '+':
                            currtotal += x;
                            break;
                    }
                }
                total += currtotal;
                nums = new ArrayList<>();
            }

        }

        System.out.println(total);
    }
}