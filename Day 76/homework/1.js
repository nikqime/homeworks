
function number9(n){
    let count = 0;
       let factor = 1;
   
       while (factor <= n) {
           let lowerNumbers = n - Math.floor(n / factor) * factor;
           let currentDigit = Math.floor(n / factor) % 10;
           let higherNumbers = Math.floor(n / (factor * 10));
   
           count += higherNumbers * factor;
   
           if (currentDigit > 9) {
               count += factor;
           } else if (currentDigit == 9) {
               count += lowerNumbers + 1;
           }
   
           factor *= 10; 
       }
   
       return count;
   }