import java.util.Scanner;

public class MinMin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of machines and tasks:");
        int nM = sc.nextInt();
        int nT = sc.nextInt();

        int[][] minMin = new int[nM][nT];
        int[][] temp = new int[nM][nT];
        int maxspan = 0;

        System.out.println("Entered the time units for each machines for respective tasks");
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++) {
                minMin[i][j] = sc.nextInt();
                temp[i][j] = minMin[i][j];
            }
        }

        
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++)
                System.out.print(minMin[i][j] + " ");
            System.out.println();
        }

        int[] resTask = new int[nT];
        int[] resMachine = new int[nT];
        int[] resTime = new int[nT];
        int ind = -1;

        while (ind < nT - 1) {
            int[] time = new int[nT];
            int[] machine = new int[nT];

            for (int j = 0; j < nT; j++) {
                int minimum = Integer.MAX_VALUE;
                int pos = -1;
                for (int i = 0; i < nM; i++) {
                    if (minMin[i][j] < minimum) {
                        minimum = minMin[i][j];
                        pos = i;
                    }
                }
                time[j] = minimum;
                machine[j] = pos;
            }

            int minimum = Integer.MAX_VALUE;
            int pos = -1;
            for (int j = 0; j < nT; j++) {
                if (time[j] < minimum) {
                    minimum = time[j];
                    pos = j;
                }
            }

            if (ind + 1 < nT) {
                resTask[++ind] = pos;
                resMachine[ind] = machine[pos];
                resTime[ind] = temp[machine[pos]][pos];

                if (minimum > maxspan) {
                    maxspan = minimum;
                }

                for (int i = 0; i < nM; i++) {
                    for (int j = 0; j < nT; j++) {
                        if (j == resTask[ind])
                            minMin[i][j] = Integer.MAX_VALUE;
                        else if (i == resMachine[ind] && minMin[i][j] != Integer.MAX_VALUE)
                            minMin[i][j] += minimum;
                    }
                }
            }
        }

        System.out.println("Scheduled Tasks:");
        for (int i = 0; i <= ind; i++) {
            System.out.printf("Task %d Runs on Machine %d with Time %d units\n", resTask[i] + 1,
                    resMachine[i] + 1, resTime[i]);
        }

        System.out.println("Max Span: " + maxspan + " units");

        sc.close();
    }
}
