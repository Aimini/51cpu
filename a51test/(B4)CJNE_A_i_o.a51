LJMP STATE_255
STATE_0:
    MOV 0xF0,#0xFF
    CJNE A,#0,STATE_1
    LJMP FINAL

STATE_1:
    MOV 0xF0,#0x01
    CJNE A,#0x01,STATE_0

STATE_2:
    MOV 0xF0,#0x02
    CJNE A,#0x02,STATE_1

STATE_3:
    MOV 0xF0,#0x03
    CJNE A,#0x03,STATE_2

STATE_4:
    MOV 0xF0,#0x04
    CJNE A,#0x04,STATE_3

STATE_5:
    MOV 0xF0,#0x05
    CJNE A,#0x05,STATE_4

STATE_6:
    MOV 0xF0,#0x06
    CJNE A,#0x06,STATE_5

STATE_7:
    MOV 0xF0,#0x07
    CJNE A,#0x07,STATE_6

STATE_8:
    MOV 0xF0,#0x08
    CJNE A,#0x08,STATE_7

STATE_9:
    MOV 0xF0,#0x09
    CJNE A,#0x09,STATE_8

STATE_10:
    MOV 0xF0,#0x0A
    CJNE A,#0x0A,STATE_9

STATE_11:
    MOV 0xF0,#0x0B
    CJNE A,#0x0B,STATE_10

STATE_12:
    MOV 0xF0,#0x0C
    CJNE A,#0x0C,STATE_11

STATE_13:
    MOV 0xF0,#0x0D
    CJNE A,#0x0D,STATE_12

STATE_14:
    MOV 0xF0,#0x0E
    CJNE A,#0x0E,STATE_13

STATE_15:
    MOV 0xF0,#0x0F
    CJNE A,#0x0F,STATE_14

STATE_16:
    MOV 0xF0,#0x10
    CJNE A,#0x10,STATE_15

STATE_17:
    MOV 0xF0,#0x11
    CJNE A,#0x11,STATE_16

STATE_18:
    MOV 0xF0,#0x12
    CJNE A,#0x12,STATE_17

STATE_19:
    MOV 0xF0,#0x13
    CJNE A,#0x13,STATE_18

STATE_20:
    MOV 0xF0,#0x14
    CJNE A,#0x14,STATE_19

STATE_21:
    MOV 0xF0,#0x15
    CJNE A,#0x15,STATE_20

STATE_22:
    MOV 0xF0,#0x16
    CJNE A,#0x16,STATE_21

STATE_23:
    MOV 0xF0,#0x17
    CJNE A,#0x17,STATE_22

STATE_24:
    MOV 0xF0,#0x18
    CJNE A,#0x18,STATE_23

STATE_25:
    MOV 0xF0,#0x19
    CJNE A,#0x19,STATE_24

STATE_26:
    MOV 0xF0,#0x1A
    CJNE A,#0x1A,STATE_25

STATE_27:
    MOV 0xF0,#0x1B
    CJNE A,#0x1B,STATE_26

STATE_28:
    MOV 0xF0,#0x1C
    CJNE A,#0x1C,STATE_27

STATE_29:
    MOV 0xF0,#0x1D
    CJNE A,#0x1D,STATE_28

STATE_30:
    MOV 0xF0,#0x1E
    CJNE A,#0x1E,STATE_29

STATE_31:
    MOV 0xF0,#0x1F
    CJNE A,#0x1F,STATE_30

STATE_32:
    MOV 0xF0,#0x20
    CJNE A,#0x20,STATE_31

STATE_33:
    MOV 0xF0,#0x21
    CJNE A,#0x21,STATE_32

STATE_34:
    MOV 0xF0,#0x22
    CJNE A,#0x22,STATE_33

STATE_35:
    MOV 0xF0,#0x23
    CJNE A,#0x23,STATE_34

STATE_36:
    MOV 0xF0,#0x24
    CJNE A,#0x24,STATE_35

STATE_37:
    MOV 0xF0,#0x25
    CJNE A,#0x25,STATE_36

STATE_38:
    MOV 0xF0,#0x26
    CJNE A,#0x26,STATE_37

STATE_39:
    MOV 0xF0,#0x27
    CJNE A,#0x27,STATE_38

STATE_40:
    MOV 0xF0,#0x28
    CJNE A,#0x28,STATE_39

STATE_41:
    MOV 0xF0,#0x29
    CJNE A,#0x29,STATE_40

