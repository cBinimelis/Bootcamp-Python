-- COMANDO BEGIN
UPDATE cuentas SET balance = balance - 100.00 WHERE n_cuenta = 0127365;
UPDATE cuentas SET balance = balance - 100.00 WHERE n_cuenta = 0795417;


-- COMANDO COMMIT
BEGIN;
    INSERT INTO cuentas
        (n_cuenta, nombre, balance)
    VALUES
        (0679259, 'Pepe', 200);
    UPDATE cuentas SET balance = balance - 137.00 WHERE nombre = 'Pepe';
    UPDATE cuentas SET balance = balance + 137.00 WHERE nombre = 'Juan';
    SELECT nombre, balance
    FROM cuentas
    WHERE nombre = 'Pepe' AND nombre = 'Juan';
    COMMIT
END;


-- COMANDO ROLLBACK
BEGIN;
    -- SENTENCIAS SQL
    COMMIT;
    ROLLBACK;
END;


-------- EJERCICIO --------
BEGIN;
CREATE USER Juan WITH PASSWORD 'PASS1';
COMMIT;

DROP USER Juan;

