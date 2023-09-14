from flask import Flask
from flask import render_template,request,redirect
from flasked.mysql import MYSQL
app=Flask(__name__)
mysql=MYSQL
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config[MYSQL_DATABASE-USER]='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.app.co[MYSQL_DATABASE_DB]='tickets3'
@app.route('/')
def index():
    Sql="select*form'persona';"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    persona=cursor.fetchall()
    print(persona)
    conn.comitc()
    return render_template('persona/index.html',perona=persona)
#codigo para eliminar vamos a utilizar el destroy
@app.route('/destroy/<int:id>')
def destroy(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("Delete from persona where id=%s",(id))
    conn.comit()
    return redirect('/')
#para editar int
@app.route('/edit/<int:id>')
def editar(id):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.excute("Select*From persona where id=%s",(id))
    persona=cursorfetchall()
    conn.comit()
    return render_template('persona/editar.html',persona=persona)
#para actalizar update
@app.route('/update',methods=['POST'])
def update():
#en base de datos poner la cedula
    _Nombre=request.form['txtNombre'] #ese la relacion que tenemos en la parte donde esta los formularios
    _Apellido=request.form['txtApellido']
    _Telefono=request.form['txtTelefono']
    _Cargo=request.form['txtCargo']
    id=request.form['txt']#llave primaria no se agrega _
    Sql="update persona SET Nombre=%s,Apellido=%s,Telefono=%s,Cargo=%s,id=%s;"
    datos=(_Nombre,_,Apellido,_Telefono,_cargo,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.excute(sql,datos)
    conn.comitc()
    return redirect("/")
@app.route('guardar')
def guardar():
    return render_template('persona/guardar.html')
@app.route('/store',methods=[Post])
def storage():
    _Nombre=request.form['txtNombre'] #ese la relacion que tenemos en la parte donde esta los formularios
    _Apellido=request.form['txtApellido']
    _Telefono=request.form['txtTelefono']
    _Cargo=request.form['txtCargo']
    id=request.form['txt']
    Sql="INSERT INTO persona ('id','Nombre,'Apellido,'Telefono','Cargo')Values(Null,%s,%s,%s,%s)"
    datos=(_Nombre,_Apellido,_Telefono,_Cargo)
    conn=mysql.connect()
    cursor=conn.cursor() 
    cursor.excute(sql,datos)
    conn.comit()
    return redirect('/')   
if(__name__=='__main__'):
    app.run(debug=True)
    