import java.util.*;

class Process {
    int id;
    int at;
    int bt;

    Process(int id, int at, int bt) {
        this.id = id;
        this.at = at;
        this.bt = bt;
    }
}

public class FCFSWithoutSorting {
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

        int ct = 0;
        int totalTat = 0;
        int totalWt = 0;

        while (!arrivalQueue.isEmpty()) {
            Process process = arrivalQueue.poll();

            if (process.at > ct) {
                ct = process.at;
            }

            ct += process.bt;

            int tat = ct - process.at;
            int wt = tat - process.bt;
            totalTat += tat;
            totalWt += wt;

            System.out.println("Process " + process.id + " | Turnaround Time: " + tat + " | Waiting Time: " + wt);
        }
        double avgTat = (double) totalTat / n;
        double avgWt = (double) totalWt / n;

        System.out.println("\nAverage Turnaround Time: " + avgTat);
        System.out.println("Average Waiting Time: " + avgWt);

        sc.close();
    }
}
