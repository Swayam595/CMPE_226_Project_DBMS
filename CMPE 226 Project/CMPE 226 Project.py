from flask import Flask, render_template, request, json, jsonify
from flaskext.mysql import MySQL
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from werkzeug import generate_password_hash, check_password_hash
from crud import sql_select, sql_delete, sql_update, sql_insert
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from bson.objectid import ObjectId

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'multicloud'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# MongoDB configurations
# app.config['MONGO_DBNAME'] = 'multicloud'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/multicloud'
# mongodb = PyMongo(app)
client = MongoClient('mongodb://localhost:27017/')
mongodb = client['multicloud']


@app.route('/')
def main():
    app.logger.info('In main API, rendering index.html')
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    app.logger.info('In showSignUp API, rendering signup.html')
    return render_template('signup.html')

@app.route('/showLogin')
def showLogin():
    app.logger.info('In showLogin API, rendering login.html')
    return render_template('login.html')

@app.route('/showCustomerAccountDisplay')
def showCustomerAccountDisplay():
    app.logger.info('In showCustomerAccountDisplay API, rendering customerAccountDisplay.html')
    return render_template('customerAccountDisplay.html')

@app.route('/showMachines')
def showMachines():
    app.logger.info('In showMachines API, rendering machines.html')
    return render_template('machines.html')

@app.route('/showOrderHistory')
def showOrderHistory():
    app.logger.info('In showOrderHistory API, rendering orderHistory.html')
    return render_template('orderHistory.html')

@app.route('/showBilling')
def showBilling():
    app.logger.info('In showBilling API, rendering billing.html')
    return render_template('billing.html')

@app.route('/showProfile')
def showProfile():
    app.logger.info('In showProfile API, rendering profile.html')
    return render_template('profile.html')

@app.route('/showHelp')
def showHelp():
    app.logger.info('In showHelp API, rendering help.html')
    return render_template('help.html')

@app.route('/showCsp')
def showCsp():
    app.logger.info('In showCsp API, rendering csp.html')
    return render_template('csp.html')

@app.route('/showCspMachines')
def showCspMachines():
    app.logger.info('In showCspMachines API, rendering cspMachines.html')
    return render_template('cspMachines.html')

@app.route('/showCspOrderHistory')
def showCspOrderHistory():
    app.logger.info('In showCspOrderHistory API, rendering cspOrderHistory.html')
    return render_template('cspOrderHistory.html')

@app.route('/showCspProfile')
def showCspProfile():
    app.logger.info('In showCspProfile API, rendering cspProfile.html')
    return render_template('cspProfile.html')

@app.route('/showCspHelp')
def showCspHelp():
    app.logger.info('In showCspHelp API, rendering cspHelp.html')
    return render_template('cspHelp.html')

@app.route('/showCspBilling')
def showCspBilling():
    app.logger.info('In showCspBilling API, rendering cspBilling.html')
    return render_template('cspBilling.html')

@app.route('/showAdmin')
def showAdmin():
    app.logger.info('In showAdmin API, rendering admin.html')
    return render_template('admin.html')

@app.route('/showAdminMachines')
def showAdminMachines():
    app.logger.info('In showAdminMachines API, rendering adminMachines.html')
    return render_template('adminMachines.html')

@app.route('/showAdminOrder')
def showAdminOrder():
    app.logger.info('In showAdminOrder API, rendering adminOrder.html')
    return render_template('adminOrder.html')

@app.route('/showAdminCustomers')
def showAdminCustomers():
    app.logger.info('In showAdminCustomers API, rendering adminCustomers.html')
    return render_template('adminCustomers.html')

@app.route('/showAdminCSP')
def showAdminCSP():
    app.logger.info('In showAdminCSP API, rendering adminCSP.html')
    return render_template('adminCSP.html')

@app.route('/showAdminBilling')
def showAdminBilling():
    app.logger.info('In showAdminBilling API, rendering adminBilling.html')
    return render_template('adminBilling.html')

@app.route('/showAdminProfile')
def showAdminProfile():
    app.logger.info('In showAdminProfile API, rendering adminProfile.html')
    return render_template('adminProfile.html')

