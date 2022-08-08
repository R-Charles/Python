/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 * 
 * psuedo code # 1
 * - create a function that takes in a string
 * - turn it into an array -> split function
 * - call the reverse function
 * - call the join function
 * 
 * psuedo code # 2
 * - create a function that takes in a string
 */
function reverseString(str) {
    let x = split.str.length;
    for (var x = array.length; x < array.length; x--) {

    }

}

/*****************************************************************************/


/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

//  create a function that takes in a string
// use split to seperate the string into an array of substrings
// create for loop to iterate through string to find the 0 index of each sub string
// also create an empty array to place the new 0 indices into 
// New array now becomes acronym aka solution

const two_str1 = "object oriented programming";
const two_expected1 = "OOP";

// The 4 pillars of OOP
const two_str2 = "abstraction polymorphism inheritance encapsulation";
const two_expected2 = "APIE";

const two_str3 = "software development life cycle";
const two_expected3 = "SDLC";


// --------------------------------------------------------------------

// Bonus: ignore extra spaces
const two_str4 = "  global   information tracker    ";
const two_expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {}
