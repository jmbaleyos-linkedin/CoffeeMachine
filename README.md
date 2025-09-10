# CoffeeMachine
☕ Coffee Machine Simulator (Python)

A Python-based simulation of a real-world coffee machine.
This project demonstrates modular programming, input validation, error handling, resource management, and earnings tracking in Python.

🔑 Highlights
* Object-Oriented Thinking (without full OOP yet): Structured functions for single responsibility (e.g., resources_checker, dispense_coffee, refill_resources).
* Modular Design: Code is separated into files for clarity and maintainability.
    - main.py → Main program logic and user interaction.
    - data.py → Menu configuration and available resources.
    - art.py → ASCII art logo.
* Error Handling: Ensures users can only enter valid inputs (e.g., numeric values for coins).
* Simulation of Real-Life Flow: Ordering coffee, inserting coins, checking resources, and managing change.
* Earnings Tracker: Keeps track of total revenue earned by the coffee machine.
* Extendability: Easy to add new coffee drinks or resources by editing data.py.

📂 Project Structure
<pre>
coffee-machine-simulator/
│── main.py       # Main program (logic + user interface)
│── data.py       # Menu items and initial resources
│── art.py        # ASCII art logo
│── .gitignore    # Ignore venv, __pycache__, IDE configs
│── README.md     # Project documentation
</pre>

⚙️ How It Works
1. Menu Display → User is shown available coffee options (espresso, latte, cappuccino).
2. Resource Check → Before brewing, the program checks if enough water, milk, and coffee are available.
3. Coin Insertion → User inserts coins (quarters, dimes, nickels, pennies) until the cost is met.
4. Transaction Handling → Gives change if overpaid, requests more coins if underpaid.
5. Dispense Coffee → Ingredients are deducted from available resources.
6. Earnings Tracking → Updates the coffee machine’s total bank balance.
7. Admin Commands:
    - report → Prints current resource status.
    - refill → Replenish resources manually.
    - bank → Displays current total earnings.
    - off → Shuts down the machine.

🖥️ Example Run
<pre>
_________         _____  _____                  _____          __                 
\_   ___ \  _____/ ____\/ ____\____   ____     /     \ _____  |  | __ ___________ 
/    \  \/ /  _ \   __\   __\/ __ \_/ __ \   /  \ /  \__   \ |  |/ // __ \_  __ \
\     \___(  <_> )  |   |  | \  ___/\  ___/  /    Y    \/ __ \|    <\  ___/|  | \/
 \______  /\____/|__|   |__|  \___  >\___  > \____|__  (____  /__|_ \___  >__|   
        \/                        \/     \/          \/     \/     \/    \/       

Available coffees:
- Espresso : $1.5
- Latte : $2.5
- Cappuccino : $3.0

What coffee is you like? latte
Latte would cost $2.5.
Please insert $2.5.
How many quarters? 8
You inserted exact amount.
Thank you for ordering! Grab your change and enjoy your coffee.
</pre>

🚀 Getting Started
1. Clone this repository:
    - git clone https://github.com/your-username/coffee-machine-simulator.git
2. Navigate into the project:
    - cd coffee-machine-simulator
3. Run the program:
    - python main.py

📈 Future Improvements
- Convert to Object-Oriented Programming (OOP).
- Add a GUI or web-based interface.
- Save transaction history to a file.
- Add more coffee types (e.g., mocha, americano).