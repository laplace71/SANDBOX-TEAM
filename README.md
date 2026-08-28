# Repositorio de Entrenamiento: Git y GitHub

## Objetivo del Repositorio
Este espacio es un entorno de pruebas cerrado (Sandbox) creado estrictamente para que el equipo de desarrollo practique el flujo de trabajo colaborativo. El propósito de este repositorio es ejecutar comandos, familiarizarse con el entorno y cometer errores de manera segura antes de iniciar el desarrollo del proyecto oficial.

## Reglas Estrictas de Integración
*   **Protección de la rama principal:** La rama `main` se encuentra bloqueada por configuración de sistema. Cualquier intento de ejecutar un `git push origin main` directo será rechazado automáticamente.
*   **Trabajo aislado:** Todo integrante debe trabajar obligatoriamente en una rama secundaria individual.
*   **Sincronización constante (Pull):** Es un requisito inquebrantable ejecutar `git pull origin main` antes de comenzar a trabajar cada día. Esto asegura que el entorno local esté actualizado y evita conflictos de código con el trabajo de los demás compañeros.
*   **Revisión de código:** Ningún cambio pasará a la rama principal sin haber pasado por un Pull Request y contar con la aprobación técnica del Scrum Master.

## Flujo de Trabajo Obligatorio (Tarea Inicial)
Para que la tarea de configuración en Trello sea considerada como "Terminada", cada integrante debe completar el siguiente ciclo exacto en su computadora:

### Paso 1: Clonar el repositorio
Descargar el entorno de trabajo localmente mediante la terminal y entrar a la carpeta:
```bash
git clone [Reemplazar_con_el_enlace_del_repositorio]
cd [Nombre_de_la_carpeta]
```

### Paso 2: Actualizar el entorno (Pull)
Antes de crear cualquier rama o hacer modificaciones, es obligatorio traer los últimos cambios del servidor para estar al día. Este comando debe convertirse en un hábito cada vez que abran el proyecto:
```bash
git pull origin main
```

### Paso 3: Crear una rama de trabajo
Queda prohibido trabajar en `main`. Crear y cambiar inmediatamente a una rama personal usando el comando `switch` con el prefijo "feature/" seguido de su nombre:
```bash
git switch -c feature/[tu-nombre]
```

### Paso 4: Modificación de archivos
Crear un archivo de texto dentro de la carpeta clonada con el nombre `archivo-[tu-nombre].txt`. Dentro de este archivo, escribir un breve párrafo respondiendo a la siguiente pregunta: ¿Qué expectativas tienes sobre el proyecto final?

### Paso 5: Registro de cambios (Commit)
Preparar y empaquetar los cambios realizados en el archivo de texto:
```bash
git add .
git commit -m "Añade archivo de prueba de [tu-nombre]"
```

### Paso 6: Subida al servidor (Push)
Enviar la rama personal al repositorio remoto en GitHub:
```bash
git push origin feature/[tu-nombre]
```

### Paso 7: Solicitud de Integración (Pull Request)
1. Ingresar a la interfaz web de este repositorio en GitHub.
2. Hacer clic en el botón "Compare & pull request" que aparecerá automáticamente.
3. Crear la solicitud para fusionar los cambios de la rama personal hacia la rama `main`.
4. Esperar la revisión y aprobación del Scrum Master.
