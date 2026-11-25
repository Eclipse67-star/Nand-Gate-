import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start NAND Gate Test")
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.uio_in.value = 0
    dut.rst_n.value = 1

    # Test 0 NAND 0 = 1
    dut.ui_in.value = 0b00
    await ClockCycles(dut.clk, 2)
    assert dut.uo_out.value == 1

    # Test 0 NAND 1 = 1
    dut.ui_in.value = 0b01
    await ClockCycles(dut.clk, 2)
    assert dut.uo_out.value == 1

    # Test 1 NAND 0 = 1
    dut.ui_in.value = 0b10
    await ClockCycles(dut.clk, 2)
    assert dut.uo_out.value == 1

    # Test 1 NAND 1 = 0
    dut.ui_in.value = 0b11
    await ClockCycles(dut.clk, 2)
    assert dut.uo_out.value == 0
