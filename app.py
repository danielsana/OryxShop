from flask import *

import pymysql

app = Flask(__name__)

# set secret key to secure your session/make it unique
app.secret_key = "AW_r%@idsjg9djg9dgj9djg9dg9dg98dg9djN*HU4AW_r%@jN*HU4AW_r%@jN*HU4"

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

# single  item  Note this route has an product_id, It displays a product based on product_id
@app.route('/single_item/<product_id>')
def single(product_id):
    # connect to db
    connection = pymysql.connect(host="localhost", user='root', password='', database='oryxdb')

    # Create SQL  - %s is a placeholder, which will take the actual ID during Query Execution.
    sql1 = "SELECT * FROM products WHERE product_id = %s"

     # Cursor - Used to run/execute above SQL
    cursor1 = connection.cursor()

     # Execute SQL providing product_id - NB: Sql had a placeholder in the Where clause thats why we provide the product_id
    cursor1.execute(sql1, (product_id))

    # Get the product retrieved 
    product = cursor1.fetchone()

    return render_template('single.html',product=product)

# signup user
@app.route('/signup',methods=['POST','GET'])
def signup():
     # Check if form was posted by user
    if request.method == 'POST':
            # Receive what was posted by user including username, password1,password2 email, phone
            username = request.form['username']
            email = request.form['email']
            phone = request.form['phone']
            password1 = request.form['password1']
            password2 = request.form['password2']

            # check if any of the password is less than eight x-ters and notify the user to put a password more that 8 -xters  
            if len(password1) < 8:
                return render_template('signup.html', error='Password must more than 8 xters')
		
            # Check if the 2 passwords are matching, if not notify the user to match them up.		
            elif password1 != password2:
                return render_template('signup.html', error='Password Do Not Match')
            else:
	        # Now we can save username, password, email, phone into our users table
		# Make a connection to database
                connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='oryxdb')
		# Create an Insert SQL, Note the SQL has 4 placeholders, Real values to be provided later			     
                sql = ''' 
                     insert into users(username, password, email, phone) 
                     values(%s, %s, %s, %s)
                 '''
		# Create a cursor to be used in Executing our SQL 
                cursor = connection.cursor()
		# Execute SQL, providing the real values to replace our placeholders 
                cursor.execute(sql, (username, password1, email,phone))
		# Commit to Save to database
                connection.commit()
		# Return a message to user to confirm successful registration.
                return render_template('signup.html', success='Registered Successfully')
    else:
        return render_template('signup.html')
    
# signin 
@app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Make a connection to database
        connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='oryxdb')
        sql = '''
           select * from users where username = %s and password = %s
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))

        if cursor.rowcount == 0:
            return render_template('signin.html', error='Invalid Credentials')  
        else:
            # ADD THIS
            session['key'] = username  # link the session key with username
            return redirect('/')  # redirect to Home Default route, After success Login
    else:
        return render_template('signin.html')

# logout 
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/signin')

# mpesa 
# Below we only need to use a POST, as posted in our Single item
@app.route('/mpesa', methods = ['POST'])
def mpesa():
    # Receive the amount and phone from single item
    phone = request.form['phone']
    amount = request.form['amount']
    # import mpesa.py module
    import mpesa
    # Call the SIM Toolkit(stk) push function present in mpesa.py
    mpesa.stk_push(phone, amount)
    # SHow user below message.
    return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
    '<a href="/" class="btn btn-dark btn-sm">Back to Products</a>'


# signup vendor
@app.route('/vendorsignup',methods=['POST','GET'])
def vendorsignup():
     # Check if form was posted by user
    if request.method == 'POST':
            # Receive what was posted by user including everything
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            county = request.form['county']
            password1 = request.form['password1']
            password2 = request.form['password2']
            email = request.form['email']

            # check if any of the password is less than eight x-ters and notify the user to put a password more that 8 -xters  
            if len(password1) < 8:
                return render_template('vendor.html', error='Password must more than 8 xters')
		
            # Check if the 2 passwords are matching, if not notify the user to match them up.		
            elif password1 != password2:
                return render_template('vendor.html', error='Password Do Not Match')
            else:
	        # Now we can save username, password, email, phone into our users table
		# Make a connection to database
                connection = pymysql.connect(host='localhost', user='root', password='',database='oryxdb')
		# Create an Insert SQL, Note the SQL has 4 placeholders, Real values to be provided later			     
                sql = ''' 
                     insert into vendors(firstname, lastname, county, password, email) 
                     values(%s, %s, %s, %s, %s)
                 '''
		# Create a cursor to be used in Executing our SQL 
                cursor = connection.cursor()
		# Execute SQL, providing the real values to replace our placeholders 
                cursor.execute(sql, (firstname, lastname, county, password1, email))
		# Commit to Save to database
                connection.commit()
		# Return a message to user to confirm successful registration.
                return render_template('vendor.html', success='Vendor Registered Successfully')
    else:
        return render_template('vendor.html')

app.run(debug=True)