// Yes, you can transform an integer into a string without using the `.toString()` method or template literals by manually iterating over the digits of the number. Here's a step-by-step explanation of how you can do this:

// **Method 3: Manually Converting to String**

// 1. Define a JavaScript function that takes an integer as an argument.
// 2. Initialize an empty string to store the result.
// 3. Check if the number is negative. If it is, append a minus sign (`-`) to the result string and make the number positive for the following steps.
// 4. Use a loop to iterate over the digits of the number:
//    - Inside the loop, find the last digit of the number using the modulo operator `%`.
//    - Convert the last digit to a character using the ASCII value, which can be done by adding the character code of `'0'` to the digit.
//    - Append the character to the result string.
//    - Remove the last digit from the number by dividing it by 10 (integer division).
//    - Repeat these steps until the number becomes 0.
// 5. If the original number was negative, prepend the minus sign to the result string.
// 6. Return the result string.

// Here's the code for this method:

// ```javascript
// function numberToString(number) {
//   // Initialize an empty string to store the result
//   let result = '';
  
//   // Check if the number is negative
//   if (number < 0) {
//     // Append a minus sign to the result and make the number positive
//     result += '-';
//     number = -number;
//   }

//   // Handle the case when the number is 0 separately
//   if (number === 0) {
//     return '0';
//   }

//   // Iterate over the digits of the number
//   while (number > 0) {
//     // Find the last digit and convert it to a character
//     const lastDigit = number % 10;
//     const charDigit = String.fromCharCode(lastDigit + 48); // ASCII '0' is 48
//     // Append the character to the result string
//     result = charDigit + result;
//     // Remove the last digit from the number
//     number = Math.floor(number / 10);
//   }

//   // Return the result string
//   return result;
// }

// // Example usage:
// const num = -100;
// const str = numberToString(num);
// console.log(str); // Output: "-100"
// ```

// This method manually converts the integer into a string without using `.toString()` or template literals. It's a more complex approach but gives you full control over the conversion process.

// ......................................................................................................


// We need a function that can transform a number (integer) into a string.

// What ways of achieving this do you know?

// Examples (input --> output):
// 123  --> "123"
// 999  --> "999"
// -100 --> "-100"

function numberToString(num) {
    // Return a string of the number here!
    const result = num.toString();

    return result;
}

  const num = -2;
  const str = numberToString(num);
  console.log(str); 