//Create a function that excepts a string parameter, and reverses each word in the string. All spaces in the string should be retained

/* 
PSEUDO CODE

Create a function that takes in a string of words, maps the location of each word.
Use split method to splits the words, then splits each letter while keeping the order
Then use reverse each word separately(can use reverse method) 
Then "join" back each separate letter in to words
Return words in order with letters of each word in reverse
*/

function reverseEveryWord(str) {
    // Split the input string into an array of words using the space as delimiter
    const words = str.split(" ");

    //Reverse each word and join them back with space
    const reversedWords = words.map(word => word.split("").reverse().join(""));

    return reversedWords.join(" ");
}

//Test Cases
const ogString = "Hello World";
const reversedString = reverseEveryWord(ogString);
console.log(reversedString); // Returns: "olleH dlroW"


/*
BETTER SOLUTIONS BY PEERS

#1
var reverseWords=s=>s.replace(/\S+/g,v=>[...v].reverse().join``)

#2
function reverseWords(str) {
  return str.split(' ').map(function(word){
    return word.split('').reverse().join('');
  }).join(' ');
}

*/