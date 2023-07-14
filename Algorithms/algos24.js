// Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

// Examples
// Input: [1, 5.2, 4, 0, -1]
// Output: 9.2

// Input: []
// Output: 0

// Input: [-2.398]
// Output: -2.398

// Assumptions
// You can assume that you are only given numbers.
// You cannot assume the size of the array.
// You can assume that you do get an array and if the array is empty, return 0.
// What We're Testing
// We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
// Advanced users may find this extremely easy and can easily write this in one line.

//sum numbers
let array = [2, 5.5, 6, 0, -2]

function sum (numbers) {
    "use strict";
  
    let total=0;
    
    if(numbers.len==0){
        return total;
    }else{
        for(let y=0; y<numbers.len; y++){
            total+=numbers[y];
            console.log(total);
        }
    }
    return total;
    }
    
    console.log(sum(array));

    // OPTIMIZED CODE

function sum(numbers) {
    return numbers.reduce((a,b) => a+b, 0);
}

let numbers = [1, 2, 3, 4, 5];
let product = numbers.reduce((accumulator, current) => accumulator * current, 1);
console.log(product); // Output: 120

