import java.util.*;

class Week10b {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the age");
        int a = sc.nextInt();
        String s1 = "Invalid age to vote";
        String s2 = "Correct age to vote";
        try {
            if (a < 18) {
                throw new MyException(s1);
            } else {
                System.out.println(s2);
            }
        } catch (MyException e) {
            System.out.println(e);
        }
    }
}

class MyException extends Exception {
    MyException(String s) {
        super(s);
    }
}
