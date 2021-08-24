import java.io.*;
import java.util.*;

class Week9_b {
    public static void main(String... args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("Week9b.csv"));
        String line = "";
        ArrayList<Integer> l = new ArrayList<Integer>();
        System.out.println("Before Sorting : ");
        while((line = br.readLine())!=null){
            String[] data = line.split(",");
            System.out.println("id : "+data[0]+" Name : "+data[1]+" cost : "+data[2]+" Quantity of sales : "+data[3]+" Revenue : "+(Integer.valueOf(data[3]))*(Integer.valueOf(data[2]))+"\n");
            l.add(Integer.valueOf(data[3]));
        }
        System.out.println("After Sorting :");
        Collections.sort(l);
        for(int i:l){
            br = new BufferedReader(new FileReader("Week9b.csv"));
            while((line = br.readLine())!=null){
                String[] data = line.split(",");
                if(i == Integer.valueOf(data[3])){
                    System.out.println("id : "+data[0]+" Name : "+data[1]+" cost : "+data[2]+" Quantity of sales : "+data[3]+" Revenue : "+(Integer.valueOf(data[3]))*(Integer.valueOf(data[2]))+"\n");
                }
            }
        }
    }
}