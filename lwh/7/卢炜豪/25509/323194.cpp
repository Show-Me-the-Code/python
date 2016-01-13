import java.io.*;
import java.util.*;
public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new FileReader("marathon.in"));
    PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("marathon.out")));
    int n = Integer.parseInt(br.readLine());
    int[] x = new int[n];
    int[] y = new int[n];
    for(int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      x[i] = Integer.parseInt(st.nextToken());
      y[i] = Integer.parseInt(st.nextToken());
    }
    int totalDistance = 0;
    for(int i = 1; i < n; i++) {
      totalDistance += Math.abs(x[i] - x[i-1]) + Math.abs(y[i] - y[i-1]);
    }
    int largestSkip = 0;
    for(int i = 1; i < n-1; i++) {
      int noSkipDistance = Math.abs(x[i+1] - x[i]) + Math.abs(x[i] - x[i-1]) + Math.abs(y[i+1] - y[i]) + Math.abs(y[i] - y[i-1]);
      int skipDistance = Math.abs(x[i+1] - x[i-1]) + Math.abs(y[i+1] - y[i-1]);
      largestSkip = Math.max(largestSkip, noSkipDistance - skipDistance);
    }
    pw.println(totalDistance - largestSkip);
    pw.close();
  }
}