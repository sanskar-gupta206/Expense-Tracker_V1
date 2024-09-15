<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker</title>
    <link rel="stylesheet" href="index.css">
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
    <h1 class="heading">Expense Tracker</h1>

    <h2>Initial Expenses</h2>
    <div id="expenses">
        <!-- Dynamic fields for adding expenses will appear here -->
    </div>
    <button id="addExpenseBtn">Add New Expense</button>

    <h2>Additional Expenses</h2>
    <div id="additionalExpenses">
        <!-- Dynamic fields for splitting additional expenses will appear here -->
    </div>
    <button id="addAdditionalExpenseBtn">Add New Additional Expense</button>

    <br><br>
    <button id="calculateBtn">Calculate Final Balances</button>

    <h2>Final Balances:</h2>
    <div id="resultTable"></div>

    <script>
        function createExpenseField() {
            const expenseContainer = document.getElementById('expenses');

            const div = document.createElement('div');
            div.classList.add('expense-entry');

            const labelName = document.createElement('label');
            labelName.innerText = "Enter Name:";
            const inputName = document.createElement('input');
            inputName.type = 'text';
            inputName.classList.add('name');

            const labelAmount = document.createElement('label');
            labelAmount.innerText = "Enter Money Spent:";
            const inputAmount = document.createElement('input');
            inputAmount.type = 'text';
            inputAmount.classList.add('amount');

            const deleteButton = document.createElement('button');
            deleteButton.innerText = "Delete";
            deleteButton.onclick = function () {
                div.remove();
            };

            div.appendChild(labelName);
            div.appendChild(inputName);
            div.appendChild(labelAmount);
            div.appendChild(inputAmount);
            div.appendChild(deleteButton);
            div.appendChild(document.createElement('br'));

            expenseContainer.appendChild(div);
        }

        function createAdditionalExpenseField() {
            const additionalExpenseContainer = document.getElementById('additionalExpenses');

            const div = document.createElement('div');
            div.classList.add('additional-expense-entry');

            const labelAnyother = document.createElement('label');
            labelAnyother.innerText = "Any Other:";
            const inputAnyother = document.createElement('input');
            inputAnyother.type = 'text';
            inputAnyother.classList.add('anyother');

            const labelAmount = document.createElement('label');
            labelAmount.innerText = "Money Spent:";
            const inputAmount = document.createElement('input');
            inputAmount.type = 'text';
            inputAmount.classList.add('extraAmount');

            const labelAmong = document.createElement('label');
            labelAmong.innerText = "Split Among (space-separated):";
            const inputAmong = document.createElement('input');
            inputAmong.type = 'text';
            inputAmong.classList.add('among');

            const deleteButton = document.createElement('button');
            deleteButton.innerText = "Delete";
            deleteButton.onclick = function () {
                div.remove();
            };

            div.appendChild(labelAnyother);
            div.appendChild(inputAnyother);
            div.appendChild(labelAmount);
            div.appendChild(inputAmount);
            div.appendChild(labelAmong);
            div.appendChild(inputAmong);
            div.appendChild(deleteButton);
            div.appendChild(document.createElement('br'));

            additionalExpenseContainer.appendChild(div);
        }

        // Bind button events for adding new fields
        document.getElementById('addExpenseBtn').addEventListener('click', createExpenseField);
        document.getElementById('addAdditionalExpenseBtn').addEventListener('click', createAdditionalExpenseField);
    </script>

    <script type="py">
        book = {}

        def add_expenses():
            # Get all the dynamically created expense entries
            expense_entries = js.document.querySelectorAll('.expense-entry')
            for entry in expense_entries:
                name = entry.querySelector('.name').value
                amount = entry.querySelector('.amount').value
                if name != '0' and amount:
                    try:
                        j = amount.split(' ')
                        total = sum([int(i) for i in j])
                        book[name] = total
                    except ValueError:
                        pass  # Ignore invalid input

        def add_additional_expenses():
            additional_entries = js.document.querySelectorAll('.additional-expense-entry')
            for entry in additional_entries:
                anyother = entry.querySelector('.anyother').value
                amount = entry.querySelector('.extraAmount').value
                among = entry.querySelector('.among').value.split(' ')
                if anyother != '0' and amount:
                    try:
                        amoun = int(amount)
                        noof = len(among)
                        contri = amoun / (noof + 1)
                        book[anyother] = book.get(anyother, 0) + amoun - contri
                        for person in among:
                            book[person] = book.get(person, 0) - contri
                    except ValueError:
                        pass  # Ignore invalid input

        def calculate(event):
            # Clear book and re-add from the form
            global book
            book = {}

            add_expenses()
            add_additional_expenses()

            if book:
                gsum = sum(book.values())
                count = len(book)
                each = gsum / count

                for name in book:
                    book[name] -= each

                # Clear existing result table
                result_div = js.document.getElementById('resultTable')
                result_div.innerHTML = ''

                # Create the table element
                table = js.document.createElement('table')
                table.setAttribute('border', '1')
                
                # Create table header
                header = js.document.createElement('tr')
                header_name = js.document.createElement('th')
                header_name.innerHTML = 'Name'
                header_balance = js.document.createElement('th')
                header_balance.innerHTML = 'Balance'
                header.appendChild(header_name)
                header.appendChild(header_balance)
                table.appendChild(header)

                # Add rows for each person and their balance
                for person, balance in book.items():
                    row = js.document.createElement('tr')

                    cell_name = js.document.createElement('td')
                    cell_name.innerHTML = person
                    row.appendChild(cell_name)

                    cell_balance = js.document.createElement('td')
                    cell_balance.innerHTML = str(balance)
                    row.appendChild(cell_balance)

                    table.appendChild(row)

                result_div.appendChild(table)
            else:
                js.document.getElementById('resultTable').innerHTML = "No valid entries found."

        # Bind the calculate button to the Python calculate function
        Element('calculateBtn').element.onclick = calculate
    </script>

    <style>
        .expense-entry, .additional-expense-entry {
            margin-bottom: 10px;
        }

        table {
            width: 50%;
            margin-top: 20px;
            border-collapse: collapse;
        }

        th, td {
            padding: 8px;
            text-align: left;
        }
    </style>
</body>
</html>
