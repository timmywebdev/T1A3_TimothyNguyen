# **T1A3 - Terminal Application Timothy Nguyen**

## **Table of contents**

[**T1A3 - Terminal Application: Timothy Nguyen**](#t1a3---terminal-application-timothy-nguyen)
[**Table of contents**](#table-of-contents)
- [**T1A3 - Terminal Application Timothy Nguyen**](#t1a3---terminal-application-timothy-nguyen)
  - [**Table of contents**](#table-of-contents)
  - [**R4 - Links**](#r4---links)
  - [**R5 - Styling Conventions**](#r5---styling-conventions)
  - [**R6 - Features**](#r6---features)
    - [**Feature 1 - Deposit Money**](#feature-1---deposit-money)
    - [**Feature 2 - Enter Bet Amount**](#feature-2---enter-bet-amount)
    - [**Feature 3 - Check Win then Pay Winnings**](#feature-3---check-win-then-pay-winnings)
    - [**Feature 4 - Slot Randomisation**](#feature-4---slot-randomisation)
    - [**Feature 5 - Slot Spinning Animation**](#feature-5---slot-spinning-animation)
    - [**Feature 6 - Check Win then Pay Winnings**](#feature-6---check-win-then-pay-winnings)
  - [**R7 - Implementation Plan**](#r7---implementation-plan)
  - [**R8 - Help Documentation**](#r8---help-documentation)

## **R4 - Links**

- [Github Repo](https://github.com/timmywebdev/TimothyNguyen_T1A3)
- [Slide Deck Presentation link - Youtube]()
- [Slide Deck PDF]()

## **R5 - Styling Conventions**

- PEP 8 – Style Guide for Python Code (<https://peps.python.org/pep-0008/>)

## **R6 - Features**

### **Feature 1 - Deposit Money**

The Deposit Money feature occurs when the game has just begun and there is no credits in the machine. The user will be able to input a money amount and it will be automatically added to the credits. The variable that the credits fall under is in the 'Game' class. The Game class handles multiple variables that are used throughout the code. 

As credits is an integer value, there are a few errors that can occur when taking the value from the input variable. These errors will occur when the input consists of letters, symbols or even if it is blank. Here is the code for this feature.

``` Py
if Game.credits <= 0 and RUNNING is True:
    os.system("clear")
    layout()
    deposit = input(" There are currently no credits in the machine. \n How much would you like to deposit?\n > ")
    if deposit.isdigit():
        deposit = int(deposit)
        if deposit >= 1:
            Game.credits += deposit
        else: 
            print(" Please enter a number larger than 0!")
            press_to_continue()
    else:
        print (" Please enter a real number!")
        press_to_continue()

```

| Input               | Error? | Implementation to fix                                                                |
|---------------------|--------|--------------------------------------------------------------|
| any input that does | yes    | I used deposit.isdigit() to make sure the input contains     |
| not have digits     |        | digits. This makes sure that turning the input into an       |
|                     |        | integer will work. If the input does not only contain digits |





- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

### **Feature 2 - Enter Bet Amount**

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

### **Feature 3 - Check Win then Pay Winnings**

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

### **Feature 4 - Slot Randomisation**

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

### **Feature 5 - Slot Spinning Animation**

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

### **Feature 6 - Check Win then Pay Winnings**

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

## **R7 - Implementation Plan**

- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item
- Utilise a suitable project management platform to track this implementation plan.
- Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 
- Your checklists for each feature should have at least 5 items.

## **R8 - Help Documentation**

- Design help documentation which includes a set of instructions which accurately describe how to use and install the application.
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application