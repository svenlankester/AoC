package day3;

import java.io.*;
import java.util.*;

public class day3_part2 {
    static void main() throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("2025/day3/data.txt"));
        String line;
        long total = 0;
        List<String> banks = new ArrayList<>();
        while ((line = br.readLine()) != null) {
            banks.add(line);
        }

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