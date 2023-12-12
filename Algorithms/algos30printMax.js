//Given an array find and print the maximum element

//  Step 1 create a function that takes in an array of integers 
//  Step 2 set a variable to contain an element 
//  Step 3 write a for loop to iterate through each element
//  Step 4 write an if statment to compare current index to next 
//  each element to find the max number 


function getMax(arr){
    let max = arr[0];   //this variable is to contain an element
    for (let i=1; i<arr.length; i++){   //iterates through the elements of the array 
        if(arr[i]>max) {    //compares new element to previous element 
            max = arr[i];   //replaces higher valued integer

        }
    }
    return max; //returns maximum value
}

//console.log(getMax([5,6,7,8]));
const maxNumber = getMax([1, 3, 5,]);
console.log("The maximum number is:", maxNumber);