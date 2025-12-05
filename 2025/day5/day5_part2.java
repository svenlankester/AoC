package day5;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day5_part2 {
    static void main() throws IOException {
        String input = Files.readString(new File("2025/day5/data.txt").toPath(), Charset.defaultCharset());
        String[] parseStep = input.split("(\\r?\\n){2}");

        List<String> ranges = new ArrayList<>(Arrays.asList(parseStep[0].split("\\r?\\n")));
        List<String> mergedRanges = new ArrayList<>();
        long total = 0;

        ranges.sort(Comparator.comparingLong(s -> Long.parseLong(s.substring(0, s.indexOf('-')))));

        long currentStart = -1;
        long currentEnd = -1;

        for (String range : ranges) {
            String[] parts = range.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);

            if (currentStart == -1) {
                currentStart = start;
                currentEnd = end;
                continue;
            }

            if (start <= currentEnd + 1) {
                currentEnd = Math.max(currentEnd, end);
            }
            else {
                mergedRanges.add(currentStart + "-" + currentEnd);
                currentStart = start;
                currentEnd = end;
            }
        }

        mergedRanges.add(currentStart + "-" + currentEnd);

        for (String range : mergedRanges) {
            String[] ends = range.split("-");
            long start = Long.parseLong(ends[0]);
            long end = Long.parseLong(ends[1]);

            total += end - start + 1;
        }

        System.out.println(total);
    }
}