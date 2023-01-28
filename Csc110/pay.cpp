#include <iostream>

/**
 * 1/28/2023
 * CSC111 - Homework 1
 * Programming Challenge 2.6: Annual Pay
 */

float getAnnualPay(float payAmount,int payPeriods)
{
    float annualPay = payAmount * payPeriods;
    return annualPay;
}


int main()
{
    const float payAmount = 2200.0;
    const int payPeriods = 26;
    float annualPay = 0;

    annualPay = getAnnualPay(payAmount, payPeriods);
    std::cout<<"Total Annual Pay is: $" << annualPay<< std::endl;
    return 0;
}


