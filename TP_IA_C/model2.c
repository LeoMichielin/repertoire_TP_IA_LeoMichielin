#include <stdio.h>

float sigmoid(float x) {
    return 1.0 / (1.0 + exp(-x));
}

float prediction(float *features, int n_features) {
    float linear_prediction = -8152.937710;
    linear_prediction += 717.258370 * features[0];
    linear_prediction += 36824.195974 * features[1];
    linear_prediction += 101571.840022 * features[2];
    float proba = sigmoid(linear_prediction);
    return proba;
}

int main() {
    float features[] = {1.0, 2.0, 3.0};
    float proba = prediction(features, 3);
    printf("Probability: %f\n", proba);
    return 0;
}
