package day3;

import java.io.*;
import java.util.*;

public class day3 {
    static void main() throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("2025/day3/data.txt"));
        String line;
        int total = 0;
        List<String> banks = new ArrayList<>();
        while ((line = br.readLine()) != null) {
            banks.add(line);
        }

        for (String bank : banks) {
            int firstNum = Arrays.stream(bank.substring(0, bank.length() - 1)
                    .chars()
                    .map(x -> x - 48)
                    .toArray())
                    .max()
                    .orElse(0);

            int secondNum = Arrays.stream(bank.substring(bank.indexOf((char)firstNum + 48) + 1)
                    .chars()
                    .map(x -> x - 48)
                    .toArray())
                    .max()
                    .orElse(0);

            total += Integer.parseInt(firstNum + "" + secondNum);
        }

        System.out.println(total);
    }

}