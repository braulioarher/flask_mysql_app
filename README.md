# Notas para flask y bases de datos

## Conectar a Mysql desde WSL

El primer paso es isntallar el paquete de mysql para esto se debe hace hacer lo siguiente

    sudo apt install mysql-client-core-8.0

Despues debemos de encontrar la direccion IPV4 de nuestra maquina virtual WSL pra esto:

    id a settigs->Network and Internet -> Status -> View Hardware and connection properties

    Buscar la opcion que diga vEthernet (WSL)
    la direccion debe ser similar a la siguiente 172.19.224.1

Despues trataremos de connectarnos desde WSL con el siguiente comando

    mysql -u wsl_root -p DATABASENAME -h 172.19.224.1

Lo anterior arroja un error pues el usuario no esta registrado aun en nuestro servidor  de MYSQL

Ahora daremos de alta un usuario a nuestro servidor que sera el usuario desde donde nos conectaremos en WSL para esto dentro de la terminal de MYSQL introducimos los siguiente comandos

    CREATE USER 'wsl_root'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON *.* TO 'wsl_root'@'localhost' WITH GRANT OPTION;
    CREATE USER 'wsl_root'@'%' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON *.* TO 'wsl_root'@'%' WITH GRANT OPTION;
    FLUSH PRIVILEGES;

Ahora para conectarnos a nuestra base de datos basta con usar el siguiente comando:
    mysql -u wsl_root -p DATABASENAME -h 172.19.224.1

Listo tenemos acceso a base de datos

## Hash contrasenas

Para hacer el hashing de coontrasenas se necesita un paquete que ya viene incluido al instalar Flask su nombre es Werkzeug de este paquete debemos importar  generate_password_hash y check_password_hash

    from werkzeug.security import generate_password_hash, check_password_hash

No dirigimos a nuestro modelo Users donde agregaremos una columna llama password_hash que almacenara la contrasena, tambien creamos metodo properties para generar y validar la contrasena por medio de las clases generate_password_hash, check_password_hash
