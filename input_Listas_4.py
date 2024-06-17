from solucion_1 import Jugador, Equipo, Sede, Organizacion, merge_sort, promedio, todo
"""
CREACION DE DATOS
"""
jugador1 = Jugador(1, "Sofia García", 21, 66)
jugador2 = Jugador(2, "Alejandro Torres", 27, 24)
jugador3 = Jugador(3, "Valentina Rodriguez", 19, 15)
jugador4 = Jugador(4, "Juan López", 22, 78)
jugador5 = Jugador(5, "Martina Martinez", 30, 55)
jugador6 = Jugador(6, "Sebastián Pérez", 25, 42)
jugador7 = Jugador(7, "Camila Fernández", 24, 36)
jugador8 = Jugador(8, "Mateo González", 29, 89)
jugador9 = Jugador(9, "Isabella Díaz", 21, 92)
jugador10 = Jugador(10, "Daniel Ruiz", 17, 57)
jugador11 = Jugador(11, "Luciana Sánchez", 18, 89)
jugador12 = Jugador(12, "Lucas Vásquez", 26, 82)
jugador13 = Jugador(13, "Carlos Mendoza", 23, 73)
jugador14 = Jugador(14, "Ana Ramírez", 22, 68)
jugador15 = Jugador(15, "Ricardo Fernández", 28, 81)
jugador16 = Jugador(16, "Elena Morales", 24, 64)
jugador17 = Jugador(17, "Jorge García", 30, 56)
jugador18 = Jugador(18, "María López", 21, 79)
jugador19 = Jugador(19, "Luis Rodríguez", 27, 43)
jugador20 = Jugador(20, "Sofía González", 19, 54)
jugador21 = Jugador(21, "Pablo Martínez", 25, 76)
jugador22 = Jugador(22, "Lorena Torres", 20, 83)
jugador23 = Jugador(23, "Fernando Pérez", 26, 92)
jugador24 = Jugador(24, "Gabriela Fernández", 28, 49)
jugador25 = Jugador(25, "Emilio Vázquez", 23, 38)
jugador26 = Jugador(26, "Andrea Díaz", 22, 41)
jugador27 = Jugador(27, "Diego Sánchez", 21, 67)
jugador28 = Jugador(28, "Paula Mendoza", 20, 85)
jugador29 = Jugador(29, "Rodrigo Ramírez", 19, 59)
jugador30 = Jugador(30, "Natalia Fernández", 24, 73)
jugador31 = Jugador(31, "Alberto García", 27, 77)
jugador32 = Jugador(32, "Julia López", 22, 88)
jugador33 = Jugador(33, "Esteban Rodríguez", 23, 64)
jugador34 = Jugador(34, "Claudia González", 29, 71)
jugador35 = Jugador(35, "Julio Martínez", 26, 53)
jugador36 = Jugador(36, "Inés Torres", 25, 45)
jugador37 = Jugador(37, "Héctor Pérez", 28, 63)
jugador38 = Jugador(38, "Teresa Fernández", 30, 82)
jugador39 = Jugador(39, "Manuel Díaz", 21, 90)
jugador40 = Jugador(40, "Irene Sánchez", 22, 58)
jugador41 = Jugador(41, "José Mendoza", 19, 50)
jugador42 = Jugador(42, "Carmen Ramírez", 24, 72)
jugador43 = Jugador(43, "Pedro García", 27, 47)
jugador44 = Jugador(44, "Cristina López", 26, 36)
jugador45 = Jugador(45, "Miguel Rodríguez", 23, 79)
jugador46 = Jugador(46, "Marina González", 28, 91)
jugador47 = Jugador(47, "Antonio Martínez", 25, 52)
jugador48 = Jugador(48, "Sara Torres", 30, 68)
jugador49 = Jugador(49, "Javier Pérez", 21, 73)
jugador50 = Jugador(50, "Angela Fernández", 22, 86)
jugador51 = Jugador(51, "Raúl Díaz", 27, 45)
jugador52 = Jugador(52, "Eva Sánchez", 24, 60)
jugador53 = Jugador(53, "Victor Mendoza", 26, 78)
jugador54 = Jugador(54, "Patricia Ramírez", 19, 69)
jugador55 = Jugador(55, "David García", 23, 57)
jugador56 = Jugador(56, "Isabel López", 28, 80)
jugador57 = Jugador(57, "Gonzalo Rodríguez", 22, 66)
jugador58 = Jugador(58, "Clara González", 29, 55)
jugador59 = Jugador(59, "Martín Martínez", 21, 82)
jugador60 = Jugador(60, "Rosa Torres", 20, 62)
jugador61 = Jugador(61, "Lucas Pérez", 30, 90)
jugador62 = Jugador(62, "Diana Fernández", 27, 77)
jugador63 = Jugador(63, "Alejandro Díaz", 24, 71)
jugador64 = Jugador(64, "Beatriz Sánchez", 23, 44)
jugador65 = Jugador(65, "Marcos Mendoza", 22, 51)
jugador66 = Jugador(66, "Silvia Ramírez", 25, 88)
jugador67 = Jugador(67, "Joaquín García", 19, 67)
jugador68 = Jugador(68, "Nuria López", 26, 74)
jugador69 = Jugador(69, "Felipe Rodríguez", 30, 83)
jugador70 = Jugador(70, "Ana González", 21, 69)
jugador71 = Jugador(71, "Iván Martínez", 28, 61)
jugador72 = Jugador(72, "Olga Torres", 24, 47)
jugador73 = Jugador(73, "Rubén Pérez", 23, 54)
jugador74 = Jugador(74, "Alba Fernández", 19, 79)
jugador75 = Jugador(75, "Guillermo Díaz", 27, 85)
jugador76 = Jugador(76, "Victoria Sánchez", 22, 68)
jugador77 = Jugador(77, "Fabián Mendoza", 26, 91)
jugador78 = Jugador(78, "Alicia Ramírez", 21, 58)
jugador79 = Jugador(79, "Andrés García", 20, 53)
jugador80 = Jugador(80, "Celia López", 30, 66)
jugador81 = Jugador(81, "Adrián Rodríguez", 25, 72)
jugador82 = Jugador(82, "Natalia González", 28, 89)
jugador83 = Jugador(83, "Ernesto Martínez", 22, 77)
jugador84 = Jugador(84, "María Torres", 19, 49)
jugador85 = Jugador(85, "Gabriel Pérez", 27, 64)
jugador86 = Jugador(86, "Susana Fernández", 23, 87)
jugador87 = Jugador(87, "Enrique Díaz", 24, 71)
jugador88 = Jugador(88, "Carolina Sánchez", 26, 52)
jugador89 = Jugador(89, "Julian Mendoza", 30, 82)
jugador90 = Jugador(90, "Lucia Ramírez", 21, 60)
jugador91 = Jugador(91, "Ricardo García", 22, 74)
jugador92 = Jugador(92, "Lorena López", 25, 68)
jugador93 = Jugador(93, "Carlos Rodríguez", 27, 56)
jugador94 = Jugador(94, "Marta González", 29, 81)
jugador95 = Jugador(95, "Jorge Martínez", 23, 50)
jugador96 = Jugador(96, "Teresa Torres", 20, 77)
jugador97 = Jugador(97, "Roberto Pérez", 26, 63)
jugador98 = Jugador(98, "Daniela Fernández", 19, 91)
jugador99 = Jugador(99, "Mario Díaz", 24, 70)
jugador100 = Jugador(100, "Rita Sánchez", 21, 83)
jugador101 = Jugador(101, "Alberto Mendoza", 27, 68)
jugador102 = Jugador(102, "Elena Ramírez", 28, 45)
jugador103 = Jugador(103, "Francisco García", 25, 66)
jugador104 = Jugador(104, "Verónica López", 22, 81)
jugador105 = Jugador(105, "Hugo Rodríguez", 29, 53)
jugador106 = Jugador(106, "Esther González", 21, 78)
jugador107 = Jugador(107, "David Martínez", 24, 59)
jugador108 = Jugador(108, "Pilar Torres", 30, 85)
jugador109 = Jugador(109, "Oscar Pérez", 23, 71)
jugador110 = Jugador(110, "Lidia Fernández", 26, 88)
jugador111 = Jugador(111, "Vicente Díaz", 27, 60)
jugador112 = Jugador(112, "Cristina Sánchez", 19, 72)
jugador113 = Jugador(113, "Alfredo Mendoza", 22, 90)
jugador114 = Jugador(114, "Laura Ramírez", 28, 74)
jugador115 = Jugador(115, "Rafael García", 25, 69)
jugador116 = Jugador(116, "Isabel López", 21, 56)
jugador117 = Jugador(117, "Emilio Rodríguez", 26, 80)
jugador118 = Jugador(118, "Adriana González", 23, 89)
jugador119 = Jugador(119, "Raquel Martínez", 24, 75)
jugador120 = Jugador(120, "Miguel Torres", 30, 93)
jugador120 = Jugador(120, "Elena Ramos", 23, 52)
jugador121 = Jugador(121, "Fernando Blanco", 28, 61)
jugador122 = Jugador(122, "Gabriela Ortiz", 20, 74)
jugador123 = Jugador(123, "Javier Morales", 29, 87)
jugador124 = Jugador(124, "Andrea Ruiz", 22, 65)
jugador125 = Jugador(125, "Hugo Castro", 24, 79)
jugador126 = Jugador(126, "Paula Navarro", 19, 90)
jugador127 = Jugador(127, "Mario Vega", 30, 66)
jugador128 = Jugador(128, "Sara Ramos", 25, 53)
jugador129 = Jugador(129, "Carlos Ortiz", 26, 81)
jugador130 = Jugador(130, "Claudia Morales", 21, 48)
jugador131 = Jugador(131, "Luis Navarro", 27, 85)
jugador132 = Jugador(132, "Rocío Sánchez", 24, 78)
jugador133 = Jugador(133, "Alejandro Cruz", 22, 54)
jugador134 = Jugador(134, "Ana Herrera", 19, 91)
jugador135 = Jugador(135, "Miguel Castillo", 25, 65)
jugador136 = Jugador(136, "María Ríos", 30, 59)
jugador137 = Jugador(137, "Rubén Peña", 21, 72)
jugador138 = Jugador(138, "Lucía Hernández", 28, 83)
jugador139 = Jugador(139, "Fernando Vargas", 26, 48)
jugador140 = Jugador(140, "Elisa Ramírez", 23, 74)
jugador141 = Jugador(141, "Pablo García", 22, 63)
jugador142 = Jugador(142, "Isabel Castro", 27, 81)
jugador143 = Jugador(143, "Jorge González", 25, 52)
jugador144 = Jugador(144, "Natalia Pérez", 20, 67)
jugador145 = Jugador(145, "Ricardo Muñoz", 19, 89)
jugador146 = Jugador(146, "Alba López", 21, 77)
jugador147 = Jugador(147, "Víctor Torres", 30, 84)
jugador148 = Jugador(148, "Marta Ruiz", 23, 55)
jugador149 = Jugador(149, "Santiago Morales", 22, 61)
jugador150 = Jugador(150, "Ana Díaz", 27, 72)
jugador151 = Jugador(151, "Emilio Vargas", 26, 79)
jugador152 = Jugador(152, "Laura Ortiz", 24, 47)
jugador153 = Jugador(153, "Iván Ramírez", 20, 88)
jugador154 = Jugador(154, "Silvia Gómez", 28, 93)
jugador155 = Jugador(155, "Adrián Hernández", 19, 64)
jugador156 = Jugador(156, "Verónica Sánchez", 21, 56)
jugador157 = Jugador(157, "Oscar Pérez", 30, 76)
jugador158 = Jugador(158, "Carolina López", 25, 69)
jugador159 = Jugador(159, "Lucas Castillo", 22, 82)
jugador160 = Jugador(160, "Patricia Muñoz", 24, 51)
jugador161 = Jugador(161, "David García", 26, 73)
jugador162 = Jugador(162, "Cristina Ramos", 27, 54)
jugador163 = Jugador(163, "Roberto Vargas", 20, 90)
jugador164 = Jugador(164, "Carmen Herrera", 23, 62)
jugador165 = Jugador(165, "Enrique Ríos", 22, 71)
jugador166 = Jugador(166, "Lucía Peña", 25, 57)
jugador167 = Jugador(167, "Pedro Cruz", 28, 79)
jugador168 = Jugador(168, "Elena Martínez", 24, 67)
jugador169 = Jugador(169, "Gabriel Gómez", 30, 86)
jugador170 = Jugador(170, "Mónica Díaz", 19, 74)
jugador171 = Jugador(171, "Sergio Sánchez", 26, 59)
jugador172 = Jugador(172, "Claudia Ramírez", 21, 83)
jugador173 = Jugador(173, "Martín Navarro", 23, 52)
jugador174 = Jugador(174, "Laura Vargas", 27, 89)
jugador175 = Jugador(175, "Adriana Muñoz", 20, 65)
jugador176 = Jugador(176, "Raúl Herrera", 22, 77)
jugador177 = Jugador(177, "Sonia Ortiz", 25, 93)
jugador178 = Jugador(178, "Carlos Ramírez", 28, 72)
jugador179 = Jugador(179, "Sandra García", 21, 56)
jugador180 = Jugador(180, "Rubén López", 26, 84)
jugador181 = Jugador(181, "Isabel Ríos", 30, 67)
jugador182 = Jugador(182, "Fernando Hernández", 24, 48)
jugador183 = Jugador(183, "Ana Martínez", 19, 81)
jugador184 = Jugador(184, "Diego Pérez", 27, 53)
jugador185 = Jugador(185, "Marta Sánchez", 21, 76)
jugador186 = Jugador(186, "Hugo Ramírez", 22, 85)
jugador187 = Jugador(187, "Rosa Navarro", 25, 91)
jugador188 = Jugador(188, "Javier Herrera", 23, 63)
jugador189 = Jugador(189, "Clara Vargas", 28, 74)
jugador190 = Jugador(190, "Manuel Peña", 20, 55)
jugador191 = Jugador(191, "Gabriela Cruz", 26, 83)
jugador192 = Jugador(192, "José Díaz", 19, 66)
jugador193 = Jugador(193, "Patricia González", 24, 72)
jugador194 = Jugador(194, "Emilio Gómez", 21, 88)
jugador195 = Jugador(195, "Lorena Ramírez", 22, 50)
jugador196 = Jugador(196, "Sergio Ortiz", 30, 79)
jugador197 = Jugador(197, "Marta Sánchez", 25, 93)
jugador198 = Jugador(198, "Héctor Vargas", 27, 64)
jugador199 = Jugador(199, "Elena Ríos", 28, 82)
jugador200 = Jugador(200, "Luis Hernández", 23, 58)
jugador201 = Jugador(201, "Carmen López", 24, 71)
jugador202 = Jugador(202, "Raúl Ramírez", 22, 83)
jugador203 = Jugador(203, "Alba Gómez", 19, 60)
jugador204 = Jugador(204, "Adrián Martínez", 27, 92)
jugador205 = Jugador(205, "Beatriz Pérez", 30, 67)
jugador206 = Jugador(206, "Óscar Sánchez", 26, 73)
jugador207 = Jugador(207, "Lucía Navarro", 21, 47)
jugador208 = Jugador(208, "Ricardo Vargas", 24, 79)
jugador209 = Jugador(209, "Sonia Herrera", 22, 88)
jugador210 = Jugador(210, "Fernando Ríos", 25, 55)
jugador211 = Jugador(211, "Claudia Ramírez", 28, 63)
jugador212 = Jugador(212, "Luis García", 23, 81)
jugador213 = Jugador(213, "Patricia López", 26, 72)
jugador214 = Jugador(214, "Miguel Díaz", 30, 64)
jugador215 = Jugador(215, "Andrea Sánchez", 19, 74)
jugador216 = Jugador(216, "Iván Ramírez", 21, 91)
jugador217 = Jugador(217, "Ana González", 22, 60)
jugador218 = Jugador(218, "Jorge Navarro", 25, 89)
jugador219 = Jugador(219, "María Vargas", 28, 77)
jugador220 = Jugador(220, "Daniel Herrera", 24, 69)
jugador221 = Jugador(221, "Paula Ríos", 19, 54)
jugador222 = Jugador(222, "Roberto Peña", 26, 81)
jugador223 = Jugador(223, "Elena Cruz", 30, 73)
jugador224 = Jugador(224, "Alejandro Ortiz", 21, 65)
jugador225 = Jugador(225, "Lorena Ramírez", 27, 79)
jugador226 = Jugador(226, "Martín García", 22, 58)
jugador227 = Jugador(227, "Silvia López", 19, 88)
jugador228 = Jugador(228, "Pablo Vargas", 26, 67)
jugador229 = Jugador(229, "Cristina Sánchez", 28, 72)
jugador230 = Jugador(230, "Diego Ramírez", 25, 82)
jugador231 = Jugador(231, "Natalia Muñoz", 30, 49)
jugador232 = Jugador(232, "Rocío Hernández", 22, 90)
jugador233 = Jugador(233, "Lucas Ortiz", 21, 77)
jugador234 = Jugador(234, "Elena Ramírez", 27, 68)
jugador235 = Jugador(235, "Antonio Ríos", 26, 64)
jugador236 = Jugador(236, "Gabriela Vargas", 24, 85)
jugador237 = Jugador(237, "Ricardo Herrera", 28, 72)
jugador238 = Jugador(238, "Isabel Navarro", 22, 55)
jugador239 = Jugador(239, "María García", 19, 89)
jugador240 = Jugador(240, "Luis Ramírez", 24, 67)



