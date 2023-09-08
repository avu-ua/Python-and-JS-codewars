// Cats and shelves
// https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/javascript

// Mariia
function solution(start, finish) 
{
  return ((finish - start)% 3) + ((finish - start) - (finish - start)% 3)/3
}


// ===============  Olesia ===============
function solution(start, finish) {
  const n = finish - start;
  return Math.floor(n / 3)  +  n % 3
}

<<<<<<< HEAD
console.log(solution(1, 5));
=======
// ===============  Slava ===============
function solution(start, finish) {
  return Math.floor((finish - start) / 3) + (finish - start) % 3
}
>>>>>>> 7adb6b2e12a1e455a791f4c48e6f8ba38eedc8c4
