var reset = document.querySelector('#b');
var s = document.querySelectorAll('td');

// Gather All box and clear
function clearBox(){
    for (var i=0; i<s.length; i++){
        s[i].innerHTML='';
    }
}

if(reset){
    reset.addEventListener('click', clearBox);
 }


//Click on the table of Square area

for (var i=0; i<s.length; i++) {

    s[i].addEventListener('click', function(){
        if (this.textContent === '') {
            this.textContent = 'X';
        }else if (this.textContent === 'X') {
            this.textContent = 'O';
        }else{
            this.textContent = '';
        }
    })
}

