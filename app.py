from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_reynolds_number(velocity, density, viscosity, length):
    return (velocity * density * length) / viscosity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        velocity = float(request.form['velocity'])
        density = float(request.form['density'])
        viscosity = float(request.form['viscosity'])
        length = float(request.form['length'])

        reynolds_number = calculate_reynolds_number(velocity, density, viscosity, length)

        if reynolds_number < 2000:
            flow_type = "Laminar"
            return render_template('laminar.html', reynolds_number=reynolds_number, flow_type=flow_type)
        elif 2000 <= reynolds_number <= 4000:
            flow_type = "Transitional"
            return render_template('transitional.html', reynolds_number=reynolds_number, flow_type=flow_type)
        else:
            flow_type = "Turbulent"
            return render_template('turbulent.html', reynolds_number=reynolds_number, flow_type=flow_type)
    except ValueError:
        return render_template('index.html', error="Please enter valid numerical values.")

if __name__ == '__main__':
    app.run(debug=True)
