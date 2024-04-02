import java.util.*;

class Process {
    int id;
    int priority;
    int burstTime;
    int completionTime;

    Process(int id, int priority, int burstTime) {
        this.id = id;
        this.priority = priority;
        this.burstTime = burstTime;
        this.completionTime = 0;
    }
}

public class PriorityScheduling {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of processes: ");
        int n = scanner.nextInt();

        List<Process> processes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.println("Enter details for process " + (i + 1) + ":");
            System.out.print("Priority: ");
            int priority = scanner.nextInt();
            System.out.print("Burst time: ");
            int burstTime = scanner.nextInt();
            processes.add(new Process(i + 1, priority, burstTime));
        }

        priorityScheduling(processes);

        System.out.println("\nProcess\tPriority\tBurst Time\tCompletion Time");
        for (Process p : processes) {
            System.out.println(p.id + "\t\t" + p.priority + "\t\t\t" + p.burstTime + "\t\t\t" + p.completionTime);
        }
    }

    private static void priorityScheduling(List<Process> processes) {
        PriorityQueue<Process> readyQueue = new PriorityQueue<>(Comparator.comparingInt(p -> p.priority));
        int currentTime = 0;

        while (!processes.isEmpty()) {
            // Add processes to the ready queue whose arrival time is less than or equal to
            // the current time
            for (Process p : processes) {
                if (p.burstTime > 0) {
                    readyQueue.add(p);
                }
            }

            if (!readyQueue.isEmpty()) {
                Process currentProcess = readyQueue.poll();
                System.out.println("Executing process " + currentProcess.id + " at time " + currentTime);
                int quantum = Math.min(2, currentProcess.burstTime);
                currentProcess.burstTime -= quantum;
                currentTime += quantum;
                if (currentProcess.burstTime == 0) {
                    currentProcess.completionTime = currentTime;
                    processes.remove(currentProcess);
                    System.out.println("Process " + currentProcess.id + " completed at time " + currentTime);
                } else {
                    readyQueue.add(currentProcess); // Re-add the process to the ready queue if it hasn't finished
                }
            } else {
                currentTime++;
            }
        }
    }
}
