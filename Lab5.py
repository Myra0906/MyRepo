import java.util.*;
public class GraphComparison {
    static final int VERTICES = 500; 
    static final int MAX_DEGREE = 10; 
    public static void main(String[] args) {
        Random random = new Random();
        GraphMatrix graphMatrix = new GraphMatrix(VERTICES);
        GraphAdjList graphAdjList = new GraphAdjList(VERTICES);
        GraphArrayList graphArrayList = new GraphArrayList(VERTICES);

        for (int i = 1; i <= VERTICES; i++) {
            for (int j = 0; j < MAX_DEGREE; j++) {
                int neighbor = random.nextInt(VERTICES) + 1;
                if (i != neighbor) {
                    graphMatrix.addEdge(i, neighbor);
                    graphAdjList.addEdge(i, neighbor);
                    graphArrayList.addEdge(i, neighbor);
                }
            }
        }
        
        graphMatrix.printMatrix();
        
        measureTime(() -> graphMatrix.bfs(1), "BFS with Adjacency Matrix");
        measureTime(() -> graphAdjList.bfs(1), "BFS with Adjacency List");
        measureTime(() -> graphArrayList.bfs(1), "BFS with Array List");

        measureTime(() -> graphMatrix.dfs(1), "DFS with Adjacency Matrix");
        measureTime(() -> graphAdjList.dfs(1), "DFS with Adjacency List");
        measureTime(() -> graphArrayList.dfs(1), "DFS with Array List");
    }
    private static void measureTime(Runnable algorithm, String description) {
        long startTime = System.nanoTime();
        algorithm.run();
        long endTime = System.nanoTime();
        System.out.println(description + ": " + (endTime - startTime) / 1e6 + " ms");
    }
}
class GraphMatrix {
    private final int[][] matrix;
    private final int vertices;

    public GraphMatrix(int vertices) {
        this.vertices = vertices;
        this.matrix = new int[vertices + 1][vertices + 1];
    }

    public void addEdge(int u, int v) {
        matrix[u][v] = 1;
        matrix[v][u] = 1;
    }
    public void printMatrix(){
        for (int i=0; i<vertices; i++){
            for (int j=0; j<vertices; j++){
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
    }

    public void bfs(int start) {
        boolean[] visited = new boolean[vertices + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");
            for (int i = 1; i <= vertices; i++) {
                if (matrix[node][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
        System.out.println(); 
    }

    public void dfs(int start) {
        boolean[] visited = new boolean[vertices + 1];
        dfsHelper(start, visited);
        System.out.println(); 
    }

    private void dfsHelper(int node, boolean[] visited) {
        visited[node] = true;
        System.out.print(node + " "); // Print node
        for (int i = 1; i <= vertices; i++) {
            if (matrix[node][i] == 1 && !visited[i]) {
                dfsHelper(i, visited);
            }
        }
    }
}
class GraphAdjList {
    private final List<List<Integer>> adjList;

    public GraphAdjList(int vertices) {
        adjList = new ArrayList<>();
        for (int i = 0; i <= vertices; i++) {
            adjList.add(new ArrayList<>());
        }
    }

    public void addEdge(int u, int v) {
        adjList.get(u).add(v);
        adjList.get(v).add(u);
    }

    public void bfs(int start) {
        boolean[] visited = new boolean[adjList.size()];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " "); 
            for (int neighbor : adjList.get(node)) {
                if (!visited[neighbor]) {
                    queue.add(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
        System.out.println();
    }

    public void dfs(int start) {
        boolean[] visited = new boolean[adjList.size()];
        dfsHelper(start, visited);
        System.out.println(); 
    }

    private void dfsHelper(int node, boolean[] visited) {
        visited[node] = true;
        System.out.print(node + " "); 
        for (int neighbor : adjList.get(node)) {
            if (!visited[neighbor]) {
                dfsHelper(neighbor, visited);
            }
        }
    }
}

class GraphArrayList {
    private final List<Integer>[] arrayList;

    public GraphArrayList(int vertices) {
        arrayList = new ArrayList[vertices + 1];
        for (int i = 0; i <= vertices; i++) {
            arrayList[i] = new ArrayList<>();
        }
    }

    public void addEdge(int u, int v) {
        arrayList[u].add(v);
        arrayList[v].add(u);
    }

    public void bfs(int start) {
        boolean[] visited = new boolean[arrayList.length];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " "); 
            for (int neighbor : arrayList[node]) {
                if (!visited[neighbor]) {
                    queue.add(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
        System.out.println(); 
    }

    public void dfs(int start) {
        boolean[] visited = new boolean[arrayList.length];
        dfsHelper(start, visited);
        System.out.println(); 
    }

    private void dfsHelper(int node, boolean[] visited) {
        visited[node] = true;
        System.out.print(node + " ");
        for (int neighbor : arrayList[node]) {
            if (!visited[neighbor]) {
                dfsHelper(neighbor, visited);
            }
        }
    }
}