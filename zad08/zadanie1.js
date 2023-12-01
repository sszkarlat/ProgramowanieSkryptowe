function funkcja_zwrotna() {
    const value1 = document.forms.MyForm.pole_tekstowe.value;
    const value2 = document.forms.MyForm.pole_liczbowe.value;
    console.log(value1, ":", typeof value1);
    console.log(value2, ":", typeof value2);
}

function load_value() {
    var load_value = window.prompt();
    console.log(load_value, ":", typeof load_value);
}
for (let i = 0; i < 4; i++) {
    // load_value()
}