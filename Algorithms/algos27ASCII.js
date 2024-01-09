// Get ASCII value of a character.

// For the ASCII table you can refer to http://www.asciitable.com/

function getASCII(c) {
    // Check if the input is a single character
    if (c.length === 1) {
      // Use charCodeAt to get the ASCII value
      const asciiValue = c.charCodeAt(0);
      return asciiValue;
    } else {
      // If the input is not a single character, return an error message or handle it as needed
      return "Input is not a single character";
    }
  }
  
  // Example usage:
  const char = "A";
  const char2 = "f";
  const ascii = getASCII(char);
  const ascii2 = getASCII(char2);
  console.log(`The ASCII value of ${char} is ${ascii}`);
  console.log(`The ASCII value of ${char2} is ${ascii2}`);

  /*

  function getASCII(c) {
    if (c.length === 1) {
      const asciiValue = c.charCodeAt(0);
      return asciiValue;
    } else {
      return "Input is not a single character";
    }
  }
  
  const char = "A";
  const char2 = "f";
  const ascii = getASCII(char);
  const ascii2 = getASCII(char2);
  console.log(`The ASCII value of ${char} is ${ascii}`);
  console.log(`The ASCII value of ${char2} is ${ascii2}`);



  */