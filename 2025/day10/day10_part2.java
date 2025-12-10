import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;
import com.microsoft.z3.*;

public class day10_part2 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day10/data.txt").toPath(), Charset.defaultCharset());
        List<Machine> machines = new ArrayList<>();
        long total = 0;

        parse(input, machines);

        for (Machine machine : machines) {
            total += findFewestPresses(machine);
        }

        System.out.println(total);
    }

    static long findFewestPresses(Machine machine) {
        Context ctx = new Context();

        int numButtons = machine.buttons.size();
        int arrayLength = machine.goal.length;

        // Create integer variables for how many times to press each button
        IntExpr[] presses = new IntExpr[numButtons];
        for (int i = 0; i < numButtons; i++) {
            presses[i] = ctx.mkIntConst("press_" + i);
        }

        Optimize optimizer = ctx.mkOptimize();

        // Constraint 1: Each press count must be non-negative
        for (int i = 0; i < numButtons; i++) {
            optimizer.Add(ctx.mkGe(presses[i], ctx.mkInt(0)));
        }

        // Constraint 2: Sum of (presses[i] * button[i]) must equal goal
        for (int pos = 0; pos < arrayLength; pos++) {
            ArithExpr sum = ctx.mkInt(0);

            for (int i = 0; i < numButtons; i++) {
                ArithExpr contribution = ctx.mkMul(presses[i], ctx.mkInt(machine.buttons.get(i)[pos]));
                sum = ctx.mkAdd(sum, contribution);
            }

            optimizer.Add(ctx.mkEq(sum, ctx.mkInt(machine.goal[pos])));
        }

        // Objective: Minimize the total number of button presses
        ArithExpr totalPresses = ctx.mkInt(0);
        for (int i = 0; i < numButtons; i++) {
            totalPresses = ctx.mkAdd(totalPresses, presses[i]);
        }
        optimizer.MkMinimize(totalPresses);

        // Solve
        Status status = optimizer.Check();

        long result = 0;
        if (status == Status.SATISFIABLE) {
            Model model = optimizer.getModel();
            result = ((IntNum) model.eval(totalPresses, false)).getInt64();
        } else if (status == Status.UNSATISFIABLE) {
            // No solution exists, return 0 or handle as needed
            result = 0;
        }

        ctx.close();
        return result;
    }


    static void parse(List<String> input, List<Machine> output) {
        for (String machine : input) {
            List<String> elems = new ArrayList<>(List.of(machine.split(" ")));
            
            String joltageString = elems.removeLast();
            joltageString = joltageString.substring(1, joltageString.length() - 1);
            int[] goal = Arrays.stream(joltageString.split(",")).mapToInt(Integer::parseInt).toArray();

            elems.removeFirst();
            
            // buttons parsing
            List<int[]> buttons = new ArrayList<>();
            for (int i = 0; i < elems.size(); i++) {
                String buttonWiring = elems.get(i).substring(1, elems.get(i).length() - 1);
                int[] buttonIDs = Arrays.stream(buttonWiring.split(",")).mapToInt(Integer::parseInt).toArray();
                int[] buttonArray = new int[goal.length];
                for (int x : buttonIDs) buttonArray[x] = 1;
                buttons.add(buttonArray);
            }

            output.add(new Machine(goal, buttons));
        }
    }
}

class Machine {
    int[] goal;
    List<int[]> buttons;
    public Machine(int[] goal, List<int[]> buttons) {
        this.goal = goal;
        this.buttons = buttons;
    }

}