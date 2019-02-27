//http://www.keil.com/support/man/docs/is51/is51_opcodes.htm
//get all <tr> that cantains opcodes
var tables = document.querySelectorAll('table.kt tr')
var op_codes = []

//get opcode form one <tr>
function get_op_code(t) {
    var tds = t.querySelectorAll("td")
    if (tds.length === 0)// maybe <th> (title row) in query result
        return; 
    let code_str = tds[0].innerText//binary encode
    let byte = tds[1].innerText//instruction length(bytes)
    let Mnemonic = tds[2].innerText//Assembly mnemonic
    let Oprands = tds[3].innerText//Oprands
    op_codes.push([code_str, byte, Mnemonic, Oprands])
}


function print_opcode(t) {
    let text = ''
    let bin_name = ''
    t.forEach(function (v) {
        let [s0, s1, s2, s3] = v;
        bin_name += (`0x${s0}:'${s2}',`) //add element to dict
        s0 += ',   '
        s1 += ',   '
        s2 += ','
        let space = ''
        while (s2.length + space.length < 10) {
            space += ' '
        }
       
        text += (`#${s0},   ${s1},   ${s2},${space}${s3}`+'\n[],\n')
    })
    console.warn(text)
    console.warn(`HEX_TO_BIN = {${bin_name}}`)
}


tables.forEach(get_op_code)
print_opcode(op_codes)


