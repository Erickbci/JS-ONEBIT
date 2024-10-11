import calculate from "./calculate.js"
import switch_theme from "./theme.js"
import { input_update, clear_input, copy_result, keyboard_click} from "./clicks.js"
 
//  Atualizar input
document.querySelectorAll(".charKey").forEach(function (charKeyBtn) {
    charKeyBtn.addEventListener("click", input_update)
})

// Limpar input
document.getElementById("clear").addEventListener("click", clear_input)

// Binds teclado
input.addEventListener("keydown", keyboard_click)

document.getElementById("equal").addEventListener("click", calculate)

// BOTAO COPY CLICADO
document.getElementById("copyToClipboard").addEventListener("click", copy_result)

// THEME SWITCHER BOTAO TROCAR TEMA
document.getElementById("themeSwitcher").addEventListener("click", switch_theme)