STATE_42:
    MOV 0xF0,#0x2A
    CJNE A,#0x2A,STATE_41

STATE_43:
    MOV 0xF0,#0x2B
    CJNE A,#0x2B,STATE_42

STATE_44:
    MOV 0xF0,#0x2C
    CJNE A,#0x2C,STATE_43

STATE_45:
    MOV 0xF0,#0x2D
    CJNE A,#0x2D,STATE_44

STATE_46:
    MOV 0xF0,#0x2E
    CJNE A,#0x2E,STATE_45

STATE_47:
    MOV 0xF0,#0x2F
    CJNE A,#0x2F,STATE_46

STATE_48:
    MOV 0xF0,#0x30
    CJNE A,#0x30,STATE_47

STATE_49:
    MOV 0xF0,#0x31
    CJNE A,#0x31,STATE_48

STATE_50:
    MOV 0xF0,#0x32
    CJNE A,#0x32,STATE_49

STATE_51:
    MOV 0xF0,#0x33
    CJNE A,#0x33,STATE_50

STATE_52:
    MOV 0xF0,#0x34
    CJNE A,#0x34,STATE_51

STATE_53:
    MOV 0xF0,#0x35
    CJNE A,#0x35,STATE_52

STATE_54:
    MOV 0xF0,#0x36
    CJNE A,#0x36,STATE_53

STATE_55:
    MOV 0xF0,#0x37
    CJNE A,#0x37,STATE_54

STATE_56:
    MOV 0xF0,#0x38
    CJNE A,#0x38,STATE_55

STATE_57:
    MOV 0xF0,#0x39
    CJNE A,#0x39,STATE_56

STATE_58:
    MOV 0xF0,#0x3A
    CJNE A,#0x3A,STATE_57

STATE_59:
    MOV 0xF0,#0x3B
    CJNE A,#0x3B,STATE_58

STATE_60:
    MOV 0xF0,#0x3C
    CJNE A,#0x3C,STATE_59

STATE_61:
    MOV 0xF0,#0x3D
    CJNE A,#0x3D,STATE_60

STATE_62:
    MOV 0xF0,#0x3E
    CJNE A,#0x3E,STATE_61

STATE_63:
    MOV 0xF0,#0x3F
    CJNE A,#0x3F,STATE_62

STATE_64:
    MOV 0xF0,#0x40
    CJNE A,#0x40,STATE_63

STATE_65:
    MOV 0xF0,#0x41
    CJNE A,#0x41,STATE_64

STATE_66:
    MOV 0xF0,#0x42
    CJNE A,#0x42,STATE_65

STATE_67:
    MOV 0xF0,#0x43
    CJNE A,#0x43,STATE_66

STATE_68:
    MOV 0xF0,#0x44
    CJNE A,#0x44,STATE_67

STATE_69:
    MOV 0xF0,#0x45
    CJNE A,#0x45,STATE_68

STATE_70:
    MOV 0xF0,#0x46
    CJNE A,#0x46,STATE_69

STATE_71:
    MOV 0xF0,#0x47
    CJNE A,#0x47,STATE_70

STATE_72:
    MOV 0xF0,#0x48
    CJNE A,#0x48,STATE_71

STATE_73:
    MOV 0xF0,#0x49
    CJNE A,#0x49,STATE_72

STATE_74:
    MOV 0xF0,#0x4A
    CJNE A,#0x4A,STATE_73

STATE_75:
    MOV 0xF0,#0x4B
    CJNE A,#0x4B,STATE_74

STATE_76:
    MOV 0xF0,#0x4C
    CJNE A,#0x4C,STATE_75

STATE_77:
    MOV 0xF0,#0x4D
    CJNE A,#0x4D,STATE_76

STATE_78:
    MOV 0xF0,#0x4E
    CJNE A,#0x4E,STATE_77

STATE_79:
    MOV 0xF0,#0x4F
    CJNE A,#0x4F,STATE_78

STATE_80:
    MOV 0xF0,#0x50
    CJNE A,#0x50,STATE_79

STATE_81:
    MOV 0xF0,#0x51
    CJNE A,#0x51,STATE_80

STATE_82:
    MOV 0xF0,#0x52
    CJNE A,#0x52,STATE_81

STATE_83:
    MOV 0xF0,#0x53
    CJNE A,#0x53,STATE_82

STATE_84:
    MOV 0xF0,#0x54
    CJNE A,#0x54,STATE_83

STATE_85:
    MOV 0xF0,#0x55
    CJNE A,#0x55,STATE_84

