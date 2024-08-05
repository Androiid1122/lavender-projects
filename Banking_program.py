# A simple Momo Trnasaction Program

def show_balance(balance):
    print(f'Your balance is GH{balance:.2f}cedis')

def deposit():
    amount = float(input('Enter an amount to be deposited :'))
    if amount < 0 :
        print('Amount deposited is invalid')
        return 0
    else:
        return amount
    
def withdraw():
    amount = float(input('Enter an amount to be withdrawn: '))
    if amount > balance:
        print('Insufficient Funds')
        return 0
    elif amount < 0:
        print('Amount must be greater than 0')
        return 0
    
def get_a_loan(balance):
    sim_usage = int(input('Enter how many years you have used your SIM card: '))
    if sim_usage >= 1 and balance == 0:
        print('You are eligible for a loan!')
        loan_amount = float(input('Enter an amount of loan you want: '))
        print(f'Your request was aprroved, GH{loan_amount}cedis has been added to your balance')
        return loan_amount
        print(f'Your loan of amount {loan_amount} has been approved successfully')
    elif balance != 0:
        print('Your current balance is not zero, Loan will not be approved')
    else:
        print('Sorry, you are not eligible for a loan based on SIM usage.')
        
def repay_loan(loan_amount, deadline):
    print(f'Your loan amount to repay is GH{loan_amount:.2f} cedis')
    repay_amount = float(input('Enter the amount you want to repay: '))
    if repay_amount >= loan_amount:
        print('Loan repaid successfully!')
        return 0
    else:
        interest = loan_amount * 0.05
        print(f'You have to pay GH{interest:.2f} cedis interest')
        new_amount = loan_amount + interest
        return new_amount
    

def main():
    balance = 0
    is_running = True
    loan_amount = 0
    
    while is_running:
        #Menu Options
        print('Banking Program  \n 1. Show Balance \n 2. Deposit \n 3. Withdraw \n 4. Get a Loan \n 5. Repay my Loan \n 6. Exit')
        try:
            choice = input('Enter your choice (1-6): ')
        except ValueError:
            print('Enter a valid choice')       
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()  # Add deposited amount to balance
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            loan_amount = get_a_loan(balance) 
            if loan_amount > 0:
                balance += loan_amount  # # Apply for a loan and update balance if approved
        elif choice == '5':
            if loan_amount > 0:
                loan_amount = repay_loan(loan_amount, 30)  # Repay the loan with interest if applicable
            else:
                print('You have not taken any loan.')
        elif choice == '6':
            is_running = False
        else:
            print('Enter a valid choice')
    print('Thank You,Have a nice day!!!')
main()