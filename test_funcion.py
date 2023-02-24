from funcion import minArreglo

def test_minArreglo():

    assert minArreglo([5,3,1,2])==1
    assert minArreglo([8,5,4,3])==3
    assert minArreglo([8,-5,4,3])==-5