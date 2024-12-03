# Modulo V - Sesión V

## Agenda

- Transacciones

## Transacciones

### Entendiendo transacciones con PostgreSQL

Una transacción es una secuencia de operaciones individuales que se realizan como una sola unidad de trabajo. Estas operaciones pueden incluir inserciones, actualizaciones, eliminaciones o consultas en una base de datos. La transacción garantiza que todas estas operaciones se completen exitosamente como un conjunto o que ninguna de ellas se complete si una falla.
Las transacciones en PostgreSQL siguen el concepto ACID, que significa Atomicidad, Consistencia, Aislamiento y Durabilidad.

Para iniciar una transacción, normalmente se utiliza la sentencia BEGIN, seguida de una serie de operaciones SQL, y luego se completa con un COMMIT para confirmar los cambios o un ROLLBACK para deshacerlos en caso de error o necesidad de reversión.

### Principios ACID

Una transacción tiene cuatro características esenciales conocidas con el acrónimo ACID:

- **Atomicity (Atomicidad):** una transacción es una unidad atómica; o se ejecutan las operaciones múltiples por completo, o no se ejecuta absolutamente nada, donde cualquier cambio parcial es revertido para asegurar la consistencia en la base de datos.

- **Consistency (Consistencia):** cuando finaliza una transacción, debe dejar todos los datos sin ningún tipo de inconsistencia, por lo que las reglas de integridad serán aplicadas a todos los cambios realizados por la transacción, es decir, todas las estructuras de datos internas deben de estar en un estado consistente.

- **Isolation (Aislamiento o independencia):** esto significa que los cambios de cada transacción son independientes de los cambios de otras que se ejecuten en ese instante, es decir, que los datos afectados de una transacción no están disponibles para otras transacciones, sino hasta que la que los ocupa finalice por completo.
- **Durability (Permanencia):** después de que las transacciones hayan terminado, todos los cambios realizados son permanentes en la base de datos, incluso si después se produce una caída del DBMS.

### DCL (DATA CONTROL LANGUAGE) - LENGUAJE DE CONTROL DE DATOS

Permite crear roles, permisos e integridad referencial, así como el control al acceso a la base de datos.

- **GRANT:** usado para otorgar privilegios de acceso de usuario a la base de datos.
- **REVOKE:** utilizado para retirar privilegios de acceso otorgados con el comando GRANT.

### TCL (TRANSACTIONAL CONTROL LANGUAGE) - LENGUAJE DE CONTROL TRANSACCIONAL

Permite administrar diferentes transacciones que ocurren dentro de una base de datos.

- **COMMIT:** empleado para guardar el trabajo hecho.
- **ROLLBACK:** utilizado para deshacer la modificación generada desde el último COMMIT.
