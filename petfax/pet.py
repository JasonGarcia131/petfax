from flask import Blueprint, render_template, json, request

bp = Blueprint(
    'pet',
    __name__,
    url_prefix='/pets'
)

pets = json.load(open('pets.json'))

@bp.route('/')
def index():
   
    print(pets)
    return render_template('pets/index.html', pets = pets)

@bp.route('/<int:id>')
def show(id):
    pet = pets[id-1]
    print(pet)
    return render_template('pets/show.html', pet=pet)
    pass