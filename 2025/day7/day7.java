package day7;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day7 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day7/data.txt").toPath(), Charset.defaultCharset());
        int total = 0;
        
        Set<Integer> prevBeams = new HashSet<>();
        prevBeams.add(input.getFirst().indexOf('S'));
        Set<Integer> newBeams = new HashSet<>();
        
        for (int i = 1; i < input.size(); i++) {
            List<Integer> splitters = new ArrayList<>();
            String currLine = input.get(i);
            
            //get indices of splitters
            for (int c = 0; c < currLine.length(); c ++) {
                if (currLine.charAt(c) == '^') splitters.add(c);
            }
            
            for (int beam : prevBeams) {
                if (splitters.contains(beam)) {
                    // based on input there are no splitters on edges, otherwise add check for edge
                    newBeams.add(beam + 1);
                    newBeams.add(beam - 1);
                    total++;
                }
                else {
                    newBeams.add(beam);
                }
            }
            
            prevBeams = new HashSet<>(newBeams);
            newBeams = new HashSet<>();
        }

        System.out.println(total);
    }
}