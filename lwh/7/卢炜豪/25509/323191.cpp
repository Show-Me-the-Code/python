(Analysis by Nick Wu)

Our first instinct when trying to figure out which point to skip is to try all of them. If we choose to skip each point and compute the new distance directly, then it takes about N operations to compute the distance and there are about N points to check, giving us an algorithm which runs in about N operations. This will be too slow when N gets to be 100,000.

Let's take a closer look at what happens when you skip a specific point. If we number the points from 1 to N, and skip point K, then the path we take goes from point 1 to point K−1, then from point K−1 to point K+1, and then from point K+1 to point N. The distance of this path is exactly equal to the following:

(total distance without skipping any points) - (distance between points K−1 and K) - (distance between points K and K+1) + (distance between points K−1 and K+1).

If we compute the total distance without skipping any points beforehand, then figuring out how long the path is when we want to skip a specific point no longer requires N operations! It only requires a constant number of operations, and that will be fast enough.

Here is my Java code:

import java.io.*;
import java.util.*;
public class marathon {
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