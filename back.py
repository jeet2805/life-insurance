import os
# classsssssssssssssssssssssssssssssssssssssssssssssssssssssssssss


class Employee:
    def __init__(self, username, password, empId):
        self.username = username
        self.password = password
        self.empId = empId
        self.agents = []

    def addAgent(self, agentName, agentPhoneNumber, agentCode):
        agent = Agent(agentName, agentPhoneNumber, agentCode)
        self.agents.append(agent)  # Append to list

        # Save agent to file in CSV format
        filename = "agents.txt"
        with open(filename, "a") as file:
            file.write(f"{agentName},{agentPhoneNumber},{agentCode}\n")

        print("Agent added successfully.")

    def viewAgents(self):
        filename = "agents.txt"
        agents = []

        # Check if file exists
        if not os.path.exists(filename):
            print("No agents found. The file does not exist.")
            return

        # Read agent details from file
        try:
            with open(filename, "r") as file:
                lines = file.readlines()

            if not lines:
                print("No agents found. The file is empty.")
                return

            for line in lines:
                # Split the line by commas and strip whitespace
                parts = line.strip().split(",")
                if len(parts) == 3:  # Ensure there are exactly 3 parts
                    agentName, agentPhone, agentCode = parts
                    agents.append(Agent(agentName, agentPhone, agentCode))
                else:
                    print(f"Skipping invalid line: {line.strip()}")

            # Display agents
            if agents:
                print("Agents List:")
                for agent in agents:
                    print(agent)  # This will use the __str__ method of the Agent class
            else:
                print("No valid agents found in the file.")

        except Exception as e:
            print(f"Error while reading the file: {e}")
    def policyComparison(self, policies):
        print()
        print("┌───────────────────────────────────┐")
        print("│      POLICY COMPARISON TOOL       │")
        print("└───────────────────────────────────┘")

        # Display policy details for each policy
        for index, policy in enumerate(policies, start=1):
            print(f"\nPolicy {index}: {policy['name']}")
            print("Age Criteria:", policy['age_criteria'])

        # Allow the user to select policies for comparison
        while True:
            try:
                selection = input("\nEnter the policy numbers you want to compare (comma-separated): ")
                policy_numbers = [int(num.strip()) for num in selection.split(',')]
                if not all(1 <= num <= len(policies) for num in policy_numbers):
                    raise ValueError("Invalid selection. Please enter valid policy numbers.")
                break
            except ValueError as ve:
                print("Error:", ve)

        # Store comparison results in a text file
        file_name = "Policy_Comparison_Report.txt"
        with open(file_name, "w") as writer:
            writer.write("Policy Comparison Report\n")
            # writer.write("────────────────────────────────────────────\n")

            for num in policy_numbers:
                policy = policies[num - 1]
                writer.write(f"\nPolicy {num}: {policy['name']}\n")
                writer.write(f"Premium Paying Term: {policy['premium_paying_term']}\n")
                writer.write(f"Payout Period: {policy['payout_period']}\n")
                writer.write(f"Death Benefit: {policy['death_benefit']}\n")
                writer.write(f"Minimum Premium: {policy['min_premium']}\n")
                writer.write(f"Age Criteria: {policy['age_criteria']}\n")
                # writer.write("────────────────────────────────────────────\n")

        print("\nComparison complete! Results saved in 'Policy_Comparison_Report.txt'.")

    
    def getAgentNameFromCode(self, agentCode):
        try:
            with open("agents.txt", "r") as file:
                for line in file:
                    # Split the line by commas and strip whitespace
                    details = line.strip().split(",")
                    if len(details) == 3 and details[2].strip() == agentCode.strip():
                        return details[0].strip()  # Return agent name
            return None  # Agent not found
        except FileNotFoundError:
            print("Agents file not found.")
            return None
        except Exception as e:
            print("Error while retrieving agent name:", e)
            return None
    def PremiumCalculator(self):
        print()
        print("┌────────────────────────────────────────────────────────┐")
        print("│                PREMIUM CALCULATOR                      │")
        print("├────────────────────────────────────────────────────────┤")
        print("│ 1. Income Builder Policy                               │")
        print("│ 2. Guaranteed Plan Policy                              │")
        print("│ 3. Return to Menu                                      │")
        print("├────────────────────────────────────────────────────────┤")
        print("│ Please select an option (1-3):                         │ ")
        print("└────────────────────────────────────────────────────────┘")

        try:
            policyChoice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return self.PremiumCalculator()

        if policyChoice == 1:
            try:
                premium = float(input("Enter premium for Income Builder Policy (must be at least 15,000): "))
                age = int(input("Enter age (must be between 1 to 50): "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                return self.PremiumCalculator()

            self.IncomePolicyCalculator(premium, age)  # Calls the updated function that stores data in a file

        elif policyChoice == 2:
            try:
                age2 = int(input("Enter customer's age (must be between 18 to 65): "))
                premium2 = float(input("Enter premium for Guaranteed Plan Policy (must be at least 20,000): "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                return self.PremiumCalculator()

            self.GP(premium2, age2)  # Calls the updated function that stores data in a file

        elif policyChoice == 3:
            return  # Exit the function

        else:
            print("Invalid choice. Please select a valid option (1-3).")
            return self.PremiumCalculator()

    
    def GuaranteedPlanPolicyCalculator(self, agentCode, customerName, customerPhoneNumber, age):
        # Get premium input
        try:
            premium = float(input("Enter Premium (must be at least 20,000): "))
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value for premium.")
            return

        # Validate premium
        if premium < 20000:
            print("Error: Premium must be at least 20,000.")
            return

        # Validate age
        if not (18 <= age <= 65):
            print("Error: Age must be between 18 and 65.")
            return

        # Policy details
        premiumPayingTerm = 10
        maturityYear = 15
        ageIncrementStart = 65

        # Calculate age-based increment (0.5% per year below 65)
        ageBasedIncrement = (ageIncrementStart - age) * 0.005  

        # Calculate policy returns
        premiumterm = premium * premiumPayingTerm
        tenYearReturn = 1.4 * premiumterm
        ageIncrementAmount = ageBasedIncrement * tenYearReturn
        totalPremiumReturn = premiumterm + tenYearReturn + ageIncrementAmount

        # Calculate death benefit
        deathBenefit = 11.0 * premium

        # Generate policy details file
        fileName = f"Customer_{customerName}_PolicyDetails.txt"
        with open(fileName, "w") as writer:
            writer.write(f"Agent Code: {agentCode}\n")
            writer.write(f"Customer Name: {customerName}\n")
            writer.write(f"Customer Phone Number: {customerPhoneNumber}\n")
            writer.write(f"Premium Paid: {premium}\n\n")

            writer.write("**Guaranteed Plan Policy Details:**\n")
            writer.write(f"Premium Paying Term: {premiumPayingTerm} years\n")
            writer.write(f"Maturity Year: {maturityYear}\n")
            writer.write(f"Death Benefit: {deathBenefit}\n")
            writer.write(f"Premium Return at 15th Year (Age-Based): {totalPremiumReturn}\n")

            writer.write("\n**Please forward these policy details to the customer.**\n")

        print(f"Policy details saved to {fileName}")

        # Write customer details to customers.txt
        with open("customers.txt", "a") as file:
            file.write(f"{agentCode},{customerName},{customerPhoneNumber},Guaranteed Plan,{premium},{age}\n")

        print("Customer added successfully.")
   
    def GP(self, premium, age):
        # Define policy details
        premiumPayingTerm = 10
        maturityYear = 15
        ageIncrementStart = 65

        # Validate age
        if not (18 <= age <= 65):
            print("Error: Age must be between 18 and 65.")
            return

        # Validate premium
        if premium < 20000:
            print("Error: Premium must be at least 20,000. Cannot calculate policy details.")
            return

        # Calculate age-based increment (0.5% per year below 65)
        ageBasedIncrement = (ageIncrementStart - age) * 0.005  

        # Calculate policy returns
        premiumterm = premium * premiumPayingTerm
        tenYearReturn = 1.4 * premiumterm
        ageIncrementAmount = ageBasedIncrement * tenYearReturn
        totalPremiumReturn = premiumterm + tenYearReturn + ageIncrementAmount

        # Calculate death benefit
        deathBenefit = 11.0 * premium

        # Display policy details
        print("\nPolicy Details:")
        print("┌───────────────────────────────────────────────┐")
        print("│          **Guaranteed Plan Policy**          │")
        print("├───────────────────────────────────────────────┤")
        print(f"│ Premium Paying Term: {premiumPayingTerm} years              │")
        print(f"│ Maturity Year: {maturityYear}                        │")
        print(f"│ Minimum Premium: 20,000                         │")
        print(f"│ Age Condition: 18 to 65 years                   │")
        print(f"│ Death Benefit: {deathBenefit:,.2f}                  │")
        print("├───────────────────────────────────────────────┤")
        print("│          **Projected Returns & Benefits**     │")
        print("├───────────────────────────────────────────────┤")
        print(f"│ Total Premium Paid: {premiumterm:,.2f}                │")
        print(f"│ 10-Year Return: {tenYearReturn:,.2f}                 │")
        print(f"│ Age-Based Bonus: {ageIncrementAmount:,.2f}            │")
        print(f"│ Total Premium Return at {maturityYear}th Year: {totalPremiumReturn:,.2f} │")
        print("└───────────────────────────────────────────────┘")

    
    def IncomePolicyCalculator(self, premium, age):
        if premium < 15000 or not (1 <= age <= 50):
            print("Error: Premium must be at least 15,000 and age must be between 1 to 50.")
            return

        # Policy details
        premiumPayingTerm = 10
        payoutPeriod = 30
        deathBenefit = 10 * premium
        premiumPaidAfter10thYear = (premium * (payoutPeriod - premiumPayingTerm)) / 100
        returnEachYear = premiumPaidAfter10thYear + premium
        totalReturn = returnEachYear * (payoutPeriod - premiumPayingTerm)

        # Display policy details
        print("\nPolicy Details:")
        print("┌───────────────────────────────────────────────┐")
        print("│           **Income Builder Policy**          │")
        print("├───────────────────────────────────────────────┤")
        print(f"│ Premium Paid: {premium:,.2f}                          │")
        print(f"│ Premium Paying Term: {premiumPayingTerm} years              │")
        print(f"│ Payout Period: {payoutPeriod} years                │")
        print(f"│ Death Benefit: {deathBenefit:,.2f}                    │")
        print("├───────────────────────────────────────────────┤")
        print("│         **Projected Returns & Benefits**      │")
        print("├───────────────────────────────────────────────┤")
        print(f"│ Total premium paid after the 10th year: {premiumPaidAfter10thYear:,.2f} │")
        print(f"│ Annual return from 11th to {payoutPeriod}th year: {returnEachYear:,.2f} │")
        print(f"│ Total return over {payoutPeriod - premiumPayingTerm} years: {totalReturn:,.2f} │")
        print("└───────────────────────────────────────────────┘")

    
    def IncomePolicyBuilder(self, agentCode, customerName, customerPhoneNumber):
        print("Enter Premium (must be greater than or equal to 15000):")
        premium = float(input())
        print("Enter age [must be between 1 to 50]:")
        age = int(input())

        if premium >= 15000 and 1 <= age <= 50:
            # Write customer details to customers.txt
            with open("customers.txt", "a") as file:
                file.write(f"{agentCode},{customerName},{customerPhoneNumber},incomebuilder Plan,{premium},{age}\n")
            premiumPayingTerm = 10
            payoutPeriod = 30
            deathBenefit = 10 * premium
            premiumPaidAfter10thYear = (premium * (payoutPeriod - premiumPayingTerm)) / 100
            returnEachYear = premiumPaidAfter10thYear + premium
            totalReturn = returnEachYear * (payoutPeriod - premiumPayingTerm)

            print("\nPolicy Details:")
            print("**Income Builder Policy:**")
            print("Premium Paid:", premium)
            print("Premium Paying Term:", premiumPayingTerm, "years")
            print("Payout Period:", payoutPeriod, "years")
            print("Death Benefit:", deathBenefit)
            print("\n**Calculations:**")
            print("Return each year from 11th to", payoutPeriod, "th year:", returnEachYear)
            print("Total return over", (payoutPeriod - premiumPayingTerm), "years:", totalReturn)
            print()

            # Save policy details in a separate text file
            fileName = f"Customer_{customerName}_PolicyDetails.txt"
            with open(fileName, "w") as writer:
                agent_name = self.getAgentNameFromCode(agentCode)
                if agent_name:
                    writer.write("Agent Name: " + agent_name + "\n")
                else:
                    print("Error: Agent with code", agentCode, "does not exist.")

                writer.write(f"Customer Name: {customerName}\n")
                writer.write(f"Customer Phone Number: {customerPhoneNumber}\n")
                writer.write(f"Premium Paid: {premium}\n\n")

                writer.write("**Policy Details:**\n")
                writer.write("**Income Builder Policy:**\n")
                writer.write(f"Premium Paying Term: {premiumPayingTerm} years\n")
                writer.write(f"Payout Period: {payoutPeriod} years\n")
                writer.write(f"Death Benefit: {deathBenefit}\n")
                writer.write(f"Total premium paid after the 10th year: {premiumPaidAfter10thYear}\n")
                writer.write(f"Return each year from 11th to {payoutPeriod}th year: {returnEachYear}\n")
                writer.write(f"Total return over {payoutPeriod - premiumPayingTerm} years: {totalReturn}\n")

            print("Policy details written to", fileName)
            print("Customer added successfully.")
        else:
            print("Premium must be at least 15000 and age must be between 1 to 50.")
    
    
    def addCustomer(self):
        agentCode = input("Enter Agent Code to add a customer: ").strip()

        # Check if the agent code exists in agents.txt
        if not self.agentExists(agentCode):
            print("Agent with code", agentCode, "does not exist.")
            return

        # Proceed with adding customer details
        print("Enter Customer Name:", end=" ")
        customerName = input().strip()
        print("Enter Customer Phone Number:", end=" ")
        customerPhoneNumber = input().strip()

        if not self.isValidPhoneNumber(customerPhoneNumber):
            print("Invalid phone number format. Please enter a valid phone number.")
            return

        print()
        print("┌────────────────────────────────────────────────────┐")
        print("│            Policies In Our Company                 │")
        print("├────────────────────────────────────────────────────┤")
        print("│ 1. Income Builder Policy                           │")
        print("│ 2. Guaranteed Plan Policy                          │")
        print("│ 3. Return to Employee Menu                         │")
        print("├────────────────────────────────────────────────────┤")
        print("│ Please select an option (1-3):                     │")
        print("└────────────────────────────────────────────────────┘")
        policyChoice = int(input())

        if policyChoice == 1:
            self.IncomePolicyBuilder(agentCode, customerName, customerPhoneNumber)
        elif policyChoice == 2:
            print("Enter age [must be between 18 to 65]:", end=" ")
            age = int(input())
            self.GuaranteedPlanPolicyCalculator(agentCode, customerName, customerPhoneNumber, age)
        elif policyChoice == 3:
            return
        else:
            print("Invalid choice. Please choose a valid option.")
            return
    def displayCustomers(self, agentCode):
        # Check if the agent exists
        if not self.agentExists(agentCode):
            print("No agent found with code:", agentCode)
            return

        agentName = self.getAgentNameFromCode(agentCode)
        customers_found = False

        try:
            with open("customers.txt", "r") as file:
                customers = file.readlines()

            print(f"Customers of Agent {agentName}\n")
            for customer in customers:
                details = customer.strip().split(",")
                if details[0].strip() == agentCode.strip():  # Check if customer belongs to the given agent
                    customers_found = True
                    customerName, customerPhoneNumber = details[1], details[2]
                    print("Customer Name:", customerName)
                    print("Customer Phone Number:", customerPhoneNumber)
                    print()

            if not customers_found:
                print("No customers found for agent:", agentName)

        except FileNotFoundError:
            print("No customer records found.")
        except Exception as e:
            print("Error while retrieving customer data:", e)
    
    def agentExists(self, agentCode):
        """Check if agent exists in agents.txt"""
        try:
            with open("agents.txt", "r") as file:
                for line in file:
                    # Split the line by commas and strip whitespace
                    data = line.strip().split(",")
                    if len(data) == 3 and data[2].strip() == agentCode.strip():
                        return True
        except FileNotFoundError:
            print("Agents file not found.")
        except Exception as e:
            print("Error while checking agent existence:", e)
        return False
    def isValidPhoneNumber(self, phoneNumber):
        return phoneNumber.isdigit() and len(phoneNumber) == 10

# class overrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr


# agebt classssssssssssssssssssssssssssssssssssssss

class Agent:
    def __init__(self, agent_name, agent_phone_number, agent_code):
        self.agent_name = agent_name
        self.agent_phone_number = agent_phone_number
        self.agent_code = agent_code
        self.assigned_employee = None

    def get_agent_name(self):
        return self.agent_name

    def set_agent_name(self, agent_name):
        self.agent_name = agent_name

    def get_agent_phone_number(self):
        return self.agent_phone_number

    def set_agent_phone_number(self, agent_phone_number):
        self.agent_phone_number = agent_phone_number

    def get_agent_code(self):
        return self.agent_code

    def set_agent_code(self, agent_code):
        self.agent_code = agent_code

    def get_assigned_employee(self):
        return self.assigned_employee

    def set_assigned_employee(self, assigned_employee):
        self.assigned_employee = assigned_employee
    def __str__(self):
        return (f"Agent Name: {self.agent_name}, "
                f"Phone Number: {self.agent_phone_number}, "
                f"Agent Code: {self.agent_code}")
# agebt overrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

def viewPolicies():
    print()
    print("----------------------------------------------------")
    print("                Policy 1: Income Builder            ")
    print("----------------------------------------------------")
    print("  Policy Details:")
    print("- Premium Paying Term: 10 years")
    print("- Payout Period: 30 years")
    print("- Death Benefit: 10 times the premium paid for the first 10 years, and from the 11th to 30th year, the death benefit increases by 0.5%")
    print("- Minimum Premium: 15,000")
    print("- Age Condition: Between 1 to 50 years")
    print()
    print("---------------------------------------------------------------------------------------")
    print("               Policy 2: Guaranteed Plan            ")
    print("----------------------------------------------------------------------------------------")
    print("  Policy Details:")
    print("- Premium Paying Term: 10 years")
    print("- Guaranteed Return: Provided on the 15th year")
    print("- Age Criteria: 18 to 65 years")
    print("- Minimum Premium: 20,000")
    print("- Death Benefit: 11 times the premium paid")
    print()
    print("- Premium Return Calculation:")
    print("Premium return at 15th year is based on age.")
    print("The return includes the total premium paid until the 10th year plus 140%.")
    print("Age-based increment starts from age 65 and increases by 0.5% per year until age 18.")
    print("-----------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------")


def isValidPhoneNumber(mobile):
    return mobile.isdigit() and len(mobile) == 10

def signUp():
    filename = "employees.txt"

    print("Enter company code: ")
    companyCode = input().strip()

    if companyCode != "AE303":
        print("Invalid company code. Sign-up failed.")
        return
    
    newUsername = input("Enter new username: ").strip()
    newPassword = input("Enter new password: ").strip()

    # Validate password (at least 8 chars, must contain a number)
    if len(newPassword) < 8 or not any(char.isdigit() for char in newPassword):
        print("Password must be at least 8 characters long and contain at least one number.")
        return

    name = input("Enter name: ").strip()
    email = input("Enter Email ID: ").strip()
    mobile = input("Enter Mobile Number (10 digits): ").strip()

    # Validate phone number
    if not isValidPhoneNumber(mobile):
        print("Invalid phone number. Please enter a 10-digit number.")
        return

    post = input("Enter Post: ").strip()
    qualification = input("Enter Qualification: ").strip()

    # Save credentials to employees.txt
    with open(filename, "a") as file:
        file.write(f"{newUsername} {newPassword}\n")

    print("Sign-up successful. Employee data saved.")

def signIn():
    filename = "employees.txt"
    
    # Ensure the file exists
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            pass  # Creates an empty file
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    # Read file and check credentials
    with open(filename, "r") as file:
        for line in file:
            credentials = line.strip().split(maxsplit=1)  # Split only at the first space
            if len(credentials) == 2:
                stored_username, stored_password = credentials
                if stored_username == username and stored_password == password:
                    print("Sign-in successful. Welcome, " + username + "!")
                    return Employee(username, password, None)  # Return an Employee object

    print("Invalid credentials. Sign-in failed.")
    return None

def employeeMenu(employee):
    while True:
        print()
        print("┌────────────────────────────────────────────────────┐")
        print("│            Welcome to Employee Menu                │")
        print("├────────────────────────────────────────────────────┤")
        print("│ 1. Add New Agent                                   │")
        print("│ 2. View Employee Agents                            │")
        print("│ 3. Add New Customer                                │")
        print("│ 4. View Customers                                  │")
        print("│ 5. Premium Calculator                              │")
        print("│ 6. Sign-out                                        │")
        print("├────────────────────────────────────────────────────┤")
        print("│ Please select an option (1-6):                     │ ")
        print("└────────────────────────────────────────────────────┘")
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if choice == 1:
            # Add Agent
            print("Enter agent name:")
            agentName = input()
            print("Enter agent phone number (10 DIGIT):")
            agentPhoneNumber = input()
            if not isValidPhoneNumber(agentPhoneNumber):
                print("Invalid phone number format. Please enter a valid phone number.")
                return
            print("Enter agent code:")
            agentCode = input()
            employee.addAgent(agentName, agentPhoneNumber, agentCode)
        elif choice == 2:
            # View Agents
            employee.viewAgents()
        elif choice == 3:
            # Add Customer
            employee.addCustomer()
        elif choice == 4:
            # View Customers
            print("Enter Agent Code to view customers:")
            agentCode = input()
            print()
            employee.displayCustomers(agentCode)
        elif choice == 5:
            employee.PremiumCalculator()
        elif choice == 6:
            # Exit
            print("Exiting employee menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def main():
    while True:
        print()
        print("┌──────────────────────────────────────────────┐")
        print("│            Welcome to Main Menu              │")
        print("├──────────────────────────────────────────────┤")
        print("│ 1. Sign In                                   │")
        print("│ 2. Sign Up                                   │")
        print("│ 3. View Company Policy                       │")
        print("│ 4. Premium Calculator                        │")
        print("│ 5. Policy Comparision                        │")
        print("│ 6. Exit                                      │")
        print("├──────────────────────────────────────────────┤")
        print("│ Please select an option (1-5):               │ ")
        print("└──────────────────────────────────────────────┘")
        
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if choice == 1:
            employee = signIn()
            if employee:
                print("Employee menu is shown")
                employeeMenu(employee)
        elif choice == 2:
            signUp()
        elif choice == 3:
            viewPolicies()
        elif choice == 4:
            employee = Employee(None, None, None)
            employee.PremiumCalculator()
        elif choice == 5:
            choice = input("Do you want to compare insurance policies? (yes/no): ")
            if choice.lower() == 'yes':
                policies = [
                    {
                        'name': 'Income Builder Policy',
                        'premium_paying_term': '10 years',
                        'payout_period': '30 years',
                        'death_benefit': '10 times premium paid (10-30 years)',
                        'min_premium': '15,000',
                        'age_criteria': '1-50 years'
                    },
                    {
                        'name': 'Guaranteed Plan Policy',
                        'premium_paying_term': '10 years',
                        'payout_period': 'Guaranteed Return Provided on the 15th year',
                        'death_benefit': '11 times premium paid',
                        'min_premium': '20,000',
                        'age_criteria': '18-65 years'
                    }
                ]
                employee = Employee(None, None, None)
                employee.policyComparison(policies)
            elif choice.lower() == 'no':
                print("Thank you. Returning Back to Main menu.")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()