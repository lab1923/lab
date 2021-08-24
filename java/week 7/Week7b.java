import java.util.*;

class Week7b {
    public static void main(String args[]) {
        byte b = 1;
        short s = 25;
        int i = 380;
        long l = 4000;
        float f = 50.9f;
        double d = 3000.9990032;
        char c = 'B';
        boolean tf = true;

        System.out.println("converting primitive into objects");
        Vector vobj = new Vector();
        Byte bobj = b;
        Short sobj = s;
        Integer iobj = i;
        Long lobj = l;
        Float fobj = f;
        Double dobj = d;
        Character cobj = c;
        Boolean tfobj = tf;

        vobj.add(bobj);
        vobj.add(sobj);
        vobj.add(iobj);
        vobj.add(lobj);
        vobj.add(fobj);
        vobj.add(dobj);
        vobj.add(cobj);
        vobj.add(tfobj);

        Iterator itobj = vobj.iterator();
        while (itobj.hasNext())
            System.out.print(itobj.next() + " ");
    }
}
