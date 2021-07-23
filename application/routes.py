from flask import redirect, url_for, request, render_template
from . import app
from . import db
from .models import Frankendama
from .forms import FrankForm

@app.route('/')
@app.route('/home')
def home():

    franks = Frankendama.query.all()
    
    return render_template("home.html", franks=franks)


@app.route("/create", methods=["GET", "POST"]) 
def create():
    
    form = FrankForm()

    if request.method == 'POST':
        new_frank = Frankendama(
            title=form.title.data,
            description=form.description.data,
            tama=form.tama.data,
            sarado=form.sarado.data,
            sword=form.sword.data,
            string=form.string.data,
            bearing=form.bearing.data
            )
        db.session.add(new_frank)
        db.session.commit()

        return redirect(url_for("home"))
    
    else:

        return render_template("create.html", form=form)

@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    frank = Frankendama.query.get(id)
    form = FrankForm()

    if form.validate_on_submit():

        
        frank.title=form.title.data
        frank.description=form.description.data
        frank.tama=form.tama.data
        frank.sarado=form.sarado.data
        frank.sword=form.sword.data
        frank.string=form.string.data
        frank.bearing=form.bearing.data
            
        
        db.session.add(frank)  
        db.session.commit()

        return redirect(url_for("home"))
    
    else:

        return render_template("create.html", form=form)


@app.route("/delete/<int:id>")
def delete(id):
    frank = Frankendama.query.get(id)

    db.session.delete(frank)
    db.session.commit()

    return redirect(url_for("home")) 

