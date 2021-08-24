import java.util.*;

class Week8_c {
    public static void main(String args[]) {
        HashMap<Integer, Employee> hashmap = new HashMap<Integer, Employee>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. of employees");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.println("Enter employee " + (i + 1) + " details:");
            System.out.println("Enter employee id:");
            int id = sc.nextInt();
            sc.nextLine();
            System.out.println("Enter employee name:");
            String name = sc.nextLine();
            System.out.println("Enter employee age:");
            int age = sc.nextInt();
            Employee e = new Employee();
            e.setter(id, name, age);
            hashmap.put(e.getId(), e);
        }
        System.out.println("Enter a key id to search:");
        int s = sc.nextInt();
        if (hashmap.containsKey(s))
            System.out.println("Employee id is:" + s + "\nEmployee name is:" + hashmap.get(s).getName()
                    + "\nEmployee age is:" + hashmap.get(s).getAge());
    }
}

class Employee {
    private int id;
    private String name;
    private int age;

    void setter(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    int getId() {
        return id;
    }

    String getName() {
        return name;
    }

    int getAge() {
        return age;
    }
}
