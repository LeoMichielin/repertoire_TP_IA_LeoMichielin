module and_gate (e1,e2,cin,s,cout);
    input e1;
    input e2;
	input cin;
    output s;
	output cout;


    assign s = e1 ^ e2 ^ cin;
	assign cout = (e1 & e2) | (e1 & cin) | (e2 & cin);


endmodule
