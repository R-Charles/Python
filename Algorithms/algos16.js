/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 * 
 * create a function that takes in an array of int
 * create for loop that iterates through array and finds first non 0 value
 * if value is equal to zero then count the zeros and store them
 * if count is >= to 6, then reset count at next non zero value
 * else array is false
 */
function socialDistancingEnforcer(queue) {
    count = 0
    for (let v = 0; v < queue.length; v++) {
        if (queue[v] = 0) {
            count++;
        else {
            if (queue[v] != 0){
                count = 0;
            }
        }
        }       
    }
}
/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 * 
 * create a function that take in an array 
 * count number of indexes in array
 * if count is even(modulus), then array will return false(-1)
 * else use function midElement() to find middle
 * OR
 * create for loops to iterate from both ends of the array
 * create 2 variables to hold the sum of the added indexes as the loop iterates through the array
 * if var1 = var 2 then array = 2
 * then return the position of the middle
 */
function balanceIndex(nums) {}