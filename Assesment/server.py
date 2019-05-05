from flask import Flask, render_template, request, jsonify
import pyodbc
import json
import json2html
import collections


app = Flask(__name__)
#@app.route('/test')
#
#def test():
#    return "Flask is being used for Development"



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form.get(''))
        try:
            searchtext = request.form['searchtext']
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=yahyaexpress.database.windows.net;'
                      'Database=YahyaShoppingCart;'
                      'UID=myahya87;'
                      'PWD=System1433;'
                      )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM  shoppingcart where product like '%"+searchtext+"%'")

                
                
            objects_list = []
            for row in cursor:
                d = collections.OrderedDict()
                d['category'] =  row.category
                d['subcategory'] = row.subcategory
                d['product'] = row.product
                d['price'] = row.price
                d['Description'] = row.Description
                objects_list.append(d)
            j = json.dumps(objects_list)
            
            
        except valueError:
            return "Please check if the values are entered correctly"

        producresult = "<h1> Result for  "+searchtext+"</hr> <br/>" + json2html.json2html.convert(json=j)
        cursor = conn.cursor()
        cursor.execute("select * from shoppingcart where subcategory in (select distinct(subcategory) from shoppingcart where product like '%"+searchtext+"%')")
        objects_list = []
        for row in cursor:
            d = collections.OrderedDict()
            d['category'] =  row.category
            d['subcategory'] = row.subcategory
            d['product'] = row.product
            d['price'] = row.price
            d['Description'] = row.Description
            objects_list.append(d)
        j = json.dumps(objects_list)
        relevantresult = "<br/><br/><h1> similar products are  "+searchtext+"</hr> <br/>" + json2html.json2html.convert(json=j)
        
        return producresult + relevantresult
        
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5444)
