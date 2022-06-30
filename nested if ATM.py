atm_card=input("insert your atm card")
if atm_card=="Right Side" or atm_card=="right side":
    language=input("enter any language")
    if language=="English" or language=="Hindi":
        pin=int(input("enter 4 digit number"))
        if pin>999 and pin<10000:
            transaction_type=input("enter transaction type")
            if transaction_type=="Withdrawal" or transaction_type=="withdrawal":
                account_type=input("enter any account type")
                amount=int(input("enter amount"))
                key_name=input("enter ok")
                if amount>=500 or amount<=2000 and amount%500==0:
                    a=amount//2000
                    b=amount%2000
                    c=b//500
                    d=b%500
                    print("note of 2000=",a,"note 0f 500=",c)
                    money_receipt=input("enter money received")
                    if money_receipt=="Y" or money_receipt=="N":
                        print("money receipt")
                    else:
                        print("thanks for money transaction")
                else:
                    print("limited amount")
            elif transaction_type=="Balance Enquiry" or transaction_type=="balance enquiry":
                account_type=input("enter account type")
                key_name=input("enter ok")
                print("total amount")
                if key_name=="Ok" or key_name=="ok":
                    print("thanks for enquiry")
                else:
                    print("invalid")
            elif transaction_type=="Deposit" or transaction_type=="deposit":
                account_no=int(input("enter account number"))
                if account_no>=1000000000 and account_no<=9999999999:
                    bill_amt=int(input("enter bill amount"))
                    if bill_amt>=1000000000 and bill_amt<=9999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter ok")
                        if key_name=="Ok" or key_name=="ok":
                            print("successful")
                        else:
                            print("unsuccessful")
            elif transaction_type=="Bill Pay" or transaction_type=="bill pay":
                account_no=int(input("enter account number"))
                if account_no>=1000000000 and account<=9999999999:
                    bill_id=int(input("enter bill id"))
                    if bill_id>=1000000000 and bill_id<=9999999999:
                        amount=int(input("enter amount"))
                        key_name=input("enter ok")
                        if key_name=="Ok" or key_name=="ok":
                            print("succesful")
                        else:
                            print("unsuccessful")
            else:
                print("not succesful")
        else:
            print("invalid pin")
    else:
        print("no bengali language")
else:
    print("rejected")                                      