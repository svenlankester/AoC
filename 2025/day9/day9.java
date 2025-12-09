package day9;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;
import java.awt.Point;

public class day9 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day9/data.txt").toPath(), Charset.defaultCharset());
        List<Point> tiles = input.stream().map(s -> new Point(Integer.parseInt(s.split(",")[0]), Integer.parseInt(s.split(",")[1]))).toList();
        
        long max = 0;
        for (Point a : tiles) {
            for (Point b : tiles) {
                if (a.equals(b)) continue;
                
                long size = (Math.abs((long)a.x - (long)b.x) + 1) * (Math.abs((long)a.y - (long)b.y) + 1);
                if (size > max) max = size;
            }
        }
        
        System.out.println(max);

    }
}