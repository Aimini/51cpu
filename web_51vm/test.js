let vm = new _51cpu()
vm.ERAM = []
for(let i = 0; i < 0x10000; ++i)
    vm.ERAM.push(0)
vm.ERAM[0x0001] = 0x01
vm.ERAM[0x00F0] = 0x0A
vm.ERAM[0x0AAA] = 0xA0
vm.ERAM[0xFF01] = 0xFF
vm.IDATA.content = [0x75,0xE0,0x01,0x13,0x80,0xFD]