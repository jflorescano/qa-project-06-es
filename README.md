# Pruebas para el parámetro "name" en la creación de un kit para la aplicación Urban.Grocers

# Requerimientos: 
-Instalación del paquete pytest. 
-Instalación del paquete requests. 


# Descripción del proyecto
 
En este proyecto se incluye la automatización de nueve pruebas para el parámetro "name" al crear un nuevo kit, 
las pruebas se describen a continuación:

-Prueba 1: El número permitido de caracteres (1), para esta prueba se utiliza el nombre: "a"
 
-Prueba 2: El número permitido de caracteres (511), para esta prueba se utiliza el nombre: "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"

-Prueba 3: El número de caracteres es menor que la cantidad permitida (0), para esta prueba se utiliza el nombre: ""

-Prueba 4: El número de caracteres es mayor que la cantidad permitida (512), para esta prueba se utiliza el nombre: Abcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

-Prueba 5: Se permiten caracteres especiales, para esta prueba se utiliza el nombre: ""№%@","

-Prueba 6: Se permiten espacios, para esta prueba se utiliza el nombre: " A Aaa "
 
-Prueba 7: Se permiten números, para esta prueba se utiliza el nombre: "123"

-Prueba 8: El parametro no se pasa en la solicitud, para esta prueba no se proporciona el parámetro "name"
 
-Prueba 9: Se ha pasado un tipo de parámetro diferente (número), para esta prueba se utiliza el nombre: 123 

# Usuario 
Para realizar las pruebas para el parámetro "name" al crear un nuevo kit, se esta considerando que la creación de un nuevo usuario ha 
sido existosa y se creado un authToken, para esto el parámetro "user_body", debe de contener la siguiente informacion: 
user_body = {
    "firstName": "Joana",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
Al utilizar este user_body se garantiza la creación exitosa de un nuevo usuario y se puede evaluar el nombre del kit. 

# Instrucciones sobre las funciones 
Para realizar las pruebas se cuenta con tres funciones:
 
---def positive_assert(kit_name)--
Esta función recibe como argumento el nombre con el que se quiere crear un nuevo kit y se espera tener una respuesta de estado 201.

--def negative_assert(kit_name)--
Esta función recibe como argumento el nombre con el que se quiere crear un nuevo kit y se espera tener una respuesta de estado 400.

--def negative_assert_no_name(kit_body)--
Esta función recibe como argumento el cuerpo de la solicitud sin el parámetro "name" y se espera tener una respuesta de estado 400. 

# Pruebas 
Para crear una nueva prueba se deben de seguir los siguientes requisitos:
 
-Es necesario que la prueba comience con la palabra "test" para que la pueda reconocer y ejecutar Pytest.
 
Se recomienda que las pruebas tengan nombres claros sobre lo que se estpa evaluando. 
Para las pruebas se puede utilizar la función positive_assert, negative_assert o negative_assert_no_name, dependiendo del resultado 
que se espera obtener en cada prueba.  


# Documentación 
La documentación utilizada para este proyecto es la API Urban Grocers 


