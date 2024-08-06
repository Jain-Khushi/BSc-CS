import java.util.Scanner;

class BankAccount {

private String name;
private String address;
private double balance =0.0;
private String accType;
private String uniqueAccNo;

//static members 
private static int accNo=100;
private static int  noOfTransaction = 0;


public BankAccount()
 {

                      Scanner sc = new Scanner(System.in);

                      System.out.print("Enter the name : " );
                      name = sc.nextLine();
                      System.out.println();

                      System.out.print("Enter the Account Type such as Saving, Current, joint : " );
                      accType = sc.nextLine();
                      System.out.println();

                      System.out.print("Enter the Address : " );
                      address = sc.nextLine();
                      System.out.println();


                      uniqueAccNo= "BA"+accNo;
                      System.out.println();
                      accNo++;

                      
 }


void depositMoney(double amount)
{

                      balance+=amount;
                      noOfTransaction++;
                      getInfo();

}


void withdrawMoney(double withdrawAmount)
{

                      if(balance ==0.0)
                  {
                                            System.out.print("your Account balance is INR 0.0 ");
                   }
               
                    else if(withdrawAmount>balance )
                  {
                                            balance = 0.0;
                   }
                  
                  else
                  {
                                              balance-=withdrawAmount;
                                              noOfTransaction++;
                                              getInfo();
                   }
}

void getInfo()
{

                       System.out.print("Name : " + name);
                       System.out.println();

                       System.out.print("Address : " + address);
                       System.out.println();

                       System.out.print("Account Type: " + accType);
                       System.out.println();

                       System.out.print("Account No: "+ uniqueAccNo );
                       System.out.println();

                       System.out.print("Current Balance: "+ balance );
                       System.out.println();
}

void ToChangeAdress(String newAddress)
{
                       address = newAddress;
                       getInfo();
}


public static void Transaction()
{

System.out.println("total number of transaction are: "+noOfTransaction);

}

}


class BankAccountDemo
{

public static void main(String args[]){

int noOfDepositer;

Scanner sc= new Scanner(System.in);


System.out.print("Enter the no of depositer: "); //taking number of depositer from user

noOfDepositer = sc.nextInt();
System.out.println();

BankAccount[] b= new BankAccount[noOfDepositer]; //Declaring Array of type BankAccount

//constructing Object of type BankAccount

for(int i= 0;i<noOfDepositer; i++){

System.out.println("enter details for "+( i+1)+" Account");
b[i]=new BankAccount();
System.out.println();
}

//depositing money
for(int i= 0;i<noOfDepositer; i++){
double amount ;

System.out.print("enter amount you want to deposit in Account"+( i+1)+" : ");
amount = sc.nextDouble();

b[i].depositMoney(amount);
System.out.println();
}

System.out.println();

//withdrawing money
for(int i= 0;i<noOfDepositer; i++){
double amount ;

System.out.print("enter amount you want to withdraw from Account"+( i+1)+" : ");
amount = sc.nextDouble();

b[i].withdrawMoney(amount);
System.out.println();
}

BankAccount.Transaction(); //To Display total no of transaction
}
}






