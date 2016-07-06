import java.io.*;
import java.util.*;

public class Solution {
    
    long factorial(int n){
    long fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }
    boolean checkprime(int n) {
            if (n == 1)
                return false;
            else {
                for (int i = 2; i <= n / 2; i++) {
                    if (n % i == 0) {
                        return false;
                    }
                }
                return true;
            }
        }
    
    public static void main(String[] args) {        
        Solution s = new Solution();
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        int array[];
        long output[];         
        array = new int[T];
        output = new long[T];
        for(int i=0; i<T; i++){
            array[i]=scan.nextInt();            
        }
        for(int i=0; i<T; i++){
            int q=array[i]/4;
            int r=array[i]%4;
            long  M=0;            
            for(int j=q; j>-1; j--){                 
              M = M + s.factorial(j + r)/(s.factorial(j)*s.factorial(r));                 
              r=r+4; 
            }
            output[i]=M;
        }
                
        for(int k=0; k<T; k++){
            int count=0;
            for(int p=1; p<=output[k]; p++){
                boolean isprime = s.checkprime(p);
                if(isprime==true)
                    count++;
            }
            System.out.println(count);
        }        
    }
}
