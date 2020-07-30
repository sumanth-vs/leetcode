<<<<<<< HEAD
import java.util.ArrayList;

public class P1480 {
    public static void main(String[] args) {
        
        int array[] = {1, 2, 3, 4, 5};
        ArrayList<Integer> rl = runningSum(array);
        // int rlf[] = rl.toArray();
    }

    public static ArrayList<Integer> runningSum(int[] nums) {

        ArrayList<Integer> rl = new ArrayList<Integer>();
        rl.add(nums[0]);

        for(int i = 1; i < nums.length; i++){
            rl.add(rl.get(i-1) + nums[i]);
        }

        return rl;
    }
=======
import java.util.ArrayList;

public class P1480 {
    public static void main(String[] args) {
        
        int array[] = {1, 2, 3, 4, 5};
        ArrayList<Integer> rl = runningSum(array);
        // int rlf[] = rl.toArray();
    }

    public static ArrayList<Integer> runningSum(int[] nums) {

        ArrayList<Integer> rl = new ArrayList<Integer>();
        rl.add(nums[0]);

        for(int i = 1; i < nums.length; i++){
            rl.add(rl.get(i-1) + nums[i]);
        }

        return rl;
    }
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
}