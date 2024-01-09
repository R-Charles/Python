//Create an array with all the odd integers between 1 and 255(inclusive)

//  Step 1 Create an empty array 
//  Step 2 Create a variable i=0
//  Step 4 Push new number into the empty array 


let arr = [];
for (val = 0; val <= 255; val++) {
    if ((val % 3 === 0)) {
        arr.push(val);
    }
}
console.log(arr);