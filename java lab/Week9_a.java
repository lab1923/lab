import java.io.*;

class Week9a {
    public static void main(String args[]) throws IOException {
        File fr = new File("D://sai_kaushik//input.txt");
        File fw = new File("D://sai_kaushik// 9aoutput.txt");
        FileInputStream fis = new FileInputStream(fr);
        FileOutputStream fos = new FileOutputStream(fw);
        int alphabets = 0;
        int numeric = 0;
        int special = 0;
        int i = 0;
        StringBuffer alp = new StringBuffer();
        StringBuffer num = new StringBuffer();
        StringBuffer spec = new StringBuffer();
        while ((i = fis.read()) != -1) {
            if (i >= '0' && i <= '9') {
                numeric++;
                num.append((char) i);
            } else if (i >= 'A' && i <= 'z') {
                alphabets++;
                alp.append((char) i);
            } else {
                special++;
                spec.append((char) i);
            }
        }
        num.append((char) '-');
        num.append(numeric);
        alp.append((char) '-');
        alp.append(alphabets);
        spec.append((char) '-');
        spec.append(special);
        for (int a = 0; a < num.length(); a++) {
            fos.write(num.charAt(a));
        }
        fos.write((char) '\n');
        for (int a = 0; a < alp.length(); a++) {
            fos.write(alp.charAt(a));
        }
        fos.write((char) '\n');
        for (int a = 0; a < spec.length(); a++) {
            fos.write(spec.charAt(a));
        }
        fos.write((char) '\n');
        System.out.println(numeric + " numeric values found");
        System.out.println(alphabets + " alphabets found");
        System.out.println(special + " special characters found");
        fis.close();
        fos.close();
        System.out.println("Check the output file");
    }
}