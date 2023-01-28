#include <iostream>

/**
 * 1/28/2023
 * CSC111 - Lab 1
 * Programing Challenge 2.11: Distance per Tank of Gas
 */

float getDistance(float numberOfGallons, float milesPerGallon)
{
    float distance = 0;
    distance = numberOfGallons * milesPerGallon;

    return distance;
}

int main()
{
    float distance = 0;
    const float numberOfGallons = 20.0;
    const float milesPerGallonInTown = 23.5;
    const float milesPerGallonInHighway = 28.9;

    distance = getDistance(numberOfGallons, milesPerGallonInTown);
    std::cout << "The distance in town is: " << distance << "miles" << std::endl;
    distance = getDistance(numberOfGallons, milesPerGallonInHighway);
    std::cout << "The distance in highway is: " << distance << "miles" << std::endl;

    return 0;
}
