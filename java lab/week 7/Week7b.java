import java.util.*;
class Week7b
{
public static void main(String args[])
{
System.out.println("Enter the primitive datatypes:");
Scanner sc=new Scanner(System.in);
System.out.println("Byte value:");
byte b=sc.nextByte();
System.out.println("Short value:");
short s=sc.nextShort();
System.out.println("Integer value:");
int i=sc.nextInt();
System.out.println("Long value:");
long l=sc.nextLong();
System.out.println("Float value:");
float f=sc.nextFloat();
System.out.println("Double value:");
double d=sc.nextDouble();
System.out.println("Character value:");
char c=sc.next().charAt(0);
System.out.println("Boolean value:");
boolean tf=sc.nextBoolean();
System.out.println("converting primitive into objects");
Vector vobj=new Vector();
Byte bobj=b;
vobj.add(bobj);
Short sobj=s;
vobj.add(sobj);
Integer iobj=i;
vobj.add(iobj);
Long lobj=l;
vobj.add(lobj);
Float fobj=f;
vobj.add(fobj);
Double dobj=d;
vobj.add(dobj);
Character cobj=c;
vobj.add(cobj);
Boolean tfobj=tf;
vobj.add(tfobj);
Iterator itobj=vobj.iterator();
while(itobj.hasNext())
System.out.print(itobj.next()+" ");
System.out.println();
System.out.println("Converting objects into primitive");
Vector vp=new Vector();
byte bp=bobj;
vp.add(bp);
short sp=sobj;
vp.add(sp);
int ip=iobj;
vp.add(ip);
long lp=lobj;
vp.add(lp);
float fp=fobj;
vp.add(fp);
double dp=dobj;
vp.add(dp);
char cp=cobj;
vp.add(cp);
boolean tfp=tfobj;
vp.add(tfp);
Iterator itp=vp.iterator();
while(itp.hasNext())
System.out.print(itp.next()+" ");
}
}