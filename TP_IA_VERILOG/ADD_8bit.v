module adder_8bit(a, b, result);
    input [7:0] a, b;
    output [7:0] result;

    reg [7:0] carry;
    wire [7:0] sum;

    assign sum = a + b + carry;
    assign result = sum;

    always @(a or b or carry) begin
        if (sum > 255) begin
            carry <= 1;
        end else begin
            carry <= 0;
        end
    end

endmodule