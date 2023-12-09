// Print all integers from 0 to 255 and print the sum of each so far

/*  Step 1 create an empty array
    Step 2 array must iterate through all integers 0 to 255
    Step 3 declare a variable (sum = 0)
    Step 3 each iteration must add the sum of subsequent integers
    Step 4 print out each sum
*/ 

// let sum = [];
// for (let i=0; i<= 3; i++){
//     sum+=sum +i;
//     sum.push(i);

// }
// console.log(sum);

let sum = 0;
for (let i=0; i<= 3; i++){
    sum += i;

    console.log(sum);
}
