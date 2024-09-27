var n1 = document.querySelector('#n1')
var n2 = document.querySelector('#n2')
var result = document.querySelector('span')

function Add () {
    result.innerHTML = parseInt(n1.value) + parseInt(n2.value)
}
        
function Subtract () {
    result.innerHTML = parseInt(n1.value) - parseInt(n2.value)
}

function Multiply () {
    result.innerHTML = parseInt(n1.value) * parseInt(n2.value)
}

function Division () {
    result.innerHTML = parseInt(n1.value) / parseInt(n2.value)
}
