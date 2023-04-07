import joblib
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def transpile_logistic_model(model):
    # Extract model coefficients
    coef = model.coef_
    intercept = model.intercept_

    # Generate C code to compute prediction
    code = "#include <stdio.h>\n\n"
    code += "float sigmoid(float x) {\n"
    code += "    return 1.0 / (1.0 + exp(-x));\n"
    code += "}\n\n"
    code += "float prediction(float *features, int n_features) {\n"
    code += "    float linear_prediction = %f;\n" % intercept
    for i, c in enumerate(coef):
        code += "    linear_prediction += %f * features[%d];\n" % (c, i)
    code += "    float proba = sigmoid(linear_prediction);\n"
    code += "    return proba;\n"
    code += "}\n"

    # Generate C code for a main function that calls prediction
    code += "\nint main() {\n"
    code += "    float features[] = {1.0, 2.0, 3.0};\n"
    code += "    float proba = prediction(features, %d);\n" % len(coef)
    code += "    printf(\"Probability: %f\\n\", proba);\n"
    code += "    return 0;\n"
    code += "}\n"

    return code

# Load trained model
model2 = joblib.load("model.joblib")

# Generate C code for the model
c_code = transpile_logistic_model(model2)

# Save C code to a file
with open("model2.c", "w") as f:
    f.write(c_code)

# Print command to compile the code
print("To compile the code, run: gcc -o model2 model2.c -lm")

# Compile and run the code
import subprocess
subprocess.call(["gcc", "-o", "model2", "model2.c", "-lm"])
subprocess.call(["./model2"])