STATE_86:
    MOV 0xF0,#0x56
    CJNE A,#0x56,STATE_85

STATE_87:
    MOV 0xF0,#0x57
    CJNE A,#0x57,STATE_86

STATE_88:
    MOV 0xF0,#0x58
    CJNE A,#0x58,STATE_87

STATE_89:
    MOV 0xF0,#0x59
    CJNE A,#0x59,STATE_88

STATE_90:
    MOV 0xF0,#0x5A
    CJNE A,#0x5A,STATE_89

STATE_91:
    MOV 0xF0,#0x5B
    CJNE A,#0x5B,STATE_90

STATE_92:
    MOV 0xF0,#0x5C
    CJNE A,#0x5C,STATE_91

STATE_93:
    MOV 0xF0,#0x5D
    CJNE A,#0x5D,STATE_92

STATE_94:
    MOV 0xF0,#0x5E
    CJNE A,#0x5E,STATE_93

STATE_95:
    MOV 0xF0,#0x5F
    CJNE A,#0x5F,STATE_94

STATE_96:
    MOV 0xF0,#0x60
    CJNE A,#0x60,STATE_95

STATE_97:
    MOV 0xF0,#0x61
    CJNE A,#0x61,STATE_96

STATE_98:
    MOV 0xF0,#0x62
    CJNE A,#0x62,STATE_97

STATE_99:
    MOV 0xF0,#0x63
    CJNE A,#0x63,STATE_98

STATE_100:
    MOV 0xF0,#0x64
    CJNE A,#0x64,STATE_99

STATE_101:
    MOV 0xF0,#0x65
    CJNE A,#0x65,STATE_100

STATE_102:
    MOV 0xF0,#0x66
    CJNE A,#0x66,STATE_101

STATE_103:
    MOV 0xF0,#0x67
    CJNE A,#0x67,STATE_102

STATE_104:
    MOV 0xF0,#0x68
    CJNE A,#0x68,STATE_103

STATE_105:
    MOV 0xF0,#0x69
    CJNE A,#0x69,STATE_104

STATE_106:
    MOV 0xF0,#0x6A
    CJNE A,#0x6A,STATE_105

STATE_107:
    MOV 0xF0,#0x6B
    CJNE A,#0x6B,STATE_106

STATE_108:
    MOV 0xF0,#0x6C
    CJNE A,#0x6C,STATE_107

STATE_109:
    MOV 0xF0,#0x6D
    CJNE A,#0x6D,STATE_108

STATE_110:
    MOV 0xF0,#0x6E
    CJNE A,#0x6E,STATE_109

STATE_111:
    MOV 0xF0,#0x6F
    CJNE A,#0x6F,STATE_110

STATE_112:
    MOV 0xF0,#0x70
    CJNE A,#0x70,STATE_111

STATE_113:
    MOV 0xF0,#0x71
    CJNE A,#0x71,STATE_112

STATE_114:
    MOV 0xF0,#0x72
    CJNE A,#0x72,STATE_113

STATE_115:
    MOV 0xF0,#0x73
    CJNE A,#0x73,STATE_114

STATE_116:
    MOV 0xF0,#0x74
    CJNE A,#0x74,STATE_115

STATE_117:
    MOV 0xF0,#0x75
    CJNE A,#0x75,STATE_116

STATE_118:
    MOV 0xF0,#0x76
    CJNE A,#0x76,STATE_117

STATE_119:
    MOV 0xF0,#0x77
    CJNE A,#0x77,STATE_118

STATE_120:
    MOV 0xF0,#0x78
    CJNE A,#0x78,STATE_119

STATE_121:
    MOV 0xF0,#0x79
    CJNE A,#0x79,STATE_120

STATE_122:
    MOV 0xF0,#0x7A
    CJNE A,#0x7A,STATE_121

STATE_123:
    MOV 0xF0,#0x7B
    CJNE A,#0x7B,STATE_122

STATE_124:
    MOV 0xF0,#0x7C
    CJNE A,#0x7C,STATE_123

STATE_125:
    MOV 0xF0,#0x7D
    CJNE A,#0x7D,STATE_124

STATE_126:
    MOV 0xF0,#0x7E
    CJNE A,#0x7E,STATE_125

STATE_127:
    MOV 0xF0,#0x7F
    CJNE A,#0x7F,STATE_126

STATE_128:
    MOV 0xF0,#0x80
    CJNE A,#0x80,STATE_127

