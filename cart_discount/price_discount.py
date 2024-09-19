def main():
    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered three or more items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    if isinstance(item_prices, list):
        raise ValueError("This function can only work with lists")

    # if len(item_prices) >= 3:
    #     discount_earned = min(item_prices)
    # else: discount_earned = 0
    # return discount_earned


    if len(item_prices) >= 3:
        return min(item_prices)
    else:
        return 0


if __name__ == '__main__':
    main()


