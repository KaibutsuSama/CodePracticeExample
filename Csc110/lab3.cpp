/**
* Lab3 CSC110 XinLeroy Liu
A software company sells a package that retails for $99.  Quantity discounts are given according to the following table.
Quantity	Discount
10–19	20%
20–49	30%
50–99	40%
100 or more	50%
Write a program that asks for the number of units sold and computes the total cost of the purchase.
Input Validation: Make sure the number of units is greater than 0.
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const float PACKAGE_PRICE = 99; // Price of package $99
    int quantityNumber; // Quantity
    float discountRate; // DiscountRate
    float priceBeforeDiscount; // priceBeforeDiscount
    float discount; // discount
    float totalPrice; // totalPrice

    // Formatting Values
    int leftWeight = 20;
    int rightWeight = 17;
    int decimalPoint = 3;

    cout << "Enter the number of packages sold\n";
    cin >> quantityNumber;

    if (quantityNumber <= 0) {
        cout << "You must give a value as >= 0";
        return 0;
    } else {
        priceBeforeDiscount = PACKAGE_PRICE * quantityNumber;
        if (quantityNumber >= 100) {
            discountRate = 0.5;
        } else if (quantityNumber >= 50) {
            discountRate = 0.4;
        } else if (quantityNumber >= 20) {
            discountRate = 0.3;
        } else if (quantityNumber >= 10) {
            discountRate = 0.2;
        } else {
            discountRate = 0;
        }
        discount = priceBeforeDiscount * discountRate;
        totalPrice = priceBeforeDiscount - discount;
    }

    cout << setw(leftWeight) << left << "Already sold: " << setw(rightWeight) << right << fixed << quantityNumber
         << endl;
    cout << setw(leftWeight) << left << "Cost: $" << setw(rightWeight) << right << setprecision(decimalPoint) << fixed
         << priceBeforeDiscount << endl;
    cout << setw(leftWeight) << left << "Discount rate:" << setw(rightWeight - 1) << right << setprecision(discountRate)
         << discountRate * 100 << "%" << endl;
    cout << setw(leftWeight) << left << "You save: $" << setw(rightWeight) << right << setprecision(decimalPoint)
         << fixed << discount << endl;
    cout << setw(leftWeight) << left << "Total price is: $" << setw(rightWeight) << right
         << setprecision(decimalPoint) << fixed << totalPrice << endl;
    return 0;
}