/**
* Programming Challenge 4.15: Shipping Charges
The Fast Freight Shipping Company charges the following rates:
Weight of Package (in Kilograms)	Rate per 500 Miles Shipped
2 kg or less	$1.10
Over 2 kg but not more than 6 kg	$2.20
Over 6 kg but not more than 10 kg	$3.70
Over 10 kg but not more than 20 kg	$4.80

Write a program that asks for the weight of the package and the distance it is to be shipped, then displays the charges.
Input Validation: Do not accept values of 0 or less for the weight of the package. Do not accept weights of more than 20 kg
 (this is the maximum weight the company will ship). Do not accept distances of less than 10 miles or more than 3,000 miles.
 These are the company's minimum and maximum shipping distances.
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MIN_WEIGHT = 0;
    const int MAX_WEIGHT = 20;
    const int MIN_DISTANCES = 10;
    const int MAX_DISTANCES = 3000;

    float packageWeight, distances, totalPay, shippedRate;

    cout << "What is the weight of your package? （Kg）" << endl;
    cin >> packageWeight;
    if (packageWeight <= MIN_WEIGHT || packageWeight > MAX_WEIGHT) {
        cout << "Sorry, We do not accept the weight of packages less than or equal to 0kg or more than 20kg" << endl;
        return 0;
    } else {
        cout << "What is the distance you want to mail? (MILES) " << endl;
        cin >> distances;
        if (distances < MIN_DISTANCES || distances > MAX_DISTANCES) {
            cout << "We do not accept orders for distances less than 10miles and more than 3000miles" << endl;
            return 0;
        }
        if (packageWeight <= 2) {
            shippedRate = 1.10;
            totalPay = distances / 500 * shippedRate;
        } else if (packageWeight <= 6) {
            shippedRate = 2.20;
            totalPay = distances / 500 * shippedRate;
        } else if (packageWeight <= 10) {
            shippedRate = 3.70;
            totalPay = distances / 500 * shippedRate;
        } else {
            shippedRate = 4.80;
            totalPay = distances / 500 * shippedRate;
        }

        cout << "Total price is:$ " << setw(15) << left << setw(20) << right << setprecision(2) << fixed << totalPay
             << endl;
        cout << "Shipping distances is:" << setw(15) << left << setw(10) << right << distances << "miles" << endl;
        cout << "Package Weight is: " << setw(15) << left << setw(16) << right << packageWeight << "Kg" << endl;
    }

}