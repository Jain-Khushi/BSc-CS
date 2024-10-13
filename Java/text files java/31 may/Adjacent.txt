class Adjacent{
    static void print(String str,int index) {
        if(index==0)
           return ;
        else{
            print(str,index-1);
            System.out.print(str.charAt(index-1));
            if(index!= str.length())
              System.out.print("#");
        }
    }  
    public static void main(String [] args) {
        int index;
        String str = "Hello";
        index=str.length();
        print(str,index);
    }  
}