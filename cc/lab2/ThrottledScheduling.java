import java.util.*;

class Process {
    int id;
    int arrivalTime;
    int burstTime;
    int completionTime;
    int turnaroundTime;
    int waitingTime;

    Process(int id, int arrivalTime, int burstTime) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.burstTime = burstTime;
    }
}

public class ThrottledScheduling {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of processes: ");
        int n = scanner.nextInt();

        List<Process> processes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.println("Enter details for process " + (i + 1) + ":");
            System.out.print("Arrival time: ");
            int arrivalTime = scanner.nextInt();
            System.out.print("Burst time: ");
            int burstTime = scanner.nextInt();
            processes.add(new Process(i + 1, arrivalTime, burstTime));
        }

        calculateCompletionTime(processes);
        calculateTurnaroundTime(processes);
        calculateWaitingTime(processes);

        System.out.println("\nProcess\tCompletion Time\tTurnaround Time\tWaiting Time");
        for (Process p : processes) {
            System.out
                    .println(p.id + "\t\t" + p.completionTime + "\t\t\t" + p.turnaroundTime + "\t\t\t" + p.waitingTime);
        }
        scanner.close();
    }
}

private static void calculateCompletionTime(List<Process> processes) {
    int currentTime = 0;
    for (Process p : processes) {
        currentTime = Math.max(currentTime, p.arrivalTime);
        currentTime += p.burstTime;
        p.completionTime = currentTime;
    }
}

private static void calculateTurnaroundTime(List<Process> processes) {
    for (Process p : processes) {
        p.turnaroundTime = p.completionTime - p.arrivalTime;
    }
}

private static void calculateWaitingTime(List<Process> processes) {
    for (Process p : processes) {
        p.waitingTime = p.turnaroundTime - p.burstTime;
    }

}
