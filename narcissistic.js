// A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
// In this Kata, we will restrict ourselves to decimal (base 10).

function narcissistic(value) {
  let digits = Array.from(String(value), Number);
  const sum = digits.reduce(
    (partialSum, a) => partialSum + a ** String(value).length,
    0
  );
  return sum === value;
}
