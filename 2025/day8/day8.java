package day8;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day8 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day8/data.txt").toPath(), Charset.defaultCharset());
        List<Box> boxes = new ArrayList<>();
        List<List<Box>> circuits = new ArrayList<>();
        
        // initialize circuits as each box separately
        for (String box : input) {
            int[] boxLoc = Arrays.stream(box.split(",")).mapToInt(Integer::parseInt).toArray();
            Box newBox = new Box(boxLoc[0], boxLoc[1], boxLoc[2]);
            boxes.add(newBox);
            circuits.add(new ArrayList<>(List.of(newBox)));
        }

        // crude assumption that no 2 items have the exact same distance, spares me from having to track individual connections
        double lastShortestDist = 0;
        for (int i = 0; i < 1000; i ++) {
            double shortestDist = 999999999;
            Box toConnect1 = null;
            Box toConnect2 = null;

            for (Box box1 : boxes) {
                for (Box box2 : boxes) {
                    // skip same box
                    if (box1.equals(box2)) continue;

                    double dist = box1.dist(box2);
                    if ((dist < shortestDist) && (lastShortestDist < dist)) {
                        toConnect1 = box1;
                        toConnect2 = box2;
                        shortestDist = dist;
                    }
                }
            }

            lastShortestDist = shortestDist;

            mergeCircuits(toConnect1, toConnect2, circuits);
        }
        
        List<Integer> circuitSizes = circuits.stream().map(List::size).sorted(Comparator.reverseOrder()).toList();
        System.out.println(circuitSizes.get(0) * circuitSizes.get(1) * circuitSizes.get(2));
    }
    
    static void mergeCircuits(Box b1, Box b2, List<List<Box>> circuits) {
        int c1 = -1;
        int c2 = -1;
        for (int i = 0; i < circuits.size(); i++) {
            if (circuits.get(i).contains(b1)) c1 = i;
            if (circuits.get(i).contains(b2)) c2 = i;
        }
        // boxes are in same circuit
        if (c1 == c2) return;
        
        circuits.get(c1).addAll(circuits.get(c2));
        circuits.remove(c2);
    }
}

class Box {
    int x;
    int y;
    int z;
    
    public Box(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    
    public double dist(Box b) {
        return (Math.sqrt(
                Math.pow((this.x - b.x), 2) +
                Math.pow((this.y - b.y), 2) +
                Math.pow((this.z - b.z), 2)
        ));
    }
    public boolean equals(Box b) {
        return (this.x == b.x) && (this.y == b.y) && (this.z == b.z);
    }
}