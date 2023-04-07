#include <stdio.h>

float prediction(float *features, int n_features) {
    float prediction = -8152.937710;
    prediction += 717.258370 * features[0];
    prediction += 36824.195974 * features[1];
    prediction += 101571.840022 * features[2];
    return prediction;
}

int main() {
    float features[] = {1.0, 2.0, 3.0};
    float result = prediction(features, 3);
    printf("Result: %f\n", result);
    return 0;
}