@app.route('/showAdminComplaints')
def showAdminComplaints():
    app.logger.info('In showAdminComplaints API, rendering adminComplaints.html')
    return render_template('adminComplaints.html')

@app.route('/showAdminOffer')
def showAdminOffer():
    app.logger.info('In showAdminOffer API, rendering adminOffer.html')
    return render_template('adminOffer.html')

@app.route('/myCSPs', methods=['GET'])
def myCSPs():
    app.logger.info("In myCSPs API, retrieving csp's for given ca")
    try:
        _ca_id = request.args['inputCaId']
        if _ca_id:
            results = {'resultsAvailable': sql_select('select * from csp c join csp_contracts o on c.csp_id=o.csp_id where o.ca_id='+_ca_id+' and c.csp_id not in (select m.csp_id from machine m where m.order_id is not null)'),
                               'resultsOccupied': sql_select(
                                   'select * from csp c join csp_contracts o on c.csp_id=o.csp_id where o.ca_id=' + _ca_id + ' and c.csp_id in (select m.csp_id from machine m where m.order_id is not null)')}
            app.logger.debug("In myCSPs API, retrieved csp's for given ca:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In myCSPs API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In myCSPs API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/myCustomers', methods=['GET'])
def myCustomers():
    app.logger.info("In myCustomers API, retrieving customers's for given ca")
    try:
        _ca_id = request.args['inputCaId']
        if _ca_id:
            results = {'results': sql_select('select * from customer c join onboards o on c.customer_id=o.customer_id where c.customer_isDelete=0 and o.ca_id='+_ca_id)}
            app.logger.debug("In myCustomers API, retrieved customers's for given ca:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In myCustomers API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In myCustomers API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/currentOrders', methods=['GET'])
def currentOrders():
    app.logger.info("In currentOrders API, retrieving current orders of customer or csp or ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        _ca_id = request.args['inputCaId']
        if _id and _ca_id and _role == "customer":
            print('select * from order_customer where customer_id="' + _id + '" and ca_id="' + _ca_id + '" and order_end_date is null')
            results = {'results': sql_select('select * from order_customer where customer_id="' + _id + '" and ca_id="' + _ca_id + '" and order_end_date is null')}
            app.logger.debug("In currentOrders API, retrieved current orders of customer:", results)
            return json.dumps(results)
        elif _id and _ca_id and _role == "csp":
            results = {'results': sql_select('select * from order_csp where csp_id="' + _id + '" and ca_id="' + _ca_id + '" and order_end_date is null')}
            app.logger.debug("In currentOrders API, retrieved current orders of csp:", results)
            return json.dumps(results)
        elif _id and _ca_id and _role == "ca":
            results = {'results': sql_select('select * from order_ o join receives r on o.order_id=r.order_id where o.ca_id="' + _ca_id + '" and o.order_end_date is null')}
            app.logger.debug("In currentOrders API, retrieved current orders of ca:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In currentOrders API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In currentOrders API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/orderHistory', methods=['GET'])
def orderHistory():
    app.logger.info("In orderHistory API, retrieving order history of customer or csp or ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        _ca_id = request.args['inputCaId']
        if _id and _ca_id and _role == "customer":
            results = {'results': sql_select('select * from order_customer where customer_id="'+_id+'" and ca_id="'+ _ca_id +'" and order_end_date is not null')}
            app.logger.debug("In orderHistory API, retrieved order history of customer:", results)
            return json.dumps(results)
        elif _id and _ca_id and _role == "csp":
            results = {'results': sql_select('select * from order_csp where csp_id="' + _id + '" and ca_id="' + _ca_id + '" and order_end_date is not null')}
            app.logger.debug("In orderHistory API, retrieved order history of csp:", results)
            return json.dumps(results)
        elif _id and _ca_id and _role == "ca":
            results = {'results': sql_select('select * from order_ o join receives r on o.order_id=r.order_id where o.ca_id="' + _ca_id + '" and o.order_end_date is not null')}
            app.logger.debug("In orderHistory API, retrieved order history of ca:", results)
            # print('select * from order_ o join receives r on o.order_id=r.order_id where o.ca_id="' + _ca_id + '" and o.order_end_date is not null')
            return json.dumps(results)
        else:
            app.logger.debug("In orderHistory API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In orderHistory API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/getMachines', methods=['GET'])
def getMachines():
    app.logger.info("In getMachines API, retrieving machines ordered by customers or ca or available with csp")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        _ca_id = request.args['inputCaId']
        if _id and _ca_id and _role == "customer":
            results = {'results': sql_select('select m.*, ord.ca_id from order_customer ord join machine_customer m on ord.order_id=m.order_id where ord.customer_id="'+_id+'" and ord.ca_id="'+ _ca_id +'" and order_end_date is null')}
            app.logger.debug("In getMachines API, retrieved machines ordered by customers:", results)
            return json.dumps(results)
        elif _id and _ca_id and _role == "csp":
            results = {'results': sql_select('select m.* from machine m where m.csp_id="' + _id + '";')}
            app.logger.debug("In getMachines API, retrieved machines available with csp:", results)
            return json.dumps(results)
        elif _id and _ca_id and _role == "ca":
            results = {'results': sql_select('select m.*, ord.customer_id from order_ ord join machine m on ord.order_id=m.order_id where ord.ca_id="' + _ca_id + '" and order_end_date is null')}
            # print('select * from order_ ord join machine m on ord.order_id=m.order_id where ord.ca_id="' + _ca_id + '" and order_end_date is null')
            app.logger.debug("In getMachines API, retrieved machines ordered by ca:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In getMachines API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In getMachines API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/bill/current', methods=['GET'])
def current_bill():
    app.logger.info("In current_bill API, retrieving unpaid current bills for customer or ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        if _id and _role == "customer":
            results = {'results': sql_select('select * from customer_bill where customer_id="'+_id+'" and is_paid is False;')}
            app.logger.debug("In current_bill API, retrieved unpaid current bills for customer:", results)
            # print('select * from customer_bill where customer_id="'+_id+'"')
            return json.dumps(results)
        elif _id and _role == "ca":
            results = {'results': sql_select('select * from ca_bill where ca_id="' + _id + '" and is_paid is False;')}
            app.logger.debug("In current_bill API, retrieved unpaid current bills for ca:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In current_bill API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In current_bill API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/bill/history', methods=['GET'])
def bill_history():
    app.logger.info("In bill_history API, retrieving paid bills history for customer or ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        if _id and _role == "customer":
            results = {'results': sql_select('select * from customer_bill where customer_id="'+_id+'" and is_paid is True;')}
            app.logger.debug("In bill_history API, retrieved paid bills history for customer:", results)
            return json.dumps(results)
        elif _id and _role == "ca":
            results = {'results': sql_select('select * from ca_bill where ca_id="' + _id + '" and is_paid is True;')}
            app.logger.debug("In bill_history API, retrieved paid bills history for  ca:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In bill_history API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In bill_history API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/revenue/current', methods=['GET'])
def current_revenue():
    app.logger.info("In current_revenue API, retrieving revenue for csp or ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        if _id and _role == "ca":
            results = {'results': sql_select('select * from customer_bill where ca_id="'+_id+'" and is_paid is False;')}
            app.logger.debug("In current_revenue API, retrieved revenue for ca:", results)
            # print('select * from customer_bill where customer_id="'+_id+'"')
            return json.dumps(results)
        elif _id and _role == "csp":
            results = {'results': sql_select('select * from ca_bill where csp_id="' + _id + '" and is_paid is False;')}
            app.logger.debug("In current_revenue API, retrieved revenue for csp:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In current_revenue API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In current_revenue API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/revenue/history', methods=['GET'])
def revenue_history():
    app.logger.info("In revenue_history API, retrieving revenue history for csp or ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        if _id and _role == "ca":
            results = {'results': sql_select('select * from customer_bill where ca_id="' + _id + '" and is_paid is True;')}
            app.logger.debug("In revenue_history API, retrieved revenue history for ca:", results)
            # print('select * from customer_bill where customer_id="'+_id+'"')
            return json.dumps(results)
        elif _id and _role == "csp":
            results = {'results': sql_select('select * from ca_bill where csp_id="' + _id + '" and is_paid is True;')}
            app.logger.debug("In revenue_history API, retrieved revenue history for csp:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In revenue_history API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In revenue_history API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/bill/generate', methods=['GET'])
def generate_bill():
    app.logger.info("In generate_bill API, generating bills for ca or customer")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        conn = mysql.connect()
        cursor = conn.cursor()
        messages = []
        if _id and _role == "ca":
            # print(_id, _role)
            for ca_id, customer_id in sql_select('select order_.ca_id, order_.customer_id from onboards join order_ on order_.customer_id = onboards.customer_id and order_.ca_id = onboards.ca_id where order_.ca_id="' + _id + '";'):
                # print("Generating bill for customer_id:", customer_id)
                cursor.callproc('sp_generate_bill_ca', (datetime.now().day, datetime.now().month, datetime.now().year, ca_id, customer_id))
                message = cursor.fetchall()
                if len(message):
                    # print(message[0])
                    messages.append(message[0])
                    app.logger.debug("In generate_bill API, generated bill for customer:", message[0])
                else:
                    app.logger.error("In generate_bill API: Error in sp_generate_bill_ca:", str(messages[0]))
                    return json.dumps({'Error': str(messages[0])}), 500
            conn.commit()
            return json.dumps({'message': messages})
        elif _id and _role == "csp":
            for csp_id, ca_id in sql_select('select receives.csp_id, order_.ca_id from receives join order_ on order_.order_id = receives.order_id where receives.csp_id="' + _id + '";'):
                # print("Generating bill for ca_id:", ca_id)
                cursor.callproc('sp_generate_bill_csp', (datetime.now().day, datetime.now().month, datetime.now().year, csp_id, ca_id))
                message = cursor.fetchall()
                if len(message):
                    # print(message[0])
                    messages.append(message[0])
                    app.logger.debug("In generate_bill API, generated bill for ca:", message[0])
                else:
                    app.logger.error("In generate_bill API: Error in sp_generate_bill_csp:", str(messages[0]))
                    return json.dumps({'Error': str(messages[0])}), 500
            conn.commit()
            return json.dumps({'message': messages})
        else:
            app.logger.debug("In generate_bill API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In generate_bill API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/bill/pay', methods=['GET'])
def pay_bill():
    app.logger.info("In pay_bill API, paying current bills of customer or ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        _bill_id = request.args['inputBillId']
        if _id and _role == "customer":
            sql_update('update bill set is_paid = True where customer_id=' + id + 'and bill_id=' + _bill_id + ' and is_paid = False;')
            results = {'results':"Bill:"+str(_bill_id)+"is paid by customer:"+str(_id)}
            app.logger.debug("In pay_bill API, paid current bills of customer:", results)
            return json.dumps(results)
        elif _id and _role == "ca":
            sql_update('update bill set is_paid = True where ca_id=' + id + 'and bill_id=' + _bill_id + ' and is_paid = False;')
            results = {'results': "Bill:" + str(_bill_id) + "is paid by ca:" + str(_id)}
            app.logger.debug("In pay_bill API, paid current bills of ca:", results)
            return json.dumps(results)
        else:
            app.logger.debug("In pay_bill API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In pay_bill API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/login', methods=['POST'])
def login():
    app.logger.info("In login API, logging in for ca or csp or customer")
    # print(request.form)
    try:
        _email = request.form['inputEmailLogin']
        _password = request.form['inputPasswordLogin']
        _role = request.args['inputRole']

        if _email and _role == "customer":
            userRow = sql_select('select customer_id, customer_email_id, customer_name, customer_password, customer_bank_account from customer where customer_email_id="'+_email+'"')
            if check_password_hash(userRow[0][3], _password):
                results = {'results': userRow}
                app.logger.debug("In login API, customer - logged in:", results)
                return json.dumps(results)
            else:
                app.logger.error("In login API : Error:", {'error': 'Invalid password'})
                return json.dumps({'error': 'Invalid password'}), 500
        elif _email and _role == "ca":
            userRow = sql_select('select ca_id, ca_email_id, ca_name, ca_password, ca_bank_account_number from ca where ca_email_id="'+_email+'"')
            if check_password_hash(userRow[0][3], _password):
                results = {'results': userRow}
                app.logger.debug("In login API, ca - logged in:", results)
                return json.dumps(results)
            else:
                app.logger.error("In login API : Error:", {'error': 'Invalid password'})
                return json.dumps({'error': 'Invalid password'}), 500
        elif _email and _role == "csp":
            userRow = sql_select('select csp_id, csp_email_id, csp_name, csp_password, csp_bank_account_number from csp where csp_email_id="'+_email+'"')
            if check_password_hash(userRow[0][3], _password):
                results = {'results': userRow}
                app.logger.debug("In login API, csp - logged in:", results)
                return json.dumps(results)
            else:
                app.logger.error("In login API : Error:", {'error': 'Invalid password'})
                return json.dumps({'error': 'Invalid password'}), 500
        else:
            app.logger.debug("In login API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"}), 500
    except Exception as e:
        app.logger.error("In login API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/placeOrder', methods=['POST'])
def placeOrder():
    app.logger.info("In palceOrder API, placing order for customer")
    try:
        _startDate = request.form['inputOrderStartDate']
        _ram = request.form['inputRam']
        _cpu = request.form['inputCpu']
        _diskSize = request.form['inputDiskSize']
        _noOfMahcines = request.form['inputNoOfMachines']
        _customer_id = request.args['customer_id']
        _ca_id = request.args['inputCaId']

        conn = mysql.connect()
        cursor = conn.cursor()

        if _startDate and _ram and _cpu and _diskSize and _noOfMahcines and _customer_id and _ca_id:
            cursor.callproc('sp_create_order', (_startDate, _ram, _cpu, _diskSize, _noOfMahcines, _customer_id, _ca_id))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                app.logger.debug("In palceOrder API, placed order for customer:", _customer_id)
                return json.dumps({'message': 'Order placed successfully !'})
            else:
                results = {'message': "Required machines are not available, couldn't place the order"}
                app.logger.debug("In palceOrder API : Error:", results)
                return json.dumps(results)
        else:
            app.logger.debug("In palceOrder API: Missing mandatory parameters")
            return json.dumps({"message": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In palceOrder API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    app.logger.info("In signup API, signing up customer, ca and csp")
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _bank_account_number = request.form['inputBankAccount']
        _role = request.args['inputRole']
        _ca_id = request.args['inputCaId']

        conn = mysql.connect()
        cursor = conn.cursor()

        # validate the received values
        if _name and _email and _password and _bank_account_number and _ca_id:
            # All Good, let's call MySQL
            _hashed_password = generate_password_hash(_password)
            if _role == 'customer':
                cursor.callproc('sp_create_customer', (_email, _name, _hashed_password, _bank_account_number, _ca_id))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    app.logger.debug("In signup API, customer signed up:", _name)
                    return json.dumps({'message': 'User created successfully !'})
                else:
                    results = {'message': "User already exists!"}
                    app.logger.debug("In signup API : Error:", results)
                    return json.dumps(results), 500
            elif _role == 'csp':
                cursor.callproc('sp_create_csp', (_email, _name, _hashed_password, _bank_account_number, _ca_id))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    app.logger.debug("In signup API, csp signed up:", _name)
                    return json.dumps({'message': 'Csp created successfully !'})
                else:
                    results = {'message': "Csp already exists!"}
                    app.logger.debug("In signup API : Error:", results)
                    return json.dumps(results), 500
            elif _role == 'ca':
                cursor.callproc('sp_create_ca', (_email, _name, _hashed_password, _bank_account_number))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    app.logger.debug("In signup API, csp signed up:", _name)
                    return json.dumps({'message': 'ca created successfully !'})
                else:
                    results = {'message': "ca already exists!"}
                    app.logger.debug("In signup API : Error:", results)
                    return json.dumps(results), 500
            else:
                app.logger.debug("In signup API: Missing mandatory parameters")
                return json.dumps({"results": "Missing mandatory parameters"})

    except Exception as e:
        app.logger.error("In signup API: Error:", str(e))
        return json.dumps({'error': str(e)})
    # finally:
    #     cursor.close()
    #     conn.close()

@app.route('/updateProfile', methods = ['POST'])
def updateProfile():
    app.logger.info("In updateProfile API, updating profile of ca or csp or customer")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _bank_account_number = request.form['inputBankAccount']
        _hashed_password = generate_password_hash(_password)
        conn = mysql.connect()
        cursor = conn.cursor()
        if _id and _role:
            if _role == 'csp':
                cursor.callproc('sp_update_csp', (_id, _email, _name, _hashed_password, _bank_account_number))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    results = {'results': { "_name" : _name, "_password" : _password, "_bank_account_number": _bank_account_number, "_hashed_password": _hashed_password}}
                    app.logger.debug("In updateProfile API : updated profile of csp:", results)
                    return json.dumps(results)
                else:
                    results = {'message': "Couldn't update profile."}
                    app.logger.debug("In updateProfile API : Error:", results, data[0])
                    return json.dumps(results)
            elif _role == 'customer':
                print(request.form)
                cursor.callproc('sp_update_customer', (_id, _email, _name, _hashed_password, _bank_account_number))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    results = {'results': { "_name" : _name, "_password" : _password, "_bank_account_number": _bank_account_number, "_hashed_password": _hashed_password}}
                    app.logger.debug("In updateProfile API : updated profile of customer:", results)
                    return json.dumps(results)
                else:
                    results = {'message': "Couldn't update profile."}
                    app.logger.debug("In updateProfile API : Error:", results, data[0])
                    return json.dumps(results)
            elif _role == 'ca':
                cursor.callproc('sp_update_ca', (_id, _email, _name, _hashed_password, _bank_account_number))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    results = {'results': { "_name" : _name, "_password" : _password, "_bank_account_number": _bank_account_number, "_hashed_password": _hashed_password}}
                    app.logger.debug("In updateProfile API : updated profile of ca:", results)
                    return json.dumps(results)
                else:
                    results = {'message': "Couldn't update profile."}
                    app.logger.debug("In updateProfile API : Error:", results, data[0])
                    return json.dumps(results)
            else:
                app.logger.debug("In updateProfile API: Missing mandatory parameters")
                return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In updateProfile API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/updateCustomerProfile', methods = ['POST'])
def updateCustomerProfile():
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _bank_account_number = request.form['inputBankAccount']
        _offer_id = request.form['inputOfferId']
        conn = mysql.connect()
        cursor = conn.cursor()
        if _id and _role:
            if _role == 'customer':
                cursor.callproc('sp_update_customer_admin', (_id, _email, _name, _bank_account_number, _offer_id))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    return json.dumps({'results': {"_name": _name, "_bank_account_number": _bank_account_number}})
                else:
                    return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/help', methods=['POST'])
def help():
    app.logger.info("In myCSPs API, retrieving csp's for given ca")
    try:
        _id = request.args['inputId']
        _role = request.args['inputRole']
        _problem_title = request.form['inputProblemTitle']
        _problem_description = request.form['inputProblemDescription']
        if _id and _role and _problem_title and _problem_description:
            record = {
                "id": _id,
                "role": _role,
                "problem_title": _problem_title,
                "problem_description": _problem_description,
                "date": datetime.utcnow(),
                "resolved": "no"
            }
            tickets = mongodb.tickets
            ticket_id = tickets.insert(record)
            # print(ticket_id, tickets.find_one({'_id': ticket_id}))
            # print(dict(tickets.find_one({'_id': ticket_id})))
            return jsonify({"result": "ticket created with id"+str(ticket_id)})
        else:
            app.logger.debug("In current_revenue API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In current_revenue API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/getTickets', methods=['GET'])
def get_tickets():
    app.logger.info("In myCSPs API, retrieving csp's for given ca")
    try:
        tickets_array = []
        id = request.args['inputId']
        role = request.args['inputRole']
        if id and role != "ca":
            tickets = mongodb.tickets
            user_tickets = tickets.find({"id":id, "role": role})
            for ticket in user_tickets:
                # print(dict(ticket))
                temp = dict()
                for key in ticket:
                    if key != '_id':
                        temp[key] = ticket[key]
                    else:
                        temp[key] = str(ticket[key])
                tickets_array.append(temp)
            return jsonify({"result":tickets_array})
        elif role == "ca":
            tickets = mongodb.tickets
            user_tickets = tickets.find()
            for ticket in user_tickets:
                temp = dict()
                for key in ticket:
                    if key != '_id':
                        temp[key] = ticket[key]
                    else:
                        temp[key] = str(ticket[key])
                tickets_array.append(temp)
            return jsonify({"result":tickets_array})
        else:
            return json.dumps({'error': 'Enter required fields'}), 500
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/resolveIssue', methods=['GET'])
def resolveIssue():
    try:
        _id = request.args['inputIssueId']
        if _id:
            mongodb.tickets.update({'_id': ObjectId(_id)}, {'$set': {"resolved": "yes"}}, upsert=False)
            return json.dumps({'msg': 'Issue resolved'})
        else:
            app.logger.debug("In current_revenue API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In current_revenue API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/createOffer', methods = ['POST'])
def createOffer():
    app.logger.info("In myCSPs API, retrieving csp's for given ca")
    try:
        _id = request.args['inputId']
        _name = request.form['inputName']
        _discount = request.form['inputDiscount']
        if _id and _name and _discount:
            sql_insert('insert into offer (offer_name, discount, ca_id, is_used ) values ( "'+ _name +'", ' + _discount + ', '+_id+',0);')
            return json.dumps({'message': 'Offer created successfully !'})
        else:
            app.logger.debug("In current_revenue API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In current_revenue API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/getOffer', methods = ['GET'])
def getOffer():
    app.logger.info("In getOffer API, retrieving csp's for given ca")
    try:
        _ca_id = request.args['inputCaId']
        _customer_id = request.args['inputId']
        _role = request.args['inputRole']
        if _ca_id and _role:
            if _role == 'ca':
                return json.dumps({'results': sql_select('select * from offer where ca_id = '+ _ca_id +';')})
            if _role == 'customer':
                return json.dumps({'results': sql_select('select * from customer c join offer o on c.customer_offer_id=o.offer_id where  c.customer_id = '+ _customer_id +';')})
        else:
            app.logger.debug("In getOffer API: Missing mandatory parameters")
            return json.dumps({"results": "Missing mandatory parameters"})
    except Exception as e:
        app.logger.error("In current_revenue API: Error:", str(e))
        return json.dumps({'error': str(e)})

@app.route('/deleteOffer', methods = ['DELETE'])
def deleteOffer():
    try:
        _offer_id = request.args['offerId']
        if _offer_id:
            return json.dumps({'results': sql_delete('delete from offer where offer_id = '+ _offer_id +';')})
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/endOrder', methods = ['GET'])
def endOrder():
    try:
        _order_id = request.args['orderId']
        conn = mysql.connect()
        cursor = conn.cursor()
        if _order_id:
            cursor.callproc('sp_end_order', (_order_id, _order_id))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                return json.dumps({'html': '<span>Order Ended</span>'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/addMachine', methods = ['POST'])
def addMachine():
    print(request.form)
    try:
        _csp_id = request.args['inputId']
        _ip_address = request.form['inputIpAddress']
        _ram = request.form['inputRam']
        _disk_size = request.form['inputDiskSize']
        _price = request.form['inputPrice']
        _cpu_cores = request.form['inputCpuCores']
        sql_insert('insert into machine (csp_id, disk_size, ram, cpu_cores, ip_address, price, order_id ) values ( "'+ _csp_id +'", "' + _disk_size + '", '+_ram+', '+_cpu_cores+', "'+_ip_address+'", '+_price+',null);')
        return json.dumps({'message': 'Machine created successfully !'})
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/deleteMachine', methods = ['DELETE'])
def deleteMachine():
    try:
        _mac_id = request.args['inputId']
        if _mac_id:
            return json.dumps({'results': sql_delete('delete from machine where mac_id = '+ _mac_id +';')})
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/deleteCustomer', methods = ['DELETE'])
def deleteCustomer():
    try:
        _customer_id = request.args['inputId']
        if _customer_id:
            return json.dumps({'results': sql_delete('update customer set customer_isDelete=true where customer_id = '+ _customer_id +';')})
    except Exception as e:
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    # handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)
