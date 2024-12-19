from flask import Flask, render_template
import owlready2

# Initialize Flask App
app = Flask(__name__)

# Load ontology using Owlready2
onto_path = "joel_math.rdf"  # Update with the correct path to your ontology
onto = owlready2.get_ontology(onto_path).load()

# Route for the home page
@app.route('/')
def index():
    # Extracting all instances (individuals) of the classes in the ontology
    integration_classes = list(onto.Integration.instances())
    function_classes = list(onto.Function.instances())
    result_classes = list(onto.Result.instances())
    step_classes = list(onto.Steps.instances())
    technique_classes = list(onto.Techniques.instances())

    # Rendering the template and passing the instances to the frontend
    return render_template(
        'index.html', 
        integration_classes=integration_classes, 
        function_classes=function_classes,
        result_classes=result_classes,
        step_classes=step_classes,
        technique_classes=technique_classes
    )

# Route for viewing a specific class
@app.route('/view_class/<class_name>')
def view_class(class_name):
    # Fetch the class from the ontology by name
    class_object = getattr(onto, class_name, None)
    
    if class_object:
        # If the class exists, render its details (for simplicity, displaying its name)
        return render_template('view_class.html', class_name=class_name)
    else:
        # If class does not exist
        return "Class not found", 404

if __name__ == '__main__':
    app.run(debug=True)
