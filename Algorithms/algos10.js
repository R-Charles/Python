/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abc ABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 * 
 * PSEUDO
 * create a function that takes in a string 
 * Using the for loop to iterate through the string 
 *      to find any duplicate characters and remove them from the string
 * OR Create an entirely new string that excludes all repeating characters
 * returns the given string with any duplicate characters removed
 * .split() splits a string at the implied character W3Schools
 * 
 */
 function stringDedupe(str) {
    let arr = []
    let split = str.split('')
    for(var i = 0; i < split.length; i++){
        if (!arr.includes(split[i])){
            arr.push(split[i])
        }
    
    } return arr.join('')
}
console.log(stringDedupe(str4))

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 * 
 * PSEUDO CODE
 * create a function that takes in a string
 * use a for loop to iterate through the string
 *      recognizing where there is an empty space
 *      creating new substrings
 * then reversing each substring 
 * returning the given string with each word's letters in reverse
 */
function reverseWords(str) {
    let revStr = []
    let split = wordsStr.split(' ')
    for (let v=split.length-1; v >=0; v--) {
        revStr.push(split[v])
        // revStr += split[v]
    } return revStr.join(' ')
}
console.log(reverseWordOrder(str3))




/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

const str2 = "hello";
const expected2 = "hello";

const str3 = "   This  is a   test  ";
const expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 * 
 * PSEUDO CODE
 * create a function that takes in a string of words
 * create an empty string to hold the what the function returns
 * use a loop to iterate through the string to recognize the empty space
 * this will recognize the substrings
 * take the last string and make it the first, then the next one second etc
 * return a new string with words reversed in sequence
 */
function reverseWordOrder(wordsStr) {}