//Write a program that accepts an „n‟ ordered square matrix elements into a single dimension
// array and print the elements of leading diagonal (top left to bottom right).
// import java.util.Scanner;
// class week3_a{
//     public static void main(String... args){
//         Scanner sc = new Scanner(System.in);
//         int size = sc.nextInt();
//         int[][] mat = new int[size][size];
//         for(int i = 0 ; i < size ; i++)
//             for(int j = 0 ; j < size ; j++)
//                 mat[i][j] = sc.nextInt();
        
//         System.out.println("Principal diagonal elements are : ");
//         for(int i=0;i<size;i++){
//             for(int j=0;j<size;j++){
//                 if(i == j)
//                     System.out.print(mat[i][j]+" ");
//             }
//         }

//         System.out.println("\nSecondary diagonal elements are : ");
//         for(int i=0;i<size;i++){
//             for(int j=0;j<size;j++){
//                 if((i+j) == (size-1))
//                     System.out.print(mat[i][j]+" ");
//             }
//         }
//     }
// }


import java.util.Scanner;
class week3_a{
    public static void main(String... args){
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt(),index = -1;
        int[][] mat = new int[size][size];
        int[] mat_1d = new int[size*size];
        for(int i = 0 ; i < size ; i++)
            for(int j = 0 ; j < size ; j++)
                mat[i][j] = sc.nextInt();
        System.out.println("Elements in single dimenssion array  are : ");
        
        for(int i=0;i<size;i++){
            for(int j=0;j<size;j++){
                mat_1d[++index] = mat[i][j];
            }
        }
        System.out.println("Principal diagonal elements are : ");

        for(int i = 0 ; i < size*size ; i++){
            if(i%(size+1) == 0)
                System.out.print(mat_1d[i]+" ");
        }
    }
}