STATE_129:
    MOV 0xF0,#0x81
    CJNE A,#0x81,STATE_128

STATE_130:
    MOV 0xF0,#0x82
    CJNE A,#0x82,STATE_129

STATE_131:
    MOV 0xF0,#0x83
    CJNE A,#0x83,STATE_130

STATE_132:
    MOV 0xF0,#0x84
    CJNE A,#0x84,STATE_131

STATE_133:
    MOV 0xF0,#0x85
    CJNE A,#0x85,STATE_132

STATE_134:
    MOV 0xF0,#0x86
    CJNE A,#0x86,STATE_133

STATE_135:
    MOV 0xF0,#0x87
    CJNE A,#0x87,STATE_134

STATE_136:
    MOV 0xF0,#0x88
    CJNE A,#0x88,STATE_135

STATE_137:
    MOV 0xF0,#0x89
    CJNE A,#0x89,STATE_136

STATE_138:
    MOV 0xF0,#0x8A
    CJNE A,#0x8A,STATE_137

STATE_139:
    MOV 0xF0,#0x8B
    CJNE A,#0x8B,STATE_138

STATE_140:
    MOV 0xF0,#0x8C
    CJNE A,#0x8C,STATE_139

STATE_141:
    MOV 0xF0,#0x8D
    CJNE A,#0x8D,STATE_140

STATE_142:
    MOV 0xF0,#0x8E
    CJNE A,#0x8E,STATE_141

STATE_143:
    MOV 0xF0,#0x8F
    CJNE A,#0x8F,STATE_142

STATE_144:
    MOV 0xF0,#0x90
    CJNE A,#0x90,STATE_143

STATE_145:
    MOV 0xF0,#0x91
    CJNE A,#0x91,STATE_144

STATE_146:
    MOV 0xF0,#0x92
    CJNE A,#0x92,STATE_145

STATE_147:
    MOV 0xF0,#0x93
    CJNE A,#0x93,STATE_146

STATE_148:
    MOV 0xF0,#0x94
    CJNE A,#0x94,STATE_147

STATE_149:
    MOV 0xF0,#0x95
    CJNE A,#0x95,STATE_148

STATE_150:
    MOV 0xF0,#0x96
    CJNE A,#0x96,STATE_149

STATE_151:
    MOV 0xF0,#0x97
    CJNE A,#0x97,STATE_150

STATE_152:
    MOV 0xF0,#0x98
    CJNE A,#0x98,STATE_151

STATE_153:
    MOV 0xF0,#0x99
    CJNE A,#0x99,STATE_152

STATE_154:
    MOV 0xF0,#0x9A
    CJNE A,#0x9A,STATE_153

STATE_155:
    MOV 0xF0,#0x9B
    CJNE A,#0x9B,STATE_154

STATE_156:
    MOV 0xF0,#0x9C
    CJNE A,#0x9C,STATE_155

STATE_157:
    MOV 0xF0,#0x9D
    CJNE A,#0x9D,STATE_156

STATE_158:
    MOV 0xF0,#0x9E
    CJNE A,#0x9E,STATE_157

STATE_159:
    MOV 0xF0,#0x9F
    CJNE A,#0x9F,STATE_158

STATE_160:
    MOV 0xF0,#0xA0
    CJNE A,#0xA0,STATE_159

STATE_161:
    MOV 0xF0,#0xA1
    CJNE A,#0xA1,STATE_160

STATE_162:
    MOV 0xF0,#0xA2
    CJNE A,#0xA2,STATE_161

STATE_163:
    MOV 0xF0,#0xA3
    CJNE A,#0xA3,STATE_162

STATE_164:
    MOV 0xF0,#0xA4
    CJNE A,#0xA4,STATE_163

STATE_165:
    MOV 0xF0,#0xA5
    CJNE A,#0xA5,STATE_164

STATE_166:
    MOV 0xF0,#0xA6
    CJNE A,#0xA6,STATE_165

STATE_167:
    MOV 0xF0,#0xA7
    CJNE A,#0xA7,STATE_166

STATE_168:
    MOV 0xF0,#0xA8
    CJNE A,#0xA8,STATE_167

STATE_169:
    MOV 0xF0,#0xA9
    CJNE A,#0xA9,STATE_168

STATE_170:
    MOV 0xF0,#0xAA
    CJNE A,#0xAA,STATE_169

STATE_171:
    MOV 0xF0,#0xAB
    CJNE A,#0xAB,STATE_170

