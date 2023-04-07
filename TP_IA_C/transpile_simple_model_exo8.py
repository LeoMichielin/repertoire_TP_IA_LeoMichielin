import joblib

def transpile_linear_model(model):
    # Extract model coefficients
    coef = model.coef_
    intercept = model.intercept_

    # Generate C code to compute prediction
    code = "#include <stdio.h>\n\n"
    code += "float prediction(float *features, int n_features) {\n"
    code += "    float prediction = %f;\n" % intercept
    for i, c in enumerate(coef):
        code += "    prediction += %f * features[%d];\n" % (c, i)
    code += "    return prediction;\n"
    code += "}\n"

    # Generate C code for a main function that calls prediction
    code += "\nint main() {\n"
    code += "    float features[] = {1.0, 2.0, 3.0};\n"
    code += "    float result = prediction(features, %d);\n" % len(coef)
    code += "    printf(\"Result: %f\\n\", result);\n"
    code += "    return 0;\n"
    code += "}\n"

    return code

# Load trained model
model = joblib.load("model.joblib")

# Generate C code for the model
c_code = transpile_linear_model(model)

# Save C code to a file
with open("model.c", "w") as f:
    f.write(c_code)

# Print command to compile the code
print("To compile the code, run: gcc -o model model.c")

# Compile and run the code
import subprocess
subprocess.call(["gcc", "-o", "model", "model.c"])
subprocess.call(["./model"])