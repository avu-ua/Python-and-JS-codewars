// Cats and shelves
// https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/javascript

// Mariia
function solution(start, finish) 
{
  return ((finish - start)% 3) + ((finish - start) - (finish - start)% 3)/3
}


// ===============  Olesia ===============
def solution(start, finish):{
    n = finish - start;
    return Math.floor(n / 3)  + n % 3
}

// ===============  Slava ===============
function solution(start, finish) {
  return Math.floor((finish - start) / 3) + (finish - start) % 3
}