package week7a2;
interface sport
{
void display();
}
public class Sports implements sport
{
public void display()
{
System.out.println("Announcement of sports league schedule");
System.out.println("24-06-2021-Throwball");
System.out.println("14-06-2021-Cricket");
System.out.println("02-05-2021-Volleyball");
}
}