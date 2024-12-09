import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class AdjacencyMatrixGraph {
    private static final int VERTICES = 500; // Оройн тоо
    private static final int MAX_DEGREE = 10; // Орой бүрийн дээд зэрэг
    private int[][] adjacencyMatrix;

    // Граф үүсгэх (санамсаргүй холболттой)
    public AdjacencyMatrixGraph() {
        adjacencyMatrix = new int[VERTICES][VERTICES];
        Random random = new Random();
        
        for (int i = 0; i < VERTICES; i++) {
            int degree = random.nextInt(MAX_DEGREE) + 1; // 1-ээс 10 хооронд
            for (int j = 0; j < degree; j++) {
                int neighbor = random.nextInt(VERTICES);
                if (i != neighbor && adjacencyMatrix[i][neighbor] == 0) {
                    adjacencyMatrix[i][neighbor] = 1;
                    adjacencyMatrix[neighbor][i] = 1; // Чиглэлгүй граф
                }
            }
        }
    }

    // BFS алгоритм
    public void bfs(int start) {
        boolean[] visited = new boolean[VERTICES];
        Queue<Integer> queue = new LinkedList<>();
        
        visited[start] = true;
        queue.add(start);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int neighbor = 0; neighbor < VERTICES; neighbor++) {
                if (adjacencyMatrix[current][neighbor] == 1 && !visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
    }

    // DFS алгоритм
    public void dfs(int current, boolean[] visited) {
        visited[current] = true;
        for (int neighbor = 0; neighbor < VERTICES; neighbor++) {
            if (adjacencyMatrix[current][neighbor] == 1 && !visited[neighbor]) {
                dfs(neighbor, visited);
            }
        }
    }

    // Гүйцэтгэлийн хугацаа хэмжих
    public static void main(String[] args) {
        AdjacencyMatrixGraph graph = new AdjacencyMatrixGraph();

        // BFS хугацааг хэмжих
        long startTime = System.nanoTime();
        graph.bfs(0); // Эхний оройг 0 гэж үзнэ
        long endTime = System.nanoTime();
        System.out.printf("BFS хугацаа: %.6f секунд%n", (endTime - startTime) / 1e9);

        // DFS хугацааг хэмжих
        boolean[] visited = new boolean[VERTICES];
        startTime = System.nanoTime();
        graph.dfs(0, visited); // Эхний оройг 0 гэж үзнэ
        endTime = System.nanoTime();
        System.out.printf("DFS хугацаа: %.6f секунд%n", (endTime - startTime) / 1e9);
    }
}
