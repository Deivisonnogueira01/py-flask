function getData(){

    const req = new XMLHttpRequest()
    req.open("GET", "http://127.0.0.1:5000/api?token=receba",false)
    req.send()
    req.console.error('server error');
    return req.responseText

}


function resultado(){
    
    const resultado = document.getElementById('resultado')
    let dados = getData()
    
    resultado.innerHTML = `<h2> ${dados}</h2>`
    
}