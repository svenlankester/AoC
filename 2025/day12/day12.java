package day12;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day12 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day12/data.txt").toPath(), Charset.defaultCharset());
        int total = 0;

        // puzzle input is kind this year
        input = input.subList(30, input.size());
        for (String line : input) {
            int width = Integer.parseInt(line.substring(0, 2));
            int height = Integer.parseInt(line.substring(3, 5));

            int blockCount = Arrays.stream(line.substring(7).split(" ")).mapToInt(Integer::parseInt).sum();
            int areaSizeBlocks = (width / 3) * (height / 3);
            if (blockCount <= areaSizeBlocks) total++;
        }

        System.out.println(total);
    }
}