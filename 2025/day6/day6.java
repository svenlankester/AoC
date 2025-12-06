package day6;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day6 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day6/data.txt").toPath(), Charset.defaultCharset());
        long total = 0;

        List<long[]> lines = new ArrayList<>();
        List<Character> operations = new ArrayList<>();

        for (char c : input.getLast().toCharArray()) {
            if (c != ' ') {
                operations.add(c);
            }
        }
        input.removeLast();

        for (String line : input) {
            lines.add(Arrays.stream(line.split("\\s+"))
                    .filter(s -> !s.isEmpty())
                    .mapToLong(Long::parseLong)
                    .toArray());
        }

        for (int i = 0; i < operations.size(); i++){
            long currtotal = operations.get(i) == '*' ? 1 : 0;
            for (long[] line : lines) {
                switch(operations.get(i)) {
                    case '*':
                        currtotal *= line[i];
                        break;
                    case '+':
                        currtotal += line[i];
                        break;
                }
            }
            total += currtotal;
        }

        System.out.println(total);
    }
}