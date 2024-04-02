import java.util.*;

class Task {
    int id;
    int startTime;
    int finishTime;
    List<Task> dependencies;

    Task(int id) {
        this.id = id;
        this.startTime = 0;
        this.finishTime = 0;
        this.dependencies = new ArrayList<>();
    }
}

public class WorkflowTaskScheduling {
    public static void main(String[] args) {
        // Construct the workflow graph
        Task[] tasks = constructWorkflow();

        // Perform earliest start time (EST) scheduling
        performESTScheduling(tasks);

        // Print scheduling results
        printSchedulingResults(tasks);
    }

    // Construct a simple workflow graph
    private static Task[] constructWorkflow() {
        Task[] tasks = new Task[5]; // Assuming 5 tasks in the workflow

        for (int i = 0; i < tasks.length; i++) {
            tasks[i] = new Task(i + 1);
        }

        // Define task dependencies
        tasks[1].dependencies.add(tasks[0]);
        tasks[2].dependencies.add(tasks[0]);
        tasks[3].dependencies.add(tasks[1]);
        tasks[3].dependencies.add(tasks[2]);
        tasks[4].dependencies.add(tasks[3]);

        return tasks;
    }

    // Perform earliest start time (EST) scheduling
    private static void performESTScheduling(Task[] tasks) {
        for (Task task : tasks) {
            int earliestStartTime = 0;
            for (Task dependency : task.dependencies) {
                earliestStartTime = Math.max(earliestStartTime, dependency.finishTime);
            }
            task.startTime = earliestStartTime;
            task.finishTime = earliestStartTime + 1; // Assuming each task takes 1 unit of time
        }
    }

    // Print scheduling results
    private static void printSchedulingResults(Task[] tasks) {
        System.out.println("Task\tStart Time\tFinish Time");
        for (Task task : tasks) {
            System.out.println(task.id + "\t\t" + task.startTime + "\t\t\t" + task.finishTime);
        }
    }
}
