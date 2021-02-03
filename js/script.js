var enviarform = document.querySelector("#enviarform")
enviarform.addEventListener("submit", submitDoForm)

async function submitDoForm(event) {
    event.preventDefault()
    let num1 = document.querySelector("#num1").value
    let num2 = document.querySelector("#num2").value
    let calculo = enviarform.calculo.value

    let formData = new FormData();
    formData.append("num1", num1);
    formData.append("num2", num2);
    formData.append("calculo", calculo);

    var dados = await fetch("/",
        {
            body: formData,
            method: "post"
        });
    var resultado = await dados.json()
    console.log(resultado)
    let campoResultado = document.querySelector("#resultadinho")
    campoResultado.style.display = "block"
    document.querySelector("#resultadoFinal").innerHTML = resultado.Resultado
}
