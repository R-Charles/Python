//create a method that takes a boolean value and returns a "yes" string for true and a "no" string for false
/*

const answer = {
    True: "Yes",
    False: "No",

    getAnswer: function() {
        if
    }
}


*/

function convertBoolean(value) {
    if (value === true) {
      return "yes";
    } else if (value === false) {
      return "no";
    } 
  }
  
  const result1 = convertBooleanToYesNo(true); // Returns "yes"
  const result2 = convertBooleanToYesNo(false); // Returns "no"
  
  console.log(result1);
  console.log(result2);
  


/*

OTHER SOLUTIONS

Solution #1(BEST PRACTICES)
function boolToWord( bool ){
  return bool ? 'Yes':'No';
}

Solution #2
const boolToWord = bool => bool ? 'Yes' : 'No';

*/