package day9;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;
import java.awt.Point;
import java.awt.Polygon;
import java.awt.Rectangle;
import java.awt.geom.Area; // Import Area

public class day9_part2 {
     static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day9/data.txt").toPath(), Charset.defaultCharset());
        List<Point> tiles = input.stream().map(s -> new Point(Integer.parseInt(s.split(",")[0]), Integer.parseInt(s.split(",")[1]))).toList();

        int[] xPoints = new int[tiles.size()];
        int[] yPoints = new int[tiles.size()];

        for (int i = 0; i < tiles.size(); i++) {
            xPoints[i] = tiles.get(i).x;
            yPoints[i] = tiles.get(i).y;
        }
        
        Polygon shape = new Polygon(xPoints, yPoints, tiles.size());
        Area polygonArea = new Area(shape);

        long max = 0;
        for (Point a : tiles) {
            for (Point b : tiles) {
                if (a.equals(b)) continue;

                int x1 = Math.min(a.x, b.x);
                int y1 = Math.min(a.y, b.y);
                int width = Math.abs(a.x - b.x);
                int height = Math.abs(a.y - b.y);

                Rectangle rect = new Rectangle(x1, y1, width, height);
                
                if (shape.getBounds().contains(rect)) {
                    Area testArea = new Area(rect);
                    testArea.subtract(polygonArea);

                    if (testArea.isEmpty()) {
                        long size = ((long)width + 1) * ((long)height + 1);
                        if (size > max) max = size;
                    }
                }
            }
        }
        System.out.println(max);
    }
}