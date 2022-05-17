
function fizzbuzz(numero) 
if (numero % 3 == 0 && numero % 5 == 0) {
  return "fizzbuzz";
}
else if (numero % 5 == 0) {
  return "buzz";
}
else if (numero % 3 == 0) {
  return "fizz";
}
  else {return numero;
}