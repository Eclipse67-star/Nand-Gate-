`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (1=output)
    input  wire       ena,      // always 1 when powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // Single 2-input NAND gate: Input 0 NAND Input 1 -> Output 0
  assign uo_out[0]   = ~(ui_in[0] & ui_in[1]);

  // Tie all unused outputs to 0
  assign uo_out[7:1] = 7'b0;
  assign uio_out     = 8'b0;
  assign uio_oe      = 8'b0;

  // List unused inputs to prevent compiler warnings
  wire _unused = &{ena, clk, rst_n, ui_in[7:2], uio_in, 1'b0};

endmodule
