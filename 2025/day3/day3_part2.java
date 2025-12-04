package day3;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day3_part2 {
    static void main() throws IOException {
        List<String> banks = Files.readAllLines(new File("2025/day3/data.txt").toPath(), Charset.defaultCharset());
        long total = 0;

        for (String bank : banks) {

            StringBuilder ans = new StringBuilder();

            for (int i = 11; i >= 0; i--) {
                int num = Arrays.stream(bank.substring(0, bank.length() - i)
                        .chars()
                        .map(x -> x - 48)
                        .toArray())
                        .max()
                        .orElse(0);
                ans.append(num);
                bank = bank.substring(bank.indexOf((char)num + 48) + 1);
            }
            total += Long.parseLong(ans.toString());
        }
        System.out.println(total);
    }

}