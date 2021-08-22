package report;
import week7a1.*;
import week7a2.*;
import java.util.Scanner;
public class Week7a
{
public static void main(String args[])
{
Student s=new Student();
Sports sp=new Sports();
Scanner sc=new Scanner(System.in);
System.out.println("Enter student name");
s.name=sc.nextLine();
System.out.println("Enter the roll number");
s.rollno=sc.nextInt();
System.out.println("Student name is:"+s.name+"\nStudent rollno is:"+s.rollno);
sp.display();
}
}