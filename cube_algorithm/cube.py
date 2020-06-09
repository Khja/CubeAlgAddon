# MIT License
# Copyright (c) 2020 Khja
# Please read before using this piece of software.


css = """\
.card {
 font-family: arial;
 font-size: 30px;
 text-align: center;
 color: black;
 background-color: white;
}

:root {
 --thickness: 4;
 --size: 20;
 --G: #39EA5C;
 --W: #FFFFFF;
 --R: #DC0010;
 --O: #FF9E00;
 --Y: #FFFF00;
 --B: #0027D7;
}
\
"""

n_back = '''{{FrontSide}}

                <hr id=answer>

                <b>{{Case}}</b>
                <br><br>
                <i>{{Algorithm}}</i>
                '''


_front = """<br>
<canvas id="cube" width=150 height=150></canvas>
<br>
<br>

<script>
    //Colors. You may change the RGB codes, don't touch the names
    var colors = {
            G: getComputedStyle(document.documentElement).getPropertyValue('--G'),
            W: getComputedStyle(document.documentElement).getPropertyValue('--W'),
            R: getComputedStyle(document.documentElement).getPropertyValue('--R'),
            O: getComputedStyle(document.documentElement).getPropertyValue('--O'),
            Y: getComputedStyle(document.documentElement).getPropertyValue('--Y'),
            B: getComputedStyle(document.documentElement).getPropertyValue('--B')
        };

    var border = getComputedStyle(document.documentElement).getPropertyValue('--Border')

    //Size of the cube
    var size = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--size'))

    //Thickness of the border
    var thickness = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--thickness'))

//*****DON'T TOUCH FURTHER!!!!*****//

    //Faces
    var F = Array(9).fill("G"),
        U = Array(9).fill("W"),
        R = Array(9).fill("R"),
        B = Array(9).fill("B")
        D = Array(9).fill("Y"),
        L = Array(9).fill("O"),
        cube = [U,F,R,D,B,L];

    function Random(max) {
        return Math.round(Math.random() * (max-1));
    }


    /*Rotation functions*/

    //Rotate_s the face colors clockwise. Center stays in center
    function Rotate_Face_1(face) {
        var top = Array()

        top.push(face[6])
        top.push(face[3])
        top.push(face[0])
        top.push(face[7])
        top.push(face[4])
        top.push(face[1])
        top.push(face[8])
        top.push(face[5])
        top.push(face[2])

        return top
    }

    //Rotate_s the face colors counterclockwise. Center stays in center
    function Rotate_Face_2(face) {
        return Rotate_Face_1(Rotate_Face_1(Rotate_Face_1(face)))
    }

    //Rotate_s all objects in the Arrays clockwise
    function Rotate_Layer(U,F,L,B,R) {
        var u = Rotate_Face_1(U)
        var f = Array()
        var l = Array()
        var b = Array()
        var r = Array()

        //Rotate_s the lateral objects
        f.push(R[0])
        f.push(R[1])
        f.push(R[2])
        f.push(F[3])
        f.push(F[4])
        f.push(F[5])
        f.push(F[6])
        f.push(F[7])
        f.push(F[8])

        l.push(F[0])
        l.push(F[1])
        l.push(F[2])
        l.push(L[3])
        l.push(L[4])
        l.push(L[5])
        l.push(L[6])
        l.push(L[7])
        l.push(L[8])

        b.push(L[0])
        b.push(L[1])
        b.push(L[2])
        b.push(B[3])
        b.push(B[4])
        b.push(B[5])
        b.push(B[6])
        b.push(B[7])
        b.push(B[8])

        r.push(B[0])
        r.push(B[1])
        r.push(B[2])
        r.push(R[3])
        r.push(R[4])
        r.push(R[5])
        r.push(R[6])
        r.push(R[7])
        r.push(R[8])

        return [u, f, l, b, r]
    }


    /*Moves*/
    //Rotations
    function Rotate_X() {
        var u = cube[0], f = cube[1], r = cube[2], d = cube[3], b = cube[4], l = cube[5]
        cube[0] = f
        cube[1] = d
        cube[2] = Rotate_Face_1(r)
        cube[3] = Rotate_Face_1(Rotate_Face_1(b))
        cube[4] = Rotate_Face_1(Rotate_Face_1(u))
        cube[5] = Rotate_Face_2(l)
    }
    function Rotate_Xi() {Rotate_X(); Rotate_X(); Rotate_X()};


    function Rotate_Y() {Rotate_Yi(); Rotate_Yi(); Rotate_Yi()};
    function Rotate_Yi() {
        var u = cube[0], f = cube[1], r = cube[2], d = cube[3], b = cube[4], l = cube[5]
        cube[0] = Rotate_Face_2(u)
        cube[1] = l
        cube[2] = f
        cube[3] = Rotate_Face_1(d)
        cube[4] = r
        cube[5] = b
    }


    function Rotate_Zi() {Rotate_Yi(); Rotate_Xi(); Rotate_Y()};
    function Rotate_Z() {Rotate_Zi(); Rotate_Zi(); Rotate_Zi()};



    //Layers
    function Rotate_U() {
        var all = Rotate_Layer(cube[0],cube[1],cube[5],cube[4],cube[2])

        cube[0] = all[0]
        cube[1] = all[1]
        cube[5] = all[2]
        cube[4] = all[3]
        cube[2] = all[4]
    }
    function Rotate_Ui() {Rotate_U(); Rotate_U(); Rotate_U()};

    function Rotate_F() {Rotate_X(); Rotate_U(); Rotate_Xi()};
    function Rotate_Fi() {Rotate_X(); Rotate_Ui(); Rotate_Xi()};

    function Rotate_R() {Rotate_Zi(); Rotate_U(); Rotate_Z()};
    function Rotate_Ri() {Rotate_R(); Rotate_R(); Rotate_R()};

    function Rotate_D() {Rotate_X(); Rotate_X(); Rotate_U(); Rotate_X(); Rotate_X()};
    function Rotate_Di() {Rotate_D(); Rotate_D(); Rotate_D()};

    function Rotate_B() {Rotate_Xi(); Rotate_U(); Rotate_X()};
    function Rotate_Bi() {Rotate_Xi(); Rotate_Ui(); Rotate_X()};

    function Rotate_L() {Rotate_Z(); Rotate_U(); Rotate_Zi()};
    function Rotate_Li() {Rotate_Z(); Rotate_Ui(); Rotate_Zi()};


    function Rotate_M() {Rotate_X(); Rotate_Ri(); Rotate_L()};
    function Rotate_Mi() {Rotate_Xi(); Rotate_R(); Rotate_Li()};

    function Rotate_r() {Rotate_L(); Rotate_X()}
    function Rotate_ri() {Rotate_Li(); Rotate_Xi()}

    function Rotate_l() {Rotate_R(); Rotate_X()}
    function Rotate_li() {Rotate_Ri(); Rotate_Xi()}

    function Rotate_u() {Rotate_Di(); Rotate_Yi()}
    function Rotate_ui() {Rotate_D(); Rotate_Y()}

    function Rotate_b() {Rotate_Fi(); Rotate_Z()}
    function Rotate_bi() {Rotate_F(); Rotate_Zi()}

    function Rotate_d() {Rotate_Ui(); Rotate_Y()}
    function Rotate_di() {Rotate_U(); Rotate_Yi()}

    function Rotate_f() {Rotate_B(); Rotate_Z()}
    function Rotate_fi() {Rotate_Bi(); Rotate_Zi()}



    /*Drawing functions*/
    function rect(ctx,l,x,y,a,b,color) {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.moveTo(x*l, y*l);
        ctx.lineTo(x*l, y*l+a*l);
        ctx.lineTo(x*l+b*l, y*l+a*l);
        ctx.lineTo(x*l+b*l, y*l);
        ctx.lineTo(x*l, y*l);
        ctx.fill();
        ctx.stroke();
    }

    function Display(cube) {
        var u = cube[0],
            f = cube[1],
            r = cube[2],
            b = cube[4],
            l = cube[5];

        var canvas = document.getElementById('cube');
            if (canvas.getContext) {
                var ctx = canvas.getContext('2d');
                ctx.canvas.width = 8 * size
                ctx.canvas.height = 8 * size

                ctx.strokeStyle = border;
                ctx.lineWidth = thickness;

                //U Face
                rect(ctx, size, 1, 5, 2, 2, colors[u[6]])
                rect(ctx, size, 3, 5, 2, 2, colors[u[7]])
                rect(ctx, size, 5, 5, 2, 2, colors[u[8]])

                rect(ctx, size, 1, 3, 2, 2, colors[u[3]])
                rect(ctx, size, 3, 3, 2, 2, colors[u[4]])
                rect(ctx, size, 5, 3, 2, 2, colors[u[5]])

                rect(ctx, size, 1, 1, 2, 2, colors[u[0]])
                rect(ctx, size, 3, 1, 2, 2, colors[u[1]])
                rect(ctx, size, 5, 1, 2, 2, colors[u[2]])

                //F Face
                rect(ctx, size, 1, 7, 1, 2, colors[f[0]])
                rect(ctx, size, 3, 7, 1, 2, colors[f[1]])
                rect(ctx, size, 5, 7, 1, 2, colors[f[2]])

/*                 //B Face
                rect(ctx, size, 1, -1, colors[b[2]])
                rect(ctx, size, 3, -1, colors[b[1]])
                rect(ctx, size, 5, -1, colors[b[0]]) */

                //R Face
                rect(ctx, size, 7, 1, 2, 1, colors[r[2]])
                rect(ctx, size, 7, 3, 2, 1, colors[r[1]])
                rect(ctx, size, 7, 5, 2, 1, colors[r[0]])

                //L Face
                rect(ctx, size, 0, 1, 2, 1, colors[l[0]])
                rect(ctx, size, 0, 3, 2, 1, colors[l[1]])
                rect(ctx, size, 0, 5, 2, 1, colors[l[2]])
            }
    }

    function Reverse(alg) {
        var reverse = Array()
        var alg = alg.reverse()

        for (i = 0; i < alg.length; i++) {
            //x
            if (alg[i] == "x") {reverse.push("x'")}
            if (alg[i] == "x'") {reverse.push("x")}
            if (alg[i] == "x2" || alg[i] == "x2'") {reverse.push("x2")}

            //y
            if (alg[i] == "y") {reverse.push("y'")}
            if (alg[i] == "y'") {reverse.push("y")}
            if (alg[i] == "y2" || alg[i] == "y2'") {reverse.push("y2")}

            //z
            if (alg[i] == "z") {reverse.push("z'")}
            if (alg[i] == "z'") {reverse.push("z")}
            if (alg[i] == "z2" || alg[i] == "z2'") {reverse.push("z2")}

            //U
            if (alg[i] == "U") {reverse.push("U'")}
            if (alg[i] == "U'") {reverse.push("U")}
            if (alg[i] == "U2" || alg[i] == "U2'") {reverse.push("U2")}

            //F
            if (alg[i] == "F") {reverse.push("F'")}
            if (alg[i] == "F'") {reverse.push("F")}
            if (alg[i] == "F2" || alg[i] == "F2'") {reverse.push("F2")}

            //R
            if (alg[i] == "R") {reverse.push("R'")}
            if (alg[i] == "R'") {reverse.push("R")}
            if (alg[i] == "R2" || alg[i] == "R2'") {reverse.push("R2")}

            //D
            if (alg[i] == "D") {reverse.push("D'")}
            if (alg[i] == "D'") {reverse.push("D")}
            if (alg[i] == "D2" || alg[i] == "D2'") {reverse.push("D2")}

            //B
            if (alg[i] == "B") {reverse.push("B'")}
            if (alg[i] == "B'") {reverse.push("B")}
            if (alg[i] == "B2" || alg[i] == "B2'") {reverse.push("B2")}

            //L
            if (alg[i] == "L") {reverse.push("L'")}
            if (alg[i] == "L'") {reverse.push("L")}
            if (alg[i] == "L2" || alg[i] == "L2'") {reverse.push("L2")}

            //M
            if (alg[i] == "M") {reverse.push("M'")}
            if (alg[i] == "M'") {reverse.push("M")}
            if (alg[i] == "M2" || alg[i] == "M2'") {reverse.push("M2")}

            //u
            if (alg[i] == "u") {reverse.push("u'")}
            if (alg[i] == "u'") {reverse.push("u")}
            if (alg[i] == "u2" || alg[i] == "u2'") {reverse.push("u2")}

            //f
            if (alg[i] == "f") {reverse.push("f'")}
            if (alg[i] == "f'") {reverse.push("f")}
            if (alg[i] == "f2" || alg[i] == "f2'") {reverse.push("f2")}

            //r
            if (alg[i] == "r") {reverse.push("r'")}
            if (alg[i] == "r'") {reverse.push("r")}
            if (alg[i] == "r2" || alg[i] == "r2'") {reverse.push("r2")}

            //d
            if (alg[i] == "d") {reverse.push("d'")}
            if (alg[i] == "d'") {reverse.push("d")}
            if (alg[i] == "d2" || alg[i] == "d2'") {reverse.push("d2")}

            //b
            if (alg[i] == "b") {reverse.push("b'")}
            if (alg[i] == "b'") {reverse.push("b")}
            if (alg[i] == "b2" || alg[i] == "b2'") {reverse.push("b2")}

            //l
            if (alg[i] == "l") {reverse.push("l'")}
            if (alg[i] == "l'") {reverse.push("l")}
            if (alg[i] == "l2" || alg[i] == "l2'") {reverse.push("l2")}
        }

        return reverse
    }

    function Perform(alg) {
        for (i = 0; i < alg.length; i++) {
            //x
            if (alg[i] == "x") {Rotate_X()}
            if (alg[i] == "x'") {Rotate_Xi()}
            if (alg[i] == "x2" || alg[i] == "x2'") {Rotate_X(); Rotate_X()}

            //y
            if (alg[i] == "y") {Rotate_Y()}
            if (alg[i] == "y'") {Rotate_Yi()}
            if (alg[i] == "y2" || alg[i] == "y2'") {Rotate_Y(); Rotate_Y();}

            //z
            if (alg[i] == "z") {Rotate_Z()}
            if (alg[i] == "z'") {Rotate_Zi()}
            if (alg[i] == "z2" || alg[i] == "z2'") {Rotate_Z(); Rotate_Z();}

            //U
            if (alg[i] == "U") {Rotate_U()}
            if (alg[i] == "U'") {Rotate_Ui()}
            if (alg[i] == "U2" || alg[i] == "U2'") {Rotate_U(); Rotate_U()}

            //F
            if (alg[i] == "F") {Rotate_F()}
            if (alg[i] == "F'") {Rotate_Fi()}
            if (alg[i] == "F2" || alg[i] == "F2'") {Rotate_F(); Rotate_F()}

            //R
            if (alg[i] == "R") {Rotate_R()}
            if (alg[i] == "R'") {Rotate_Ri()}
            if (alg[i] == "R2" || alg[i] == "R2'") {Rotate_R();Rotate_R();}

            //D
            if (alg[i] == "D") {Rotate_D();}
            if (alg[i] == "D'") {Rotate_Di();}
            if (alg[i] == "D2" || alg[i] == "D2'") {Rotate_D(); Rotate_D()}

            //B
            if (alg[i] == "B") {Rotate_B()}
            if (alg[i] == "B'") {Rotate_Bi()}
            if (alg[i] == "B2" || alg[i] == "B2'") {Rotate_B(); Rotate_B()}

            //L
            if (alg[i] == "L") {Rotate_L()}
            if (alg[i] == "L'") {Rotate_Li()}
            if (alg[i] == "L2" || alg[i] == "L2'") {Rotate_L(); Rotate_L()}

            //M
            if (alg[i] == "M") {Rotate_M()}
            if (alg[i] == "M'") {Rotate_Mi()}
            if (alg[i] == "M2" || alg[i] == "M2'") {Rotate_M(); Rotate_M()}

            //u
            if (alg[i] == "u") { Rotate_u()}
            if (alg[i] == "u'") {Rotate_ui()}
            if (alg[i] == "u2" || alg[i] == "u2'") {Rotate_u(); Rotate_u()}

            //f
            if (alg[i] == "f") {Rotate_f()}
            if (alg[i] == "f'") {Rotate_fi()}
            if (alg[i] == "f2" || alg[i] == "f2'") {Rotate_f(); Rotate_f()}

            //r
            if (alg[i] == "r") {Rotate_r()}
            if (alg[i] == "r'") {Rotate_ri()}
            if (alg[i] == "r2" || alg[i] == "r2'") {Rotate_r(); Rotate_r()}

            //d
            if (alg[i] == "d") {Rotate_d()}
            if (alg[i] == "d'") {Rotate_di()}
            if (alg[i] == "d2" || alg[i] == "d2'") {Rotate_d(); Rotate_d()}

            //b
            if (alg[i] == "b") {Rotate_b()}
            if (alg[i] == "b'") {Rotate_bi()}
            if (alg[i] == "b2" || alg[i] == "b2'") {Rotate_b(); Rotate_b()}

            //l
            if (alg[i] == "l") {Rotate_R(); Rotate_Xi()}
            if (alg[i] == "l'") {Rotate_li()}
            if (alg[i] == "l2" || alg[i] == "l2'") {Rotate_l(); Rotate_l()}

        }
    }

    var neutrality = "{{Neutrality}}".trim().split(' // ');

    function getNeutral(neutrality) {
        var colors = Array();

        for (i = 0; i < neutrality.length; i ++) {
            color = neutrality[i];
            for (k = 0; k < 10; k ++) {
                if (color == "W") {colors.push("")};
                if (color == "Y") {colors.push("x2")};
                if (color == "G") {colors.push("x")};
                if (color == "B") {colors.push("x'")};
                if (color == "R") {colors.push("z'")};
                if (color == "O") {colors.push("z")};
            }
        }
        return colors
    }

    function Scramble(moves,number) {
        var scramble = Array();
        var i = 0;

        while (i < number) {
            var k = Random(moves.length)
            var move = moves[k]

            if (move.length > 2) {
                move = move.split(' ')
            }
            else {
                move = [move]
            }

            Perform(move)
            i ++
        }
    }

    function getAlg(alg,s) {
        alg = alg.replace(/\(/g, "")
        alg = alg.replace(/\)/g, "")
        return alg.trim().split(s)
    }

    var moves = getAlg("{{Algorithm}}",' ');

    var scramble_size = {{ScrambleSize}};
    var scramble = getAlg("{{Scramble}}"," // ");

    var aufmoves = ["U","U'","U2"];

    var reverse = Reverse(moves);

    //Apply algorithm and scramble and AUF
    var ufaces = getNeutral(neutrality)
    Perform([ufaces[Random(ufaces.length)]])
    Scramble(['y','y2'],6)
    Scramble(scramble,scramble_size);
    Perform(reverse);
    Perform([aufmoves[0]])

    //Draw Cube
    Display(cube);
</script>
"""



