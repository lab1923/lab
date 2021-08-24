import java.util.*;

class Week10_a {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("Enter num1:");
            int n1 = Integer.parseInt(sc.next());
            System.out.println("Enter num2");
            int n2 = Integer.parseInt(sc.next());
            System.out.println("Quotient is:" + n1 / n2);
        } catch (NumberFormatException e) {
            System.out.println(e);
        } catch (ArithmeticException e) {
            System.out.println(e);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
