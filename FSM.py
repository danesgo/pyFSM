def write_PSL(y):
    f.write('--Present State Logic\n')
    f.write('process(clk, rst)\n')
    f.write('begin \n')
    f.write("    if(rst='1') then \n")
    f.write('	    state<=')
    f.write(str(y))
    f.write('; \n')
    f.write('    elsif(rising_edge(clk)) then\n')
    f.write('	    state <= next_state;\n')
    f.write('    end if;\n')
    f.write('end process;\n')
    f.write('\n')

def write_OL(x):
    f.write('--Output Logic')
    f.write('process(state)\n')
    f.write('begin\n')
    f.write('   case state is\n')
    for j in x:
        f.write('when ')
        f.write(str(j.pop(0)))
        f.write('=>Z<=')
        f.write("'")
        f.write(str(j.pop()))
        f.write("'; \n")
    f.write('end case; \n')
    f.write('end process;\n ')
    f.write('\n')

def write_NSL(x,y):
    f.write('--Next State Logic\n')
    f.write('process(state, X)\n')
    f.write('begin \n')
    f.write('   case state is\n')
    for i in range(len(x)):
        s = x[i].pop(0)
        f.write('       when ')
        f.write(str(s))
        f.write(' =>\n')
        sl = x[i]
        sx = y[i]
        for j in range(len(sl)):
            f.write("           if(X='")
            f.write(str(sx[j]))
            f.write("') then\n")
            f.write('               next_state<=')
            f.write(str(sl[j]))
            f.write(';\n')
            f.write('           end if;\n')
    f.write('   end case;\n')
    f.write('end process;\n')
    f.write('-- :3\n')

print "Generador FSM"
m=[]
b=[]
c=[]
#arreglo de logica de salida
ol=[]
#arreglo de logica del siguiente estado
nsl=[]
#arreglo de los valores de x correspondientes al siguiente estado
nslx=[]
cnt=0
f = open('FSM.vhd', 'w')

while(1):
    a = raw_input('Ingrese # para finalizar:').split(",")
    #salida pantalla de ingreso
    if a[0] == '#':
        break
    #guardar el vector a en la matriz m solo por comparativa
    m.append(a)

for l in m:    
    #Escritura de la logica de estado presente (Present State Logic)
    #con el primer estado ingresado
    if cnt==0:
        #funcion de escritura en el archivo definida con anterioridad
        write_PSL(l[0]);
    
    #generar vector de logica de salida
    b.append(l[0])
    b.append(l.pop())
    ol.append(b)
    #limpia el vector para la siguiente iteracion
    b=[]
    #extrae el valor 'z'
    l.pop()

    #generar vectores de estados
    while(1):
        k = l.pop()
        if k == 's':
            break
        b.append(k)    
    print b
    b.append(l[0])
    b.reverse()
    nsl.append(b)
    #limpia el vector para la siguiente iteracion
    b=[]

    #generar vectores de valores de x
    while(1):
        k = l.pop()
        if k == 'x':
            break
        b.append(k)    
    print b
    b.reverse()
    nslx.append(b)
    #limpia el vector para la siguiente iteracion
    b=[]
    print l
    cnt = cnt + 1;
print ol
print nsl
print nslx
write_OL(ol);
write_NSL(nsl,nslx);
f.close()
print m



