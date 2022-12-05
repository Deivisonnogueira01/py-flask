const ladoA = document.getElementById('ladoA');
const ladoB = document.getElementById('ladoB');
const ladoC = document.getElementById('ladoC');

const area = document.getElementById('area');

const maiorLado = document.getElementById('maiorLado');
const perimetro = document.getElementById('perimetro');

const picoDoTriangulo = document.getElementById('pico');

picoDoTriangulo.style.borderLeftWidth = `${ladoA.value}px` 
picoDoTriangulo.style.borderRightWidth = `${ladoB.value}px`
picoDoTriangulo.style.borderBottomWidth = `${ladoC.value}px`

function alterarBorda(e){
    picoDoTriangulo.style.borderLeftWidth = `${ladoA.value}px` 
    picoDoTriangulo.style.borderRightWidth = `${ladoB.value}px`
    picoDoTriangulo.style.borderBottomWidth = `${ladoC.value}px`
}
function ladoMaior(){
    maiorLado.style.visibility = 'visible'
    perimetro.style.visibility = 'hidden'
    area.style.visibility = 'hidden'
}
function perimetroResult(){
    perimetro.style.visibility = 'visible'
    maiorLado.style.visibility = 'hidden'
    area.style.visibility = 'hidden'
}

function areaResult(){
    area.style.visibility = 'visible'
    maiorLado.style.visibility = 'hidden'
    perimetro.style.visibility = 'hidden'
}
function submeterInfo(e){
    e.preventDefault()
    return false
}