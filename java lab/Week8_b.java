import java.util.*;

class Week8_b {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<>();
        // add
        System.out.println("Enter the size of the ArrayList:");
        int n = sc.nextInt();
        System.out.println("Enter the ArrayList:");
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            names.add(s);
        }
        System.out.println("ArrayList:" + names);
        System.out.println("Enter an index no. to add a name:");
        int k = sc.nextInt();
        System.out.println("Enter the name:");
        sc.nextLine();
        String name = sc.nextLine();
        names.add(k, name);
        System.out.println("ArrayList:" + names);
        // get
        System.out.println("Enter an index no. to display the name:");
        int i = sc.nextInt();
        System.out.println("Name at index " + i + " is:" + names.get(i));
        // remove
        System.out.println("Enter an index no. to remove a name:");
        int j = sc.nextInt();
        names.remove(j);
        System.out.println("ArrayList after removing:" + names);
        // size
        System.out.println("Size of the ArrayList is:" + names.size());
    }
}
