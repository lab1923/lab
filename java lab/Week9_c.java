import java.io.*;
import java.util.Arrays;

public class Week9c {
    public static void main(String args[]) throws IOException {
        FileInputStream fis = new FileInputStream("D://sai_kaushik//input.txt");
        FileWriter fw = new FileWriter("D://sai_kaushik//output.txt");
        InputStreamReader isr = new InputStreamReader(fis);
        BufferedReader br = new BufferedReader(isr);
        String line;
        String[] wordlist = {};
        while ((line = br.readLine()) != null) {
            wordlist = line.split(" ");
        }
        Arrays.sort(wordlist);
        for (String s : wordlist) {
            fw.write(s);
            fw.write(" ");
        }
        fw.close();
        br.close();
        System.out.println("Check the output file");
    }
}