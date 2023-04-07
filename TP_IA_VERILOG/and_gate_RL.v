logic signed [WIDTH-1:0] coeff;
logic signed [WIDTH-1:0] intercept;

// Appel au module de calcul des coefficients de la régression
linear_regression #(WIDTH, DEPTH) lin_reg(price, size, coeff, intercept);

// Calcul de la prédiction
assign y = intercept + coeff * size;

