/*Create a class Box that uses a parameterized constructor to initialize the dimensions of a
box. The dimensions of the Box are width, height, depth. The class should have a method that
can return the volume of the box. Create an object of the Box class and test the functionality.*/
import java.util.Scanner;
class Week4_a{
    double height,width,depth;
    Week4_a(double h , double w , double d){
        System.out.println("Constructing..........In progress");
        height = h;
        width = w;
        depth = d;
    }
    double volume(){
        return height*width*depth;
    }
    public static void main(String... args){
        Scanner sc = new Scanner(System.in);
        double h = sc.nextDouble(),w = sc.nextDouble(),d = sc.nextDouble(); 
        Week4_a obj = new Week4_a(h,w,d);
        System.out.println("Volume of the box is : "+obj.volume());
    }
}