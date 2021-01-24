from flask import Flask

from flask_pymongo import PyMongo

from flask import jsonify, request

app =Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/shahbaz"


mongo = PyMongo(app)

output = []

@app.route('/contact', methods=['GET'])
def get_all_data():
   contact = mongo.db.contact
   for q in contact.find():
        output.append({ 'Name' : q['Name'],'Contact': q['Contact'],'Email':q['Email']})

   return jsonify({ "result": output})

    

      
@app.route('/contact/<Name>',methods=['GET'])
def get_one_data(Name):
    contact = mongo.db.contact

    q= contact.find_one({'Name' : Name})

    if q:
      output = { 'Name' : q['Name'],'Contact': q['Contact'],'Email':q['Email']}
    else:
      output="NO record"
    return jsonify({'result': output})    

@app.route('/contact',methods=['POST'])
def add_data():
    contact = mongo.db.contact

    Name= request.json['Name']
    Contact=request.json['Contact']
    Email=request.json['Email']
    

   
    data_id=contact.insert({ 'Name' : Name,'Contact': Contact,'Email':Email})
    new_data = contact.find_one({'Name': Name})

    output = { 'Name' : new_data['Name'],'Contact': new_data['Contact'],'Email':new_data['Email']}
    return jsonify({'result': output})



@app.route('/contact/<Name>',methods=['DELETE'])
def data_user(Name):
     contact = mongo.db.contact
     q= contact.delete_one({'Name': Name})

     output = "Deleted Successfully"

     return jsonify({'result': output})




if __name__ == '__main__':
    app.run(debug=True)

    