u_back = '''\
{{FrontSide}}

<hr id=answer>

<b>{{Case}}</b>
<br><br>
<i><div id='alg'></div></i>

<script>
    if ("{{U Algorithm}}".length > 0) {
        document.getElementById('alg').innerHTML = "{{U Algorithm}}"
    }
    else {
        document.getElementById('alg').innerHTML = "(U) "+"{{Algorithm}}"
    }
</script>
\
'''

n_front = _front.replace("Perform([aufmoves[0]])","")
n_back = '''\
{{FrontSide}}

<hr id=answer>

<b>{{Case}}</b>
<br><br>
<i>{{Algorithm}}</i>
\
'''

u_front = "{{#U}}"+_front+"{{/U}}"
ui_front = "{{#U'}}"+_front.replace("[aufmoves[0]]","[aufmoves[1]]")+"{{/U'}}"
ui_back = u_back.replace("U Algorithm","U' Algorithm")
ui_back = ui_back.replace('"(U) "+"{{Algorithm}}"', '''"(U') "+"{{Algorithm}}"''')

u2_front = "{{#U2}}"+_front.replace("[aufmoves[0]]","[aufmoves[2]]")+"{{/U2}}"
u2_back = u_back.replace("U Algorithm","U2 Algorithm")
u2_back = u2_back.replace('"(U) "+"{{Algorithm}}"', '''"(U2) "+"{{Algorithm}}"''')

