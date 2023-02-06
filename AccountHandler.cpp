#include "BankingCommonDecl.h"
#include "AccountHandler.h"
#include "Account.h"
#include "NormalAccount.h"
#include "HighCreditAccount.h"
#include "AccountException.h"

void AccountHandler::ShowMenu(void) const {
	cout << "-----Menu-----" << endl;
	cout << "1. Create Account" << endl;
	cout << "2. Deposit" << endl;
	cout << "3. Withdraw" << endl;
	cout << "4. Print the account information" << endl;
	cout << "5. End of program" << endl;
}

void AccountHandler::MakeAccount(void) {
	int sel;
	cout << "Choose your account type" << endl;
	cout << "1. Saving Account" << endl;
	cout << "2. Checking Account" << endl;
	cout << "Select: ";
	cin >> sel;

	if (sel == NORMAL)
		MakeNormalAccount();
	else
		MakeCreditAccount();
}

void AccountHandler::MakeNormalAccount(void) {
	int id;
	String name;
	int balance;
	int interest;

	cout << "Saving Account" << endl;
	cout << "Account ID: "; cin >> id;
	cout << "Name: "; cin >> name;
	cout << "Amount of deposit: "; cin >> balance;
	cout << "Interest rate: "; cin >> interest;
	cout << endl;
	accArr[accNum++] = new NormalAccount(id, balance, name, interest);
}

void AccountHandler::MakeCreditAccount(void) {
	int id;
	String name;
	int balance;
	int interest;
	int credit;

	cout << "Checking Account" << endl;
	cout << "Account ID: "; cin >> id;
	cout << "Name: "; cin >> name;
	cout << "Deposit amount: "; cin >> balance;
	cout << "Interest rate: "; cin >> interest;
	cout << "Credit Level (1toA, 2toB, 3toC): "; cin >> credit;
	cout << endl;

	switch (credit) {
	case 1:
		accArr[accNum++] = new HighCreditAccount(id, balance, name, interest, LEVEL_A);
		break;
	case 2:
		accArr[accNum++] = new HighCreditAccount(id, balance, name, interest, LEVEL_B);
		break;
	case 3:
		accArr[accNum++] = new HighCreditAccount(id, balance, name, interest, LEVEL_C);
		break;
	}
}

void AccountHandler::DepositMoney(void) {
	int money;
	int id;
	cout << "Deposit" << endl;
	cout << "Account ID: "; cin >> id;
	while (true) {
		cout << "Deposit amount: "; cin >> money;

		try {
			for (int i = 0; i < accNum; i++) {
				if (accArr[i]->GetAccID() == id) {
					accArr[i]->Deposit(money);
					cout << "Deposit success" << endl << endl;
					return;
				}
			}
			cout << "Unvalid ID." << endl << endl;
			return;
		}
		catch (AccountException &expn) {
			expn.ShowExceptionReason();
			cout << "Enter the valid amount." << endl;
		}
	}
}

void AccountHandler::WithdrawMoney(void) {
	int money;
	int id;
	cout << "Withdraw" << endl;
	cout << "Account ID: "; cin >> id;
	while (true)
	{
		cout << "Withdraw amount: "; cin >> money;

		try {
			for (int i = 0; i < accNum; i++) {
				if (accArr[i]->GetAccID() == id) {
					if (accArr[i]->Withdraw(money) == 0) {
						cout << "Declined" << endl << endl;
						return;
					}

					cout << "Withdraw success" << endl << endl;
					return;
				}
			}
			cout << "Unvalid ID.." << endl << endl;
			return;
		}
		catch (AccountException &expn) {
			expn.ShowExceptionReason();
			cout << "Enter the valid amount." << endl;
		}
	}
}

AccountHandler::AccountHandler() : accNum(0) {}

void AccountHandler::ShowAllAccInfo(void) const {
	for (int i = 0; i < accNum; i++) {
		accArr[i]->ShowAccInfo();
		cout << endl;
	}
}

AccountHandler::~AccountHandler() {
	for (int i = 0; i < accNum; i++)
		delete accArr[i];
}