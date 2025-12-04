package day4;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;
import java.awt.Point;

public class day4_part2 {

    static List<Point> adjacencyMatrix = new ArrayList<>(Arrays.asList(
            new Point(-1, -1), new Point(0,-1), new Point (1, -1),
            new Point(-1, 0),                       new Point (1, 0),
            new Point(-1, 1), new Point(0,1), new Point (1, 1)
    ));

    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day4/data.txt").toPath(), Charset.defaultCharset());
        int total = 0;
        boolean removed = true;

        while (removed) {
            removed = false;
            for (int i = 0; i < input.size(); i++) {
                for (int j = 0; j < input.getFirst().length(); j++) {
                    if (input.get(i).charAt(j) == '@') {
                        if (isAccessible(input, j, i)) {
                            StringBuilder newLine = new StringBuilder(input.get(i));
                            newLine.setCharAt(j, '.');
                            input.set(i, newLine.toString());
                            removed = true;
                            total++;
                        }
                    }
                }
            }
        }

        System.out.println(total);
    }

    static boolean isAccessible(List<String> input, int x, int y) {
        int total = 0;

        for (Point p : adjacencyMatrix) {
            int newX = x + p.x;
            int newY = y + p.y;

            if (0 <= newY && newY < input.size() && 0 <= newX && newX < input.getFirst().length()) {
                if (input.get(newY).charAt(newX) == '@') total++;
            }
        }

        return total < 4;
    }
}