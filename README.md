# CloudNova - Aplicación Web con Monitoreo

Aplicación web Flask con gestión de usuarios y productos, desplegada con Docker/Vagrant, Nginx, MySQL, Prometheus y Grafana.

## Video del despliegue
https://youtu.be/_2yiXBV8tkE

## Despliegue con Vagrant

### Iniciar la VM
```bash
vagrant up
```

La aplicación estará disponible en: http://192.168.60.3

### Acceder a la VM
```bash
vagrant ssh servidorWeb
```
## Despliegue y prerrequisitos (máquina basada en ubuntu)

### Iniciar la aplicación
```bash
sudo apt update && sudo apt install docker docker-compose -y

sudo docker-compose up --build
```

### Servicios disponibles
- **Web App**: http://192.168.60.3 (Puerto 80) / https://192.168.60.3 (Puerto 443)
- **Prometheus**: http://192.168.60.3:9090
- **Grafana**: http://192.168.60.3:3000 (Usuario: `admin`, Contraseña: `admin`)
- **Node Exporter**: http://192.168.60.3:9100

### Detener servicios
```bash
sudo docker-compose down
```
## ¿Qué aprendió al integrar Docker, AWS y Prometheus?

Aprendimos a orquestar contenedores con Docker Compose, una herramienta muy poderosa que nos permite contener diferentes servicios en contenedores separados entre si y, exponerlos a diferentes puertos al mismo tiempo para su correcta operación y manej. A configurar una instacia segura en AWS EC2 y, aunque en primera instancia con recursos insuficientes, al momento de configurarla para tener los recursos respectivos se vuelve una herramienta muy poderosa para podertener diferentes aplicaciones o proyecto activos sin tener que gastar recursos propios. Al integrar Prometheus en esta orquestación, este nos ayuda a revisar constantemente la salud de nuestro proyecto, al configurar alertas y dashboards (grafana) que nos sirven para saber si algo esta yendo mal o directamente esta en estado crítico y necesita de un arreglo al momento en todo el ciclo de vida de nuestros proyectos.

## ¿Qué fue lo más desafiante y cómo lo resolvería en un entorno real?

En este caso fue la correcta orquestación de los servicios en el archivo de docker-compose.yml.
Aquí uno se tiene que asegurar de que cada servicios este configurado de manera correcta, ya que al momento de ser inicializados, como en este proyecto todos depende de todos entre sí, si llega a fallar uno todos los demás también fallarán. Esto se puede resolver adquiriendo mucha más experiencia al crear diferentes proyectos usando microservicios, realizando prueba y error para saber qué se tiene que ahcer y qué no.

También, al momento de la creación de la instancia en EC2 se había escogido la máquina t3.micro. Esta  no contaba con la capacidad necesaria para levantar todos los contenedores al mismo tiempo y se congelaba al querer usarse.
Por eso, se tomó la decisión de usar una máquina t3.small, la cual si contaba con los recursos y no nos presentaba ningún problema. En un entorno real, este problema se soluciona al agregar más recursos a las máquinas, ya sean virtual o personales o también, limitar la cantidad de recursos que un contenedor de docker puede utilizar.

## ¿Qué beneficio aporta la observabilidad en el ciclo DevOps?

Gracias a la observabilidad nos podemos enterar mucho antes de fallos que puedan ocurrir en el ciclo de despliegue y funcionamiento de nuestros proyectos además, las decisiones las podemos hacer basadas en los datos que se recolectan con los diferentes servicios que proveemos para el monitoreo y gestión. Todo esto es complementeado por una accesibilidad mucho más rápida a todos losd atos necesarios para poder realizar acciones al momento.