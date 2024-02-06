import java.util.Scanner;

public class MaxMin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of machines and tasks:");
        int nM = sc.nextInt();
        int nT = sc.nextInt();

        int[][] maxMin = new int[nM][nT];
        int[][] tmp = new int[nM][nT];
        int maxspan = 0;

        System.out.println("Entered the time units for each machines for respective tasks");
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++) {
                maxMin[i][j] = sc.nextInt();
                tmp[i][j] = maxMin[i][j];
            }
        }

      
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++)
                System.out.print(maxMin[i][j] + " ");
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
                    if (maxMin[i][j] < minimum) {
                        minimum = maxMin[i][j];
                        pos = i;
                    }
                }
                time[j] = minimum;
                machine[j] = pos;
            }

            int maximum = Integer.MIN_VALUE;
            int pos = -1;

            for (int j = 0; j < nT; j++) {
                if (time[j] > maximum && time[j] != Integer.MAX_VALUE) {
                    maximum = time[j];
                    pos = j;
                }
            }

            resTask[++ind] = pos;
            resMachine[ind] = machine[pos];
            resTime[ind] = tmp[machine[pos]][pos];

            if (maximum > maxspan)
                maxspan = maximum;

            for (int i = 0; i < nM; i++) {
                for (int j = 0; j < nT; j++) {
                    if (j == resTask[ind])
                        maxMin[i][j] = Integer.MAX_VALUE;
                    else if (i == resMachine[ind] && maxMin[i][j] != Integer.MAX_VALUE)
                        maxMin[i][j] += maximum;
                }
            }
        }

        System.out.println("\nScheduled Tasks:");
        for (int i = 0; i < nT; i++) {
            System.out.printf("\nTask %d Runs on Machine %d with Time %d units\n", resTask[i] + 1,
                    resMachine[i] + 1, resTime[i]);
        }

        System.out.println("\nMax Span: " + maxspan + " units");

        sc.close();
    }
}
