package day1;

import java.io.*;
import java.util.*;

public class day1 {
    static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("2025/day1/data.txt"));
        String line;
        List<String> input = new ArrayList<>();

        int max = 100;
        int curr = 50;
        int count = 0;

        while ((line = br.readLine()) != null) {
            input.add(line);
        }

        for (String s : input) {
            char dir = s.charAt(0);
            int size = Integer.parseInt(s.substring(1));

            if (dir == 'L') curr = modulus((curr - size), max);
            else curr = modulus((curr + size), max);
            
            if (curr == 0) count++;
        }

        System.out.println(count);
        br.close();
    }

    private static int modulus(int l, int r) {
        return (((l % r) + r) % r);
    }
}