STATE_172:
    MOV 0xF0,#0xAC
    CJNE A,#0xAC,STATE_171

STATE_173:
    MOV 0xF0,#0xAD
    CJNE A,#0xAD,STATE_172

STATE_174:
    MOV 0xF0,#0xAE
    CJNE A,#0xAE,STATE_173

STATE_175:
    MOV 0xF0,#0xAF
    CJNE A,#0xAF,STATE_174

STATE_176:
    MOV 0xF0,#0xB0
    CJNE A,#0xB0,STATE_175

STATE_177:
    MOV 0xF0,#0xB1
    CJNE A,#0xB1,STATE_176

STATE_178:
    MOV 0xF0,#0xB2
    CJNE A,#0xB2,STATE_177

STATE_179:
    MOV 0xF0,#0xB3
    CJNE A,#0xB3,STATE_178

STATE_180:
    MOV 0xF0,#0xB4
    CJNE A,#0xB4,STATE_179

STATE_181:
    MOV 0xF0,#0xB5
    CJNE A,#0xB5,STATE_180

STATE_182:
    MOV 0xF0,#0xB6
    CJNE A,#0xB6,STATE_181

STATE_183:
    MOV 0xF0,#0xB7
    CJNE A,#0xB7,STATE_182

STATE_184:
    MOV 0xF0,#0xB8
    CJNE A,#0xB8,STATE_183

STATE_185:
    MOV 0xF0,#0xB9
    CJNE A,#0xB9,STATE_184

STATE_186:
    MOV 0xF0,#0xBA
    CJNE A,#0xBA,STATE_185

STATE_187:
    MOV 0xF0,#0xBB
    CJNE A,#0xBB,STATE_186

STATE_188:
    MOV 0xF0,#0xBC
    CJNE A,#0xBC,STATE_187

STATE_189:
    MOV 0xF0,#0xBD
    CJNE A,#0xBD,STATE_188

STATE_190:
    MOV 0xF0,#0xBE
    CJNE A,#0xBE,STATE_189

STATE_191:
    MOV 0xF0,#0xBF
    CJNE A,#0xBF,STATE_190

STATE_192:
    MOV 0xF0,#0xC0
    CJNE A,#0xC0,STATE_191

STATE_193:
    MOV 0xF0,#0xC1
    CJNE A,#0xC1,STATE_192

STATE_194:
    MOV 0xF0,#0xC2
    CJNE A,#0xC2,STATE_193

STATE_195:
    MOV 0xF0,#0xC3
    CJNE A,#0xC3,STATE_194

STATE_196:
    MOV 0xF0,#0xC4
    CJNE A,#0xC4,STATE_195

STATE_197:
    MOV 0xF0,#0xC5
    CJNE A,#0xC5,STATE_196

STATE_198:
    MOV 0xF0,#0xC6
    CJNE A,#0xC6,STATE_197

STATE_199:
    MOV 0xF0,#0xC7
    CJNE A,#0xC7,STATE_198

STATE_200:
    MOV 0xF0,#0xC8
    CJNE A,#0xC8,STATE_199

STATE_201:
    MOV 0xF0,#0xC9
    CJNE A,#0xC9,STATE_200

STATE_202:
    MOV 0xF0,#0xCA
    CJNE A,#0xCA,STATE_201

STATE_203:
    MOV 0xF0,#0xCB
    CJNE A,#0xCB,STATE_202

STATE_204:
    MOV 0xF0,#0xCC
    CJNE A,#0xCC,STATE_203

STATE_205:
    MOV 0xF0,#0xCD
    CJNE A,#0xCD,STATE_204

STATE_206:
    MOV 0xF0,#0xCE
    CJNE A,#0xCE,STATE_205

STATE_207:
    MOV 0xF0,#0xCF
    CJNE A,#0xCF,STATE_206

STATE_208:
    MOV 0xF0,#0xD0
    CJNE A,#0xD0,STATE_207

STATE_209:
    MOV 0xF0,#0xD1
    CJNE A,#0xD1,STATE_208

STATE_210:
    MOV 0xF0,#0xD2
    CJNE A,#0xD2,STATE_209

STATE_211:
    MOV 0xF0,#0xD3
    CJNE A,#0xD3,STATE_210

STATE_212:
    MOV 0xF0,#0xD4
    CJNE A,#0xD4,STATE_211

STATE_213:
    MOV 0xF0,#0xD5
    CJNE A,#0xD5,STATE_212

STATE_214:
    MOV 0xF0,#0xD6
    CJNE A,#0xD6,STATE_213

STATE_215:
    MOV 0xF0,#0xD7
    CJNE A,#0xD7,STATE_214

STATE_216:
    MOV 0xF0,#0xD8
    CJNE A,#0xD8,STATE_215

STATE_217:
    MOV 0xF0,#0xD9
    CJNE A,#0xD9,STATE_216

STATE_218:
    MOV 0xF0,#0xDA
    CJNE A,#0xDA,STATE_217

STATE_219:
    MOV 0xF0,#0xDB
    CJNE A,#0xDB,STATE_218

STATE_220:
    MOV 0xF0,#0xDC
    CJNE A,#0xDC,STATE_219

STATE_221:
    MOV 0xF0,#0xDD
    CJNE A,#0xDD,STATE_220

STATE_222:
    MOV 0xF0,#0xDE
    CJNE A,#0xDE,STATE_221

STATE_223:
    MOV 0xF0,#0xDF
    CJNE A,#0xDF,STATE_222

STATE_224:
    MOV 0xF0,#0xE0
    CJNE A,#0xE0,STATE_223

STATE_225:
    MOV 0xF0,#0xE1
    CJNE A,#0xE1,STATE_224

STATE_226:
    MOV 0xF0,#0xE2
    CJNE A,#0xE2,STATE_225

STATE_227:
    MOV 0xF0,#0xE3
    CJNE A,#0xE3,STATE_226

STATE_228:
    MOV 0xF0,#0xE4
    CJNE A,#0xE4,STATE_227

STATE_229:
    MOV 0xF0,#0xE5
    CJNE A,#0xE5,STATE_228

STATE_230:
    MOV 0xF0,#0xE6
    CJNE A,#0xE6,STATE_229

STATE_231:
    MOV 0xF0,#0xE7
    CJNE A,#0xE7,STATE_230

STATE_232:
    MOV 0xF0,#0xE8
    CJNE A,#0xE8,STATE_231

STATE_233:
    MOV 0xF0,#0xE9
    CJNE A,#0xE9,STATE_232

STATE_234:
    MOV 0xF0,#0xEA
    CJNE A,#0xEA,STATE_233

STATE_235:
    MOV 0xF0,#0xEB
    CJNE A,#0xEB,STATE_234

STATE_236:
    MOV 0xF0,#0xEC
    CJNE A,#0xEC,STATE_235

STATE_237:
    MOV 0xF0,#0xED
    CJNE A,#0xED,STATE_236

STATE_238:
    MOV 0xF0,#0xEE
    CJNE A,#0xEE,STATE_237

STATE_239:
    MOV 0xF0,#0xEF
    CJNE A,#0xEF,STATE_238

STATE_240:
    MOV 0xF0,#0xF0
    CJNE A,#0xF0,STATE_239

STATE_241:
    MOV 0xF0,#0xF1
    CJNE A,#0xF1,STATE_240

STATE_242:
    MOV 0xF0,#0xF2
    CJNE A,#0xF2,STATE_241

STATE_243:
    MOV 0xF0,#0xF3
    CJNE A,#0xF3,STATE_242

STATE_244:
    MOV 0xF0,#0xF4
    CJNE A,#0xF4,STATE_243

STATE_245:
    MOV 0xF0,#0xF5
    CJNE A,#0xF5,STATE_244

STATE_246:
    MOV 0xF0,#0xF6
    CJNE A,#0xF6,STATE_245

STATE_247:
    MOV 0xF0,#0xF7
    CJNE A,#0xF7,STATE_246

STATE_248:
    MOV 0xF0,#0xF8
    CJNE A,#0xF8,STATE_247

STATE_249:
    MOV 0xF0,#0xF9
    CJNE A,#0xF9,STATE_248

STATE_250:
    MOV 0xF0,#0xFA
    CJNE A,#0xFA,STATE_249

STATE_251:
    MOV 0xF0,#0xFB
    CJNE A,#0xFB,STATE_250

STATE_252:
    MOV 0xF0,#0xFC
    CJNE A,#0xFC,STATE_251

STATE_253:
    MOV 0xF0,#0xFD
    CJNE A,#0xFD,STATE_252

STATE_254:
    MOV 0xF0,#0xFE
    CJNE A,#0xFE,STATE_253

STATE_255:
    MOV 0xF0,#0xFF
    CJNE A,#0xFF,STATE_254
FINAL: MOV A,#0xFF