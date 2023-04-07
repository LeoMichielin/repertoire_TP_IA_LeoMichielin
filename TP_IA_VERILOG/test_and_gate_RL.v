// Déclaration des signaux d'entrée/sortie
logic signed [15:0] price;
logic signed [15:0] size;
logic signed [15:0] y;

// Instanciation du module de test
regression #(.WIDTH(16), .DEPTH(32)) reg(price, size, y);

// Simulation
initial begin
    // Initialisation des signaux d'entrée
    price = 50000;
    size = 1000;

    // Attente d'un cycle
    #1;

    // Vérification de la prédiction
    if (y != 15000) $error("Regression test failed!");

    // Modification des signaux d'entrée
    price = 60000;
    size = 1200;

    // Attente d'un cycle
    #1;

    // Vérification de la prédiction
    if (y != 17000) $error("Regression test failed!");
end
