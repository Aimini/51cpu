var tables = document.querySelectorAll('table.kt tr')
var op_codes = []
function get_op_code(t) {
    var tds = t.querySelectorAll("td")
    if (tds.length === 0)
        return;
    let code_str = tds[0].innerText//binary encode
    let byte = tds[1].innerText
    let Mnemonic = tds[2].innerText
    let Oprands = tds[3].innerText
    op_codes.push([code_str, byte, Mnemonic, Oprands])
}

function print_opcode(t) {
    let text = ''
    t.forEach(function (v) {
        let [s0, s1, s2, s3] = v;
        s0 += ',   '
        s1 += ',   '
        s2 += ','
        while (s2.length < 10) {
            s2 += ' '
        }
        text += ('#' + s0 + s1 + s2 + s3 + '\n[],\n')
    })
    console.warn(text)
}


tables.forEach(get_op_code)
print_opcode(op_codes)


