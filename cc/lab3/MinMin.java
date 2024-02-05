import java.util.Scanner;

public class MinMin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of machines and tasks:");
        int nM = sc.nextInt();
        int nT = sc.nextInt();

        int[][] minMin = new int[nM][nT];
        int[][] temp = new int[nM][nT];
        int makespan = 0;

        System.out.println("Fill data:");
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++) {
                minMin[i][j] = sc.nextInt();
                temp[i][j] = minMin[i][j];
            }
        }

        System.out.println("Original Data:");
        for (int i = 0; i < nM; i++) {
            for (int j = 0; j < nT; j++)
                System.out.print(minMin[i][j] + " ");
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

            if (ptr + 1 < nT) {
                resultTask[++ptr] = pos;
                resultMachine[ptr] = machine[pos];
                resultTime[ptr] = temp[machine[pos]][pos];

                if (minimum > makespan) {
                    makespan = minimum;
                }

                for (int i = 0; i < nM; i++) {
                    for (int j = 0; j < nT; j++) {
                        if (j == resultTask[ptr])
                            minMin[i][j] = Integer.MAX_VALUE;
                        else if (i == resultMachine[ptr] && minMin[i][j] != Integer.MAX_VALUE)
                            minMin[i][j] += minimum;
                    }
                }
            }
        }

        System.out.println("Scheduled Tasks:");
        for (int i = 0; i <= ptr; i++) {
            System.out.printf("Task %d Runs on Machine %d with Time %d units\n", resultTask[i] + 1,
                    resultMachine[i] + 1, resultTime[i]);
        }

        System.out.println("Max Span: " + makespan + " units");

        sc.close();
    }
}
