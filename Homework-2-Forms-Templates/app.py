from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        <label>Toppings</label><br>
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_froyo_toppings': request.args.get('toppings')
    }
    # users_froyo_flavor = request.args.get('flavor')
    # users_foryo_toppings = request.args.get('toppings')
    return render_template("froyo_results.html", **context)
    # return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {users_foryo_toppings}!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite Color, Animal and City?<br/>
        <label>Color</label><br>
        <input type="text" name="color"><br/>
        <label>Animal</label><br>
        <input type="text" name="animal"><br/>
        <label>City</label><br>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    users_favorite_color = request.args.get('color')
    users_favorite_animal = request.args.get('animal')
    users_favorite_city = request.args.get('city')
    return f"Wow, I didn't know {users_favorite_color} {users_favorite_animal} lived in {users_favorite_city}!"

@app.route('/secret_message')
def secret_message():
    
   return """
    <form action="/message_results" method="POST">
        What is your Secret Message?<br/>
        <label>Secret Message</label><br>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    return f"Here's your secret message! <br> {sort_letters(users_message)}"

@app.route('/calculator')
def calculator():
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():

    users_first_num = int(request.args.get('operand1'))
    users_second_num = int(request.args.get('operand2'))
    users_operator = request.args.get('operation')
    answer = 0
    context = {
        'users_first_num': users_first_num,
        'users_second_num': users_second_num,
        'users_operator': users_operator,
        'answer': answer
    }
    # users_first_num = int(request.args.get('operand1'))
    # users_second_num = int(request.args.get('operand2'))
    # users_operator = request.args.get('operation')
    # answer = 0
    print(users_first_num)
    if (users_operator == "add"):
        context['answer'] = users_first_num + users_second_num
    elif (users_operator == "subtract"):
        context['answer'] = users_first_num - users_second_num
    elif (users_operator == "divide"):
        context['answer'] = users_first_num / users_second_num
    elif (users_operator == "multiply"):
        context['answer'] = users_first_num * users_second_num
    pass
    return render_template("calculator_results.html", **context)



# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic', 
    'cottenheadedninnymuggins'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    name = request.args.get('users_name')
    wants_compliments = request.args.get("wants_compliments")
    num_compliments = int(request.args.get("num_compliments"))
    if (wants_compliments == "yes"):
        random_compliments = random.sample(list_of_compliments,k=num_compliments)
    elif (wants_compliments == "no"):
        pass
    context = {
        # TODO: Enter your context variables here.
        'name': name,
        'compliments_list': random_compliments,
        'wants_compliments': wants_compliments
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
