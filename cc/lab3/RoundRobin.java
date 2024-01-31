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

public class RoundRobin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Process> processes = new ArrayList<>();
        System.out.println("Enter the number of processes:");
        int n = sc.nextInt();
        System.out.println("Enter the arrival and burst time for each process:");
        for (int i = 0; i < n; i++) {
            int at = sc.nextInt();
            int bt = sc.nextInt();
            processes.add(new Process(i, at, bt));
        }

        System.out.println("Enter the time quantum:");
        int quantum = sc.nextInt();

        roundRobin(processes, quantum);

        sc.close();
    }

    public static void roundRobin(List<Process> processes, int quantum) {
        int n = processes.size();
        int[] wt = new int[n];
        int[] tat = new int[n];

        int totalWt = 0;
        int totalTat = 0;

        int currentTime = 0;

        Queue<Process> queue = new LinkedList<>();
        for (Process p : processes) {
            queue.add(p);
        }

        while (!queue.isEmpty()) {
            Process currentProcess = queue.poll();
            if (currentProcess.rt > quantum) {
                currentTime += quantum;
                currentProcess.rt -= quantum;
                queue.add(currentProcess);
            } else {
                currentTime += currentProcess.rt;
                currentProcess.rt = 0;
                // Calculate turnaround time and waiting time when a process completes
                tat[currentProcess.id] = currentTime - currentProcess.at;
                wt[currentProcess.id] = tat[currentProcess.id] - currentProcess.bt;
                totalTat += tat[currentProcess.id];
                totalWt += wt[currentProcess.id];
            }
            // Update arrival times for new processes
            for (Process p : processes) {
                if (p.at <= currentTime && !queue.contains(p) && p != currentProcess && p.rt > 0) {
                    queue.add(p);
                }
            }
        }

        double avgTat = (double) totalTat / n;
        double avgWt = (double) totalWt / n;

        System.out.println("\nProcess\tTurnaround Time\tWaiting Time");
        for (int i = 0; i < n; i++) {
            System.out.println(i + "\t\t" + tat[i] + "\t\t\t\t" + wt[i]);
        }

        System.out.println("\nAverage Turnaround Time: " + avgTat);
        System.out.println("Average Waiting Time: " + avgWt);
    }
}
