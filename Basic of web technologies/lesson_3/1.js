function queryTemperatureCel() {
    return parseInt(prompt("Введите температуру в градусах Цельсия: "));
}

function countTemperatureKel(temp_c) {
    let temp_k = Math.round((9 / 5 * temp_c + 32) * 100) / 100;
    return temp_k;
}
let temp_c = queryTemperatureCel()
let my_string = "Цельсий: " + temp_c + "; Фаренгейт: " + countTemperatureKel(temp_c)
alert(my_string);