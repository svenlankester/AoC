package day11;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.*;
import org.jgrapht.*;
import org.jgrapht.graph.*;
import org.jgrapht.nio.*;
import org.jgrapht.nio.dot.*;
import org.jgrapht.traverse.*;


public class day11_part2 {
    static void main() throws IOException {
        List<String> input = Files.readAllLines(new File("2025/day11/data.txt").toPath(), Charset.defaultCharset());

        HashMap<String, List<String>> connections = new LinkedHashMap<>();

        for (String line : input) {
            String key = line.substring(0, 3);
            List<String> val = List.of(line.substring(5).split(" "));
            connections.put(key, val);
        }

        Graph<String, DefaultEdge> g = new DefaultDirectedGraph<>(DefaultEdge.class);

        // first add all vertices
        g.addVertex("out");
        for (String s : connections.keySet()) g.addVertex(s);

        for (String key : connections.keySet()) {
            for (String output : connections.get(key)) {
                g.addEdge(key, output);
            }
        }
        
        System.out.println(countPaths(g, "svr", "dac") * countPaths(g, "dac", "fft") * countPaths(g, "fft", "out") +
                countPaths(g, "svr", "fft") * countPaths(g, "fft", "dac") * countPaths(g, "dac", "out"));
    }

    static long countPaths(Graph<String, DefaultEdge> g, String source, String target) {
        TopologicalOrderIterator<String, DefaultEdge> topoIterator = new TopologicalOrderIterator<>(g);
        List<String> topoOrder = new ArrayList<>();
        topoIterator.forEachRemaining(topoOrder::add);
        
        HashMap<String, Long> pathCount = new HashMap<>();
        pathCount.put(source, (long) 1);

        for (String v : topoOrder) {
            if (!pathCount.containsKey(v)) continue;
            long count = pathCount.get(v);

            for (DefaultEdge e : g.outgoingEdgesOf(v)) {
                String next = g.getEdgeTarget(e);
                pathCount.put(next, pathCount.getOrDefault(next, 0L) + count);
            }
        }

        return pathCount.getOrDefault(target, 0L);
    }
}