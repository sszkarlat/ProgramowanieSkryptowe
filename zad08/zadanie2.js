'use strict';

function sum(x, y) {
    return x + y;
}

function sum_strings(a) {
    let sum = 0;
    for (const value of a) {
        if (!isNaN(parseInt(value))) {
            sum += parseInt(value);
        }
    }
    return sum;
}

function digits(s) {
    let suma_liczb_nieparzystych = 0;
    let suma_liczb_parzystych = 0;

    for (const char of s) {
        const parsedValue = parseInt(char);
        if (!isNaN(parsedValue)) {
            if (parsedValue % 2 === 1) {
                suma_liczb_nieparzystych += parsedValue;
            } else {
                suma_liczb_parzystych += parsedValue;
            }
        }
    }

    return [suma_liczb_nieparzystych, suma_liczb_parzystych];
}

function letters(s) {
    let ilość_małych_liter = 0;
    let ilość_dużych_liter = 0;

    for (const char of s) {
        if (char >= 'a' && char <= 'z') {
            ilość_małych_liter += 1;
        } else if (char >= 'A' && char <= 'Z') {
            ilość_dużych_liter += 1;
        }
    }
    return [ilość_małych_liter, ilość_dużych_liter];
}
