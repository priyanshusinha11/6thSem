import java.util.Scanner;

public class MaxMin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of machines and tasks:");
        int nM = sc.nextInt();
        int nT = sc.nextInt();

        int[][] maxMin = new int[nM][nT];
        int[][] tmp = new int[nM][nT];
        int total_time = 0;

        System.out.println("Fill Data:");
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++) {
                maxMin[i][j] = sc.nextInt();
                tmp[i][j] = maxMin[i][j];
            }
        }

        System.out.println("Original Data:");
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++)
                System.out.print(maxMin[i][j] + " ");
            System.out.println();
        }

        int[] resultTask = new int[nT];
        int[] resultMachine = new int[nT];
        int[] resultTime = new int[nT];

        int ptr = -1;

        while (ptr < nT - 1) {
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

            resultTask[++ptr] = pos;
            resultMachine[ptr] = machine[pos];
            resultTime[ptr] = tmp[machine[pos]][pos];

            if (maximum > total_time)
                total_time = maximum;

            for (int i = 0; i < nM; i++) {
                for (int j = 0; j < nT; j++) {
                    if (j == resultTask[ptr])
                        maxMin[i][j] = Integer.MAX_VALUE;
                    else if (i == resultMachine[ptr] && maxMin[i][j] != Integer.MAX_VALUE)
                        maxMin[i][j] += maximum;
                }
            }
        }

        System.out.println("\nScheduled Tasks:");
        for (int i = 0; i < nT; i++) {
            System.out.printf("\nTask %d Runs on Machine %d with Time %d units\n", resultTask[i] + 1,
                    resultMachine[i] + 1, resultTime[i]);
        }

        System.out.println("\nMax Span: " + total_time + " units");

        sc.close();
    }
}
