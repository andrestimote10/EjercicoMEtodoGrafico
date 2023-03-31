from bokeh.plotting import  figure,output_file,show

#Preparamos los datos.

x=[-20,-10,0,10,20,30,40,50]
x2=[2,2]
y1=[(35/3)-(5/3)*i for i in x]
y2=[-150,150]
y3=[2*i for i in x]
px=[(35/11),2,2]
py=[(70/11),4,(25/3)]

#Salida en un HTML
output_file("grafico.html")
#Crear el nuevo grafico.
p = figure(title="Ejercicio 8", x_axis_label="x", y_axis_label="y",
y_range=[0,10], x_range=[0, 10], tools="")
#Agregar datos.
p.line(x, y1, color="blue", legend="40x + 30y <= 600", line_wide=2)
p.line(x2, y2, color="green", legend="x >= 3", line_width=2)
p.line (x, y3, color="red", legend="y >= 2x", line_width=2)
p.patch(px,py,color="purple",legend="Region Solucion",alpha=0.3)
p.circle(px, py, color="black")

#Mostrar.
show(p)
