from sms_reader import read_sms
from expense_classifier import classify_expense
from report import generate_report
import re

sms_list = read_sms()

expenses = []

for sms in sms_list:

    amount = int(re.findall(r'\d+', sms)[0])

    category = classify_expense(sms)

    expenses.append((category, amount))

generate_report(expenses)