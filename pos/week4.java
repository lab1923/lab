
class DiningPhilosophers
{
String state[]={"THINKING","THINKING","THINKING","THINKING","THINKING"};
//int self[]={};
void pickup(int i) {
state[i] = "HUNGRY";
test(i);
if (state[i] != "EATING")
{
//self[i].wait();
System.out.println("p-"+i+"hungry waiting");
}
}
void putdown(int i) {
if(state[i]=="EATING")
System.out.println("p-"+i+"completed eating");
state[i] = "THINKING";
test((i + 4) % 5);
test((i + 1) % 5);
}
void test(int i) {
if ((state[(i + 4) % 5] != "EATING") &&
(state[i] == "HUNGRY") &&
(state[(i + 1) % 5] != "EATING")) {
state[i] = "EATING";
System.out.println("p-"+i+"eating");
//self[i].signal();
}
}
}


class DP{
    public static void main(String[] args){
        DiningPhilosophers dp=new DiningPhilosophers();
        dp.pickup(0);
        dp.pickup(1);
        dp.pickup(2);
        dp.putdown(0);
        dp.putdown(2);
        dp.putdown(1);
    }
}
