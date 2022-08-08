/* 
Given in an alumni interview in 2021.
String Encode
You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcdddaa";
const expected1 = "a4b2c1d3a2";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 * 
 * 
 * 
 * 
 * PSEUDO CODE...
 * - 
 */
// creating a function that takes in a string 
// create for loop that iterates through each string and counts the characters that are ==
// have a counter reset for each new value and add value for each character to new string 
// use if statment to check if length of new string is equal to length of original string, if equal then return OG String

function encodeStr(str) {
    var temp = ""
    for(let x = 0; x < str.length; x++ ){
        let count = 0

    }

}

/*****************************************************************************/

/* 
String Decode  
*/

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 * 
 * PSEUDO CODE
 * create a function that takes in a string
 * build for loop to iterate through set string 
 * create a temp var for the character to be pushed into new string
 * build a type check that checks whether the next character is an int 
 *  if it isnt an int then it would multipy character and push to temp var/new string
 * if it is an int then we check the next character
 * 
 */
function decodeStr(str) {}