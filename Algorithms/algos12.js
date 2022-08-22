// Reverse Word Order
// Given a string of words (with spaces)
// return a new string with words in reverse sequence.
// */

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
function reverseWordOrder(wordsStr) {
    let revStr = []
    let split = wordsStr.split(' ')
    for (let v=split.length-1; v >=0; v--) {
        revStr.push(split[v])
        // revStr += split[v]
    } return revStr.join(' ')
}
console.log(reverseWordOrder(str3))