package day2;

import java.io.*;
import java.util.*;
import java.util.stream.LongStream;

public class day2_part2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("2025/day2/data.txt"));
        String[] input = br.readLine().split(",");
        long total = 0;

        for (String entry : input) {
            long[] ends = Arrays.stream(entry.split("-")).mapToLong(Long::parseLong).toArray();
            total += LongStream.range(ends[0], ends[1] + 1).filter(num -> isInvalid(num)).sum();
        }

        System.out.println(total);
    }

    private static boolean isInvalid(long number) {
        return String.valueOf(number).matches("^(\\d+?)\\1+$");
    }
}