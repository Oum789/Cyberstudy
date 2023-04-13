check_money = cart.initiate_payment(1234)

    if check_money == 1:
        print("Payment Successful")
        course_bought.add_course_to_list(cart.get_buying_list(),user1.get_name())
        receipt = Receipt("receipt_pic.png","order_date",1)
        user1.add_receipt_to_list(receipt)
    else:
        print("Payment Failed, Please try again")