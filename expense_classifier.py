def classify_expense(sms):

    sms = sms.lower()

    if "zomato" in sms or "food" in sms:
        return "Food"

    elif "uber" in sms:
        return "Travel"

    elif "amazon" in sms:
        return "Shopping"

    else:
        return "Other"