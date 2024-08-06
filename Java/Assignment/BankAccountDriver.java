import java.util.Scanner;
class BankAccount {
    
    private String name;
    private String address;
    private String type;
    private double balance = 0.0;
    private static int transactions=0;
    private String accNumber;

    private static int acc = 1000;

    public BankAccount(){
        
        Scanner sc = new Scanner(System.in);
            System.out.println("Enter name of depositor : ");
            String name = sc.nextLine();
           
            System.out.println("Enter address of depositor : ");
            String address = sc.nextLine();
            
            System.out.println("Enter the type of account : ");
            String type = sc.nextLine();
            
            System.out.println("Enter the balance in account : ");
            double balance = sc.nextDouble();
           
            accNumber = "BA" + acc;
            acc++;
        }

    void deposit(double depositAmount){
        balance = balance + depositAmount;
        transactions ++ ;
        display();
    }
    void withdraw(double withdrawAmount){
        if(balance==0.0)
           System.out.println("Insufficient balance !!");
        else if(withdrawAmount > balance)
           System.out.println("Bank overdraft !!");
        else if(withdrawAmount < balance)
           balance = balance - withdrawAmount;
           transactions ++ ;
           display();
    }
    void changeAddress(String address1){
        address = address1;
        display();
    }
    static void transaction(){
        System.out.println("Total number of transactions is " + transactions);
    }

void display(){
    System.out.println("Name : " + name );
    System.out.println("Address : " + address);
    System.out.println("Type : " + type);
    System.out.println("Balance : " + balance);
    System.out.println("Account number : " + accNumber);
}
}

class BankAccountDriver{
        public static void main (String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of depositors : ");
        int n = sc.nextInt();
        BankAccount [] arr = new BankAccount[n]; //Declaring array of type Account
        for(int i=0 ; i<n ; i++){
            System.out.println("Enter details for depositors " + i+1);
            arr[i] = new BankAccount();
        }

        for(int i=0 ; i<n ; i++){
            System.out.println("Enter the amount you want to deposit in account " + (i+1) );
            double depositAmount = sc.nextDouble();
            arr[i].deposit(depositAmount);
        }

        for(int i=0 ; i<n ; i++){
            System.out.println("Enter the amount you want to withdraw from account " + (i+1) );
            double withdrawAmount = sc.nextDouble();
            arr[i].withdraw(withdrawAmount);
        }

        for(int i=0 ; i<n ; i++){
            System.out.println("Enter the address you want in account " + (i+1) );
            String address = sc.nextLine();
            arr[i].changeAddress(address);
        }

        BankAccount.transaction();

        sc.close();
    }
}
