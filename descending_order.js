// # Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
// # Essentially, rearrange the digits to create the highest possible number.

function descendingOrder(n) {
  let numbers = Array.from(String(n), Number);
  numbers.sort(function (a, b) {
    return a - b;
  });
  return Number(numbers.reverse().join(""));
}
