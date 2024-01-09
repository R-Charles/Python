//Given an array and a value Y, count and print the number of array values greater than Y

//  Step 1  Create a function that takes in an array 
//  Step 2  Create an empty value Y 
//  Step 3  The function should iterate through the array and compare each value to Y
//  Step 4  It should then count and print the number of array values greater than Y

function getGreaterY(arr){
    let Y = 0;
    result = []
    for (let i = 1; i <= arr.length; i++){
        if (Y < arr[i]){
            result.push(arr[i]);
        }
    }
    return arr[i];
}

const GreaterY = getGreaterY([1, 3, 5,]);
console.log(result);