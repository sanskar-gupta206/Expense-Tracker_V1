# ExpenseTracker_V1
Website to calculate expenses of your trip with friends easily.
https://sanskarg.pyscriptapps.com/hisab/v1/

## Overview
This Expense Tracker is a web-based application that helps groups of people track and split shared expenses. It calculates the final balances, showing who owes money and who should receive money based on the expenses entered.

## Features
1. Add initial expenses for each person
2. Add additional expenses that can be split among multiple people
3. Calculate final balances based on all entered expenses
4. Display results in a table format

## How to Use
1. Open the HTML file in a web browser
2. Under "Initial Expenses", click "Add New Expense" to add a person and their expenses:
   - Enter the person's name
   - For the amount, you can enter multiple amounts separated by spaces (e.g., "50 30 20")
   - The application will automatically sum up these amounts for the person
3. Under "Additional Expenses", click "Add New Additional Expense" to add expenses that should be split among multiple people
4. Click "Calculate Final Balances" to see the results

## Technologies Used
- HTML
- JavaScript
- PyScript (Python in the browser)

## Limitations
1. New people cannot be added in the additional expenses section if they weren't included in the initial expenses
2. The application doesn't show the total expenditure
3. The person who paid in the additional expense is bound to split that amount with others
4. The user interface is basic and could be improved for better usability

## Potential Improvements
1. Allow adding new people in the additional expenses section
2. Display total expenditure and individual breakdowns
3. Enhance the user interface for better user experience
4. Add input validation to prevent errors from invalid inputs
5. Create a mobile-responsive design for better use on different devices
6. Allow the person who paid in additional expenses to choose whether to split their share or not
7. Provide an option to enter expenses with descriptions for each amount
