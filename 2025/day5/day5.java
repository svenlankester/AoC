package day5;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day5 {
    static void main() throws IOException {
        String input = Files.readString(new File("2025/day5/data.txt").toPath(), Charset.defaultCharset());
        String[] parseStep = input.split("(\\r?\\n){2}");

        String[] ranges = parseStep[0].split("\\r?\\n");
        List<Long> ids = Arrays.stream(parseStep[1].split("\\r?\\n"))
                .map(Long::parseLong)
                .toList();

        int total = 0;

        for (long id : ids) {
            for (String range : ranges) {
                String[] ends = range.split("-");
                long start = Long.parseLong(ends[0]);
                long end = Long.parseLong(ends[1]);

                if ((start <= id) && (end >= id)){
                    total++;
                    break;
                }
            }
        }

        System.out.println(total);
    }
}