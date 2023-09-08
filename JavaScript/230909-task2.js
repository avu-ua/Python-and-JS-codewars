// Cats and shelves
// https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/javascript

// Mariia
function solution(start, finish) 
{
  return ((finish - start)% 3) + ((finish - start) - (finish - start)% 3)/3
}