e1 = Equipo("Futbol", [jugador1, jugador11, jugador21, jugador31, jugador41, jugador51])
e2 = Equipo("Volleyball", [jugador2, jugador12, jugador22, jugador32, jugador42])
e3 = Equipo("Basketball", [jugador3, jugador13, jugador23, jugador33, jugador43, jugador53])
e4 = Equipo("Futbol", [jugador4, jugador14, jugador24, jugador34, jugador44])
e5 = Equipo("Volleyball", [jugador5, jugador15, jugador25, jugador35, jugador45])
e6 = Equipo("Basketball", [jugador6, jugador16, jugador26, jugador36, jugador46, jugador56])
e7 = Equipo("Futbol", [jugador7, jugador17, jugador27, jugador37, jugador47])
e8 = Equipo("Volleyball", [jugador8, jugador18, jugador28, jugador38, jugador48, jugador58])
e9 = Equipo("Basketball", [jugador9, jugador19, jugador29, jugador39, jugador49])
e10 = Equipo("Tenis", [jugador10, jugador20, jugador30, jugador40, jugador50, jugador60])
e11 = Equipo("Natacion", [jugador61, jugador71, jugador81, jugador91, jugador101])
e12 = Equipo("Tenis", [jugador62, jugador72, jugador82, jugador92, jugador102])
e13 = Equipo("Natacion", [jugador63, jugador73, jugador83, jugador93, jugador103])
e14 = Equipo("Tenis", [jugador64, jugador74, jugador84, jugador94, jugador104])
e15 = Equipo("Natacion", [jugador65, jugador75, jugador85, jugador95, jugador105])
e16 = Equipo("Futbol", [jugador66, jugador76, jugador86, jugador96, jugador106])
e17 = Equipo("Volleyball", [jugador67, jugador77, jugador87, jugador97, jugador107])
e18 = Equipo("Basketball", [jugador68, jugador78, jugador88, jugador98, jugador108])
e19 = Equipo("Futbol", [jugador69, jugador79, jugador89, jugador99, jugador109])
e20 = Equipo("Volleyball", [jugador70, jugador80, jugador90, jugador100, jugador110])
e21 = Equipo("Basketball", [jugador111, jugador121, jugador131, jugador141, jugador151])
e22 = Equipo("Futbol", [jugador112, jugador122, jugador132, jugador142, jugador152])
e23 = Equipo("Volleyball", [jugador113, jugador123, jugador133, jugador143, jugador153])
e24 = Equipo("Basketball", [jugador114, jugador124, jugador134, jugador144, jugador154])
e25 = Equipo("Tenis", [jugador115, jugador125, jugador135, jugador145, jugador155])
e26 = Equipo("Natacion", [jugador116, jugador126, jugador136, jugador146, jugador156])
e27 = Equipo("Tenis", [jugador117, jugador127, jugador137, jugador147, jugador157])
e28 = Equipo("Natacion", [jugador118, jugador128, jugador138, jugador148, jugador158])
e29 = Equipo("Tenis", [jugador119, jugador129, jugador139, jugador149, jugador159])
e30 = Equipo("Natacion", [jugador120, jugador130, jugador140, jugador150, jugador160])

# Asignar los jugadores restantes para asegurar que todos tengan un equipo
e1.jugadores.extend([jugador161, jugador162, jugador163, jugador164, jugador165])
e2.jugadores.extend([jugador166, jugador167, jugador168, jugador169, jugador170])
e3.jugadores.extend([jugador171, jugador172, jugador173, jugador174, jugador175])
e4.jugadores.extend([jugador176, jugador177, jugador178, jugador179, jugador180])
e5.jugadores.extend([jugador181, jugador182, jugador183, jugador184, jugador185])
e6.jugadores.extend([jugador186, jugador187, jugador188, jugador189, jugador190])
e7.jugadores.extend([jugador191, jugador192, jugador193, jugador194, jugador195])
e8.jugadores.extend([jugador196, jugador197, jugador198, jugador199, jugador200])
e9.jugadores.extend([jugador201, jugador202, jugador203, jugador204, jugador205])
e10.jugadores.extend([jugador206, jugador207, jugador208, jugador209, jugador210])
e11.jugadores.extend([jugador211, jugador212, jugador213, jugador214, jugador215])
e12.jugadores.extend([jugador216, jugador217, jugador218, jugador219, jugador220])
e13.jugadores.extend([jugador221, jugador222, jugador223, jugador224, jugador225])
e14.jugadores.extend([jugador226, jugador227, jugador228, jugador229, jugador230])
e15.jugadores.extend([jugador231, jugador232, jugador233, jugador234, jugador235])
e16.jugadores.extend([jugador236, jugador237, jugador238, jugador239, jugador240])


s1 = Sede("Cali", [e1,e2,e3,e10,e11])
s2 = Sede("Medellin", [e7,e8,e9,e14,e15])
s3 = Sede("Bogota", [e4,e5,e6,e12,e13])
s4 = Sede("Palmira", [e16,e17,e18,e25,e26])
s5 = Sede("Buga", [e22,e23,e24,e29,e30])
s6 = Sede("Pereira", [e19,e20,e21,e27,e28])


colombia_sport = Organizacion("Colombia Sport", [s1, s2, s3])
todo(colombia_sport)