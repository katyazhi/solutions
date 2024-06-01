import conductivity_fun

def test_factor():
    result = conductivity_fun.custom_factor(2,6)
    assert result == 0.707355302630646

def test_condcalc():
    result = conductivity_fun.conductivity_calculator(1.5,10000)
    assert result == 0.00015

def test_condcalc():
    result = conductivity_fun.conductivity_calculator(1.5,10000)
    assert result == 0.00015

def test_excel_work():
    result = conductivity_fun.excel_work("test_data.xlsx", 0.672)
    assert result == 0.000166 
