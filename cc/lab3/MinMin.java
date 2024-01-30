import java.util.*;

class Process {
    int id;
    int bt;

    Process(int id, int bt) {
        this.id = id;
        this.bt = bt;
    }
}

public class MinMin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Process> processes = new ArrayList<>();
        System.out.println("Enter the number of processes:");
        int n = sc.nextInt();
        System.out.println("Enter the burst time for each process:");
        for (int i = 0; i < n; i++) {
            int bt = sc.nextInt();
            processes.add(new Process(i, bt));
        }

        minMin(processes);

        sc.close();
    }

    public static void minMin(List<Process> processes) {
        processes.sort(Comparator.comparingInt(p -> p.bt)); 

        int n = processes.size();
        int[] wt = new int[n];
        int[] tat = new int[n]; 

        int currentTime = 0;

        for (int i = 0; i < n; i++) {
            Process currentProcess = processes.get(i);
            wt[currentProcess.id] = currentTime; 
            currentTime += currentProcess.bt; 
            tat[currentProcess.id] = currentTime; 
        }

        double totalWt = 0;
        double totalTat = 0;

        for (int i = 0; i < n; i++) {
            totalWt += wt[i];
            totalTat += tat[i];
        }

        double avgTat = totalTat / n;
        double avgWt = totalWt / n;

        System.out.println("\nProcess\tTurnaround Time\tWaiting Time");
        for (int i = 0; i < n; i++) {
            System.out.println(i + "\t\t" + tat[i] + "\t\t\t\t" + wt[i]);
        }

        System.out.println("\nAverage Turnaround Time: " + avgTat);
        System.out.println("Average Waiting Time: " + avgWt);
    }
}
