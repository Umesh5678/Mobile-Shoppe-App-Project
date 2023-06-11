function myFunction() {
    alert("Hello from a static file!");
  }


// let increase;
// let decrease;
// let prize1st;
// let prize2nd;
// let total = increase * prize1st + decrease * prize2nd;
// console.log(total)



  function increaseCount(a, b) {
    var input = b.previousElementSibling;
    var value = parseInt(input.value, 10); 
    value = isNaN(value)? 0 : value;
     temp = value ++;
    input.value = value;
    var theValue = document.getElementById("prize").innerHTML;
    console.log(theValue)
    
    var total = theValue * temp+1
    document.getElementById('amount').innerHTML = total;
    document.getElementById('total').innerHTML = total;
    
    }
    function decreaseCount(a, b) {
    var input = b.nextElementSibling;
    var value = parseInt(input.value, 10); 
    if (value > 0) {
    value = isNaN(value)? 0 : value;
    temp = value --;
    input.value = value;
    var theValue = document.getElementById("prize").innerHTML;
    var total = theValue * temp
    document.getElementById('amount').innerHTML = total;
    document.getElementById('total').innerHTML = total;
    
    }
    }




