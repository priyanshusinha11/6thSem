import java.util.*;

class Process {
    int id;
    int at;
    int bt;
    int rt;

    Process(int id, int at, int bt) {
        this.id = id;
        this.at = at;
        this.bt = bt;
        this.rt = bt;
    }
}

public class PreemptiveSJF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Process> arrivalQueue = new LinkedList<>();
        System.out.println("Enter the number of processes:");
        int n = sc.nextInt();
        System.out.println("Enter the arrival and burst time:");
        for (int i = 0; i < n; i++) {
            int at = sc.nextInt();
            int bt = sc.nextInt();
            arrivalQueue.add(new Process(i, at, bt));
        }

        PriorityQueue<Process> processQueue = new PriorityQueue<>(Comparator.comparingInt(p -> p.rt));
        int currentTime = 0;
        int completed = 0;
        int totalTat = 0;
        int totalWt = 0;

        while (completed < n) {
            while (!arrivalQueue.isEmpty() && arrivalQueue.peek().at <= currentTime) {
                processQueue.add(arrivalQueue.poll());
            }

            if (processQueue.isEmpty()) {
                currentTime++;
                continue;
            }

            Process currentProcess = processQueue.poll();
            int executionTime = Math.min(currentProcess.rt, 1);
            currentProcess.rt -= executionTime;
            currentTime += executionTime;

            if (currentProcess.rt == 0) {
                completed++;
                int tat = currentTime - currentProcess.at;
                int wt = tat - currentProcess.bt;
                totalTat += tat;
                totalWt += wt;
                System.out.println(
                        "Process " + currentProcess.id + " | Turnaround Time: " + tat + " | Waiting Time: " + wt);
            } else {
                processQueue.add(currentProcess);
            }
        }

        double avgTat = (double) totalTat / n;
        double avgWt = (double) totalWt / n;

        System.out.println("\nAverage Turnaround Time: " + avgTat);
        System.out.println("Average Waiting Time: " + avgWt);

        sc.close();
    }
}
