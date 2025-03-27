from flask import Flask , request ,flash , redirect , url_for
from flask import render_template
from .prjClass import PrjClass

def createFlask():
    app=Flask(__name__)
    app.config['SECRET_KEY']="ZSHSAHAHA"
    @app.errorhandler(FileNotFoundError)
    def handle_file_not_found(error):
        return render_template('404.html'), 404  

    
    obj=PrjClass()
    #This is a route which is used any time that an action is done .For showing the file content.
    @app.route('/view')
    def view():
        filename=request.args.get('filename')
        title=request.args.get('title')
        if not filename or not title:  
            flash('Filename or title missing!', 'error')
            return redirect(url_for('home'))
        fileContent= obj.tablemaker(filename)
        return render_template('table.html', fileContent=fileContent ,title=title )
    
    #This route is used for getting user data from interface and add to the file:
    @app.route('/add',methods=['POST','GET'])
    def add():
        if request.method=='POST':
           item=request.form.get('itemtoadd')
           quantity=request.form.get('quantitytoadd')
           price=request.form.get('pricetoadd')
           filename = request.args.get('filename')
           title = request.args.get('title')
           if item == "" or quantity == "" or price == "":
                flash("Item , quantity and price should be written!", 'error') 
                return redirect(url_for('view' , filename=filename, title=title)) 
           result=obj.add(item,quantity,price)
           if result=="repeat":
              flash("No repeated item !",'error')
           else :
              flash("Item added !",'success') 

        return redirect(url_for('view' , filename=filename, title=title))  

    #This is a route through which the user chosen item is deleted:
    @app.route('/delete' , methods=['GET','POST'])
    def delete():
        if request.method == 'POST':
            filename=request.args.get('filename')
            title=request.args.get('title')
            item=request.form.get('delItem') 
            if item == "":
                flash("Item not selected!", 'error') 
                return redirect(url_for('view' , filename=filename, title=title)) 
            result=obj.delete(item)
            if result == "Not":  
                flash(f"No such item :{item}", 'error')
            else:
                flash("Item deleted !","success")     
        return redirect(url_for('view' , filename=filename, title=title))  
    
    #This is a route for changing the chosen item by user and applying the delete method on it: 
    @app.route('/change' , methods=['GET','POST']) 
    def change():
        if request.method == 'POST':
            filename=request.args.get('filename')
            title=request.args.get('title')
            item=request.form.get('chItem')
            price=request.form.get('chPrice')
            quantity=request.form.get('chQuantity')
            if item == "" or quantity == "" or price == "":
                flash("Item , quantity and price should be written!", 'error') 
                return redirect(url_for('view' , filename=filename, title=title)) 

            result=obj.change(item, quantity,price)
            if result == 'Not':
                flash('No such item!', 'error')
            else:
                flash('Item changed!', 'success')
        return redirect(url_for('view', filename=filename, title=title))    
    return app

