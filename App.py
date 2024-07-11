from flask import Flask ,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app= Flask(__name__)

#Mysql conexion
app.config['MYSQL_HOST']= 'localhost'   
app.config['MYSQL_USER']= 'root'   
app.config['MYSQL_PASSWORD']= ''   
app.config['MYSQL_DB']= 'new'   
mysql=MySQL(app)

#sesion
app.secret_key='mysecretkey'
 

@app.route('/')
def Index ():
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM new1')
        data=cur.fetchall()
  
        return render_template ('index.html',contacts =data)
    
@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method=='POST':
        
       nombre= request.form['nombre'] 
       celular= request.form['celular'] 
       correo= request.form['correo'] 
       cur= mysql.connection.cursor()
       cur.execute('INSERT INTO new1 (nombre,celular,correo) VALUES (%s,%s,%s)',(nombre,celular,correo))
       mysql.connection.commit()
       flash ('Persona agregada correctamente')
    
    
    
    return redirect(url_for('Index'))
    

@app.route ('/edit/<id>')
def get_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM new1 WHERE id = %s',[id])
    data=cur.fetchall()
    print (data)
    return render_template('edit.html',contact=data[0])


@app.route ('/update/<id>' ,methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombre=request.form['nombre']
        celular=request.form['celular']
        correo=request.form['correo']
        
    cur=mysql.connection.cursor()
    cur.execute("""UPDATE new1 SET nombre=%s, celular=%s, correo=%s WHERE id=%s """,(nombre,celular,correo,id))
    mysql.connection.commit()
    flash('Empleado actualizado correctamente')
    return redirect(url_for('Index'))
        
        

@app.route ('/delete/<string:id>')
def delete_contact(id):
 cur=mysql.connection.cursor()
 cur.execute('DELETE FROM new1 WHERE id={0}'.format(id))
 mysql.connection.commit()
 flash('Empleado borrado exitosamente')
 return redirect(url_for('Index'))

if __name__=='__main__':
    {
        app.run(port=3306,debug =True)
    }
