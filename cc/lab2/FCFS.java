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

public class FCFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Process> prc = new ArrayList<>();
        System.out.println("Enter the number of processes:");
        ;
        int n = sc.nextInt();
        System.out.println("Enter the arrival and burst time:");
        for (int i = 0; i < n; i++) {
            int at = sc.nextInt();
            int bt = sc.nextInt();
            prc.add(new Process(i, at, bt));
        }

        prc.sort(Comparator.comparingInt(p -> p.at));

        int ct = 0;

        for (Process process : prc) {

            if (process.at > ct) {
                ct = process.at;
            }

            ct += process.bt;

            int tat = ct - process.at;
            int wt = tat - process.bt;

            System.out.println("Process " + process.id + " | Turnaround Time: " + tat + " | Waiting Time: " + wt);
        }

        sc.close();
    }
}
