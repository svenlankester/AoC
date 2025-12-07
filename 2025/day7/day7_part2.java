package day7;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day7_part2 {

    List<String> input;
    Map<String, Long> cache = new HashMap<>();
    
    void main() throws IOException {
        input = Files.readAllLines(new File("2025/day7/data.txt").toPath(), Charset.defaultCharset());
        int startX = input.getFirst().indexOf('S');
        
        System.out.println(traverse(startX, 1));
    }

    long traverse(int startX, int startY) {
        String key = startX + "," + startY;
        
        if (cache.containsKey(key)) return cache.get(key);

        long result;

        if (startY == input.size() - 1) {
            result = 1;
        } else if (input.get(startY + 1).charAt(startX) == '.') {
            result = traverse(startX, startY + 1);
        } else {
            result = traverse(startX - 1, startY + 1)
                    + traverse(startX + 1, startY + 1);
        }

        cache.put(key, result);
        return result;
    }
}