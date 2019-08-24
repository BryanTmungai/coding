//let firstname = 'Peter';
//const pi = 3.14;
//ES5
//let age = prompt('how old are you');



function drive(event) {
    event.preventDefault();
    let age = document.getElementById('age').value;

    if (age == 18) {
        document.getElementById('log').innerHTML = 'you can drive a small car'
    } else if (age > 18 && age <= 24) {
        document.getElementById('log').innerHTML = 'you can drive a big car'
    } else if (age > 24) {
        document.getElementById('log').innerHTML = 'you can drive a truck'
    } else {
        document.getElementById('log').innerHTML = 'you are under age'
    }
}
drive(age);