import java.util.*;

class Week8a {
    public static void main(String args[]) {
        System.out.println("Enter the lower limit:");
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt();
        System.out.println("Enter the upper limit:");
        int x2 = sc.nextInt();
        System.out.println("Enter the no. of random numbers to be generated:");
        int n = sc.nextInt();
        System.out.println("The random numbers are:");
        for (int i = 0; i < n; i++) {
            int r = (int) (Math.random() * (x2 - x1)) + x1;
            System.out.println(i + 1 + ")" + r);
        }
    }
}
