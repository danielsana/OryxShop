from flask import *

import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    # connect to db 
    connection = pymysql.connect(host="localhost", user='root', password='', database='oryxdb')

    # fetch electronics 
    sql1 = 'select * from products where product_category = "Electronics"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    electronics = cursor.fetchall()

    # fetch clothes 
    sql1 = 'select * from products where product_category = "Clothes"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    Clothes = cursor.fetchall()

    # fetch smartphones 
    sql1 = 'select * from products where product_category = "Clothes"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    Clothes = cursor.fetchall()

    # fetch clothes 
    sql1 = 'select * from products where product_category = "smartphones"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    smartphones = cursor.fetchall()

    # fetch utensils 
    sql1 = 'select * from products where product_category = "Utensils"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    Utensils = cursor.fetchall()

    # fetch others 
    sql1 = 'select * from products where product_category = "Other"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    others = cursor.fetchall()

    return render_template('home.html', electronics=electronics , clothes =Clothes, smartphones=smartphones, Utensils=Utensils, others=others)

# about us
@app.route('/upload',methods=['POST','GET'])
def upload():
    # Below if works when the Form in upload.html is Submitted/Sent
    if request.method == 'POST':
         # Below receives all variables sent/submitted from the Form
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename) 
        # Saves the image File in images folder, in static Folder.

        # connect to db
        connection = pymysql.connect(host="localhost", user='root', password='', database='oryxdb')

        cursor =connection.cursor()

        sql ='insert into products (product_name,product_desc,product_cost,product_category,product_image_name) values (%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql,(product_name,product_desc,product_cost,product_category,product_image_name.filename))
            connection.commit()
            return render_template('upload.html', message="product added success")
        except:
            connection.rollback()
            return render_template('upload.html', message="Failed to add the product")
    else:
        return render_template('upload.html')
# contact us
@app.route('/contact')
def contact():
    return "contact OryxSHOP"

app.run(debug=True)