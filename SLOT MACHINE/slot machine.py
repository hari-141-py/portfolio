
WIN_LIMIT=10000
WHEEL1=["A","B","C"]
WHEEL2=["A","B","C"]
WHEEL3=["A","B","C"]

import random
import time

def deposite():
    print("Minimum deposite amount is $10 and Maximum is $",WIN_LIMIT-1)
    while True:
        amount= input("Enter the deposite amount : $")
        if amount.isdigit():
            amount=int(amount)
            if  10 <= amount < WIN_LIMIT:
                break
            else:
                print("Minimum deposite amount is $10 and Maximum is $",WIN_LIMIT-1," PLEASE TRY AGAIN !!!")
        else:
            print("NOT A NUMBER Enter a valid amount")
    print("$",amount," Has been deposited")
    return amount
dpst=deposite()

def main():
    def get_bet_amount(a):
        while True:
            bet_amount = input("Enter how much you want to bet ( minimum bet amount is $5 ): $")
            if bet_amount.isdigit():
                bet_amount = int(bet_amount)
                if bet_amount <= a and 0 < bet_amount < WIN_LIMIT and 5<=bet_amount:
                    break
                else:
                    print("NOTE : Minimum amount is $5 and Maximum is less than $", WIN_LIMIT,
                          "and should be less than or equal to the balance amount")
            else:
                print("NOT A NUMBER Enter a valid amount")
        print("$" + str(bet_amount) + " Has been Betted")
        return bet_amount

    bt_amt = get_bet_amount(dpst)

    def spin_the_wheel():
        print("RESULT IN.....", end="")
        for count_down in range(3, 0, -1):
            print(count_down, "...", end="")
            time.sleep(1)

    spin_the_wheel()

    def wallet():
        debit = dpst - bt_amt

        reel1 = random.choice(WHEEL1)
        reel2 = random.choice(WHEEL2)  # option 2 easy way
        reel3 = random.choice(WHEEL3)

        if reel1 == reel2 == reel3:
            wallet = debit + (bt_amt * 5)
            return wallet
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            wallet = debit + (bt_amt * 2)
            return wallet
        elif reel1 != reel2 or reel1 != reel3 or reel2 != reel3:
            wallet = dpst - bt_amt
            return wallet

    walt=wallet()

    def display_win(walt,bt_amt):
        # a=random.randint(0,len(WHEEL1)-1)
        # b=random.randint(0,len(WHEEL2)-1)
        # c=random.randint(0,len(WHEEL3)-1)
        #                                          #option 1 hard way
        # reel1 = WHEEL1[a]
        # reel2 = WHEEL1[b]
        # reel3 = WHEEL1[c]

        reel1 = random.choice(WHEEL1)
        reel2 = random.choice(WHEEL2)  # option 2 easy way
        reel3 = random.choice(WHEEL3)

        result_list = [reel1, reel2, reel3]
        print("\n")
        for random_pick in result_list:
            print("|", random_pick, end=" |")
            time.sleep(1)
        if reel1 == reel2 == reel3:
            print("\n/// JACKPOT /// 'YOU HAVE WON'"+"$",(bt_amt * 3))
            walt = walt + (bt_amt * 3)
            print("Balance :", walt)
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            print("\n/// DOUBLE WIN /// 'YOU HAVE WON' $",(bt_amt *2))
            walt = walt + (bt_amt * 2)
            print("Balance :", walt)
        elif reel1 != reel2 or reel1 != reel3 or reel2 != reel3:
            print("\n/// BETTER LUCK NEXT TIME [-_-] /// 'YOU HAVE LOST' $",bt_amt)
            walt = walt - bt_amt
            print("Balance :",walt)
        else:
            print("Hmm Somthings wrong...")

    display_win(walt,bt_amt)

    def play_again(walt):
        print("\n DO YOU WANNA PLAY AGAIN ?")
        print("TYPE : YES OR NO")
        while True:
            choice = input(">")
            if choice == "YES" or choice == "yes":
                if walt <= 0:
                    print("=( SORRY, YOUR WALLET IS EMPTY")

                else:
                    print("^_^ OK ")
                break
            elif choice == "NO" or choice == "no":
                print("^_^ OK, SEE YA AGAIN BYE.")
                break
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")
        main()
    # call the main function here to repeat game
    play_again(walt)

m=main()

