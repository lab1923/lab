import java.io.*;
import java.util.*;
public class Week9c 
{
    public static void main(String args[]) throws IOException
    {
        ArrayList<String> l1=new ArrayList<String>();
        ArrayList<String> l2=new ArrayList<String>();
        File f1=new File("stopwords.txt");
        File f2=new File("technical.txt");
        Scanner sc1=new Scanner(f1);
        Scanner sc2=new Scanner(f2);
        while(sc1.hasNext())
        {
            String a=sc1.next();
            l1.add(a.toLowerCase());
        }
        while(sc2.hasNext())
        {
            String a=sc2.next();
            if(l1.contains(a)||l2.contains(a))
            {
                continue;
            }
            else
            l2.add(a.toLowerCase());
        }
        Collections.sort(l2);
        System.out.println(l2);
    }
}
