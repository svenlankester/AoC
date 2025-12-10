package day10;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;

public class day10 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day10/data.txt").toPath(), Charset.defaultCharset());
        List<Machine> machines = new ArrayList<>();
        long total = 0;
        
        parse(input, machines);
        
        for (Machine machine : machines) {
            total += findFewestPresses(machine, new BitSet(machine.goal.size()), 0, 10, 0);
        }
        
        System.out.println(total);
    }
    
    static long findFewestPresses(Machine machine, BitSet curr, int startIdx, int maxDepth, int depth) {
        if (curr.equals(machine.goal)) return depth;
        if (depth == maxDepth) return 999999999;
        
        int buttonCount = machine.buttons.length;
        long min = 999999999;
        
        for (int i = startIdx; i < buttonCount; i++) {
            BitSet temp = (BitSet) curr.clone();
            temp.xor(machine.buttons[i]);
            long res = findFewestPresses(machine, temp, i, maxDepth, depth + 1);
            if (res < min) min = res;
        }
        return min;
    }
    
    
    static void parse(List<String> input, List<Machine> output) {
        for (String machine : input) {
            List<String> elems = new ArrayList<>(List.of(machine.split(" ")));
            // problem for part 2
            elems.removeLast();
            
            // goal parsing
            String goalString = elems.removeFirst();
            goalString = goalString.substring(1, goalString.length() - 1);
            BitSet goal = new BitSet(goalString.length());

            for (int i = 0; i < goalString.length(); i++) {
                if (goalString.charAt(i) == '#') goal.set(i);
            }

            // buttons parsing
            BitSet[] buttons = new BitSet[elems.size()];
            for (int i = 0; i < elems.size(); i++) {
                String buttonWiring = elems.get(i).substring(1, elems.get(i).length() - 1);
                int[] buttonIDs = Arrays.stream(buttonWiring.split(",")).mapToInt(Integer::parseInt).toArray();
                BitSet wiring = new BitSet(buttonIDs.length);
                for (int id : buttonIDs) wiring.set(id);
                buttons[i] = wiring;
            }

            output.add(new Machine(goal, buttons));
        }
    }
}

class Machine {
    BitSet goal;
    BitSet[] buttons;
    
    public Machine(BitSet goal, BitSet[] buttons) {
        this.goal = goal;
        this.buttons = buttons;
    }
    
}