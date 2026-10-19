public class hello {
    public static void main(String[] args) {
      int n = 4;
      int m =5;
      int space;
      //upper part 
      for(int i =1;i<=n;i++){
        for(int j=1; j<=i;j++){
          System.out.print("*");
        
        }
        // print space 
        space = 2*(n-i);
        for(int j=1;j<=space;j++){
          System.out.print(" ");
        }
        for(int j=1; j<=i;j++){
          System.out.print("*");
        
        } 
        System.out.println();


      }
      //lower part 
       for(int i =n;i>=1;i--){
        for(int j=1; j<=i;j++){
          System.out.print("*");
        
        }
        //space
        space = 2*(n-i);
        for(int j=1;j<=space;j++){
          System.out.print(" ");
        }
        for(int j=1; j<=i;j++){
          System.out.print("*");
        
        } 
        System.out.println();


      }

      //new questioin
      for(int i=1;i<=m;i++){
        for(int j=1;j<=m-i;j++){
          System.out.print(" ");

        }
        for(int j=1;j<=5;j++){
          System.out.print("*");
        }
         System.out.println();
      }
      System.out.println();
     


      //new question
      int p=5;
      int num=1;
      for(int i=1;i<=p;i++){
        //space
        for( int j=1;j<=p-i;j++){
          System.out.print(" ");  

        }
        for(int j=1;j<=i;j++){
          System.out.print(i);
          num++;


        }
        System.out.println();
      }


    }
}