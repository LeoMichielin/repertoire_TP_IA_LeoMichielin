import joblib
import numpy as np
from sklearn.tree import export_graphviz

def transpile_decision_tree(model):

    # Export tree to Graphviz dot file
    export_graphviz(model, out_file="tree.dot", feature_names=["x1", "x2"])

    # Parse dot file and generate C code
    with open("tree.dot", "r") as f:
        dot_code = f.read()

    code = "#include <stdio.h>\n\n"
    code += "float prediction(float *features, int n_features) {\n"
    code += "    int node_id = 0;\n"
    code += "    while (1) {\n"
    for line in dot_code.splitlines():
        if "label" in line:
            node_id, label = line.strip().split("[label=\"")
            node_id = int(node_id)
            label = label[:-2]  # Remove closing quotes and semicolon
            if "<=" in label:
                feature, threshold = label.split(" <= ")
                feature_id = int(feature[1:])
                threshold = float(threshold)
                code += "        if (features[%d] <= %f) {\n" % (feature_id, threshold)
                code += "            node_id = %d;\n" % model.tree_.children_left[node_id]
                code += "        } else {\n"
                code += "            node_id = %d;\n" % model.tree_.children_right[node_id]
                code += "        }\n"
            else:
                # Leaf node
                value = model.tree_.value[node_id][0][0]
                code += "        return %f;\n" % value
    code += "    }\n"
    code += "}\n"

    # Generate C code for a main function that calls prediction
    code += "\nint main() {\n"
    code += "    float features[] = {1.0, 2.0};\n"
    code += "    float result = prediction(features, %d);\n" % model.tree_.n_features
    code += "    printf(\"Result: %f\\n\", result);\n"
    code += "    return 0;\n"
    code += "}\n"

    return code

# Load trained model
model3 = joblib.load("model.joblib")

# Generate C code for the model
dot_code = transpile_decision_tree(model3)

# Save C code to a file
with open("model3.c", "w") as f:
    f.write(dot_code)

# Print command to compile the code
print("To compile the code, run: gcc -o model3 model3.c")

# Compile and run the code
import subprocess
subprocess.call(["gcc", "-o", "model3", "model3.c"])
subprocess.call(["./model3"])