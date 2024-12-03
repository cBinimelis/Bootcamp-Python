CREATE TABLE estudiante
(
	idEstudiante SERIAL PRIMARY KEY NOT NULL,
	niu int,
	nombre VARCHAR(30),
	apellido VARCHAR(30),
	nroIdentificacion INT,
	fechaNacimiento DATE,
	genero VARCHAR(15)
);

CREATE TABLE facultad
(
	idFacultad SERIAL PRIMARY KEY NOT NULL,
	nombre VARCHAR(60)
);

CREATE TABLE semestre_academico
(
	idSemestreAcademico SERIAL PRIMARY KEY NOT NULL,
	fechaInicio DATE,
	fechaTermino DATE
);

CREATE TABLE programa_academico
(
	idProgramaAcademico SERIAL PRIMARY KEY NOT NULL,
	nombre VARCHAR(50),
	creditosTotales INT,
	creditosObligatorios INT,
	creditosopcionales INT,
	descripcion TEXT
);

CREATE TABLE direccion
(
	idDireccion SERIAL PRIMARY KEY NOT NULL,
	idEstudiante INT NOT NULL,
	calle VARCHAR(50),
	numero VARCHAR(6),
	comuna VARCHAR(30),
	region VARCHAR(30),
	FOREIGN KEY(idEstudiante) REFERENCES estudiante(idEstudiante)
);

CREATE TABLE docente
(
	idDocente SERIAL PRIMARY KEY NOT NULL,
	nombreDocente VARCHAR(80),
	nroIdentificacion INT,
	fechaNacimiento DATE,
	genero VARCHAR(15),
	telefono VARCHAR(10),
	fechaInicioJefatura DATE
);

CREATE TABLE departamento
(
	idDepartamento SERIAL PRIMARY KEY NOT NULL,
	idDocente INT NOT NULL,
	idFacultad INT NOT NULL,
	nombreDepartamento VARCHAR(50),
	cantidadProfesores int,
	FOREIGN KEY (idDocente) REFERENCES docente(idDocente),
	FOREIGN KEY (idFacultad) REFERENCES facultad(idFacultad)
);

ALTER TABLE docente
ADD COLUMN idDepartamento INT NOT NULL;

ALTER TABLE docente
ADD CONSTRAINT docente_idDepartamento
FOREIGN KEY (idDepartamento) REFERENCES departamento(idDepartamento);

CREATE TABLE curso
(
	idCurso SERIAL PRIMARY KEY NOT NULL,
	idProgramaAcademico INT NOT NULL,
	idDocente INT NOT NULL,
	nombreCurso VARCHAR(30),
	FOREIGN KEY (idProgramaAcademico) REFERENCES programa_academico (idProgramaAcademico),
	FOREIGN KEY (idDocente) REFERENCES docente (idDocente)
);

CREATE TABLE asignatura
(
	idAsignatura SERIAL PRIMARY KEY NOT NULL,
	idDepartamento INT NOT NULL,
	idCurso INT NOT NULL,
	codigo VARCHAR(20),
	titulo VARCHAR(50),
	nroCreditos INT,
	descripcion TEXT,
	tieneLaboratorio BOOL,
	idRequisitoPrevio INT NOT NULL,
	FOREIGN KEY (idDepartamento) REFERENCES departamento(idDepartamento),
	FOREIGN KEY (idCurso) REFERENCES curso(idCurso),
	FOREIGN KEY (idRequisitoPrevio) REFERENCES asignatura(idAsignatura)
);

CREATE TABLE proyecto_final_carrera
(
	idProyectoFinalCarrera SERIAL PRIMARY KEY NOT NULL,
	idDocente INT NOT NULL,
	idEstudiante INT NOT NULL,
	fecha DATE,
	calificacion NUMERIC,
	FOREIGN KEY (idDocente) REFERENCES docente (idDocente),
	FOREIGN KEY(idEstudiante) REFERENCES estudiante(idEstudiante)
);

CREATE TABLE estudiante_programa
(
	idEstudiante INT NOT NULL,
	idProgramaAcademico INT NOT NULL,
	FOREIGN KEY(idEstudiante) REFERENCES estudiante(idEstudiante),
	FOREIGN KEY (idProgramaAcademico) REFERENCES programa_academico (idProgramaAcademico)
);

CREATE TABLE materias_cursar
(
	idMateriasCursar SERIAL PRIMARY KEY NOT NULL,
	idEstudiante INT NOT NULL,
	idSemestreAcademico INT NOT NULL,
	idCurso INT NOT NULL,
	FOREIGN KEY(idEstudiante) REFERENCES estudiante(idEstudiante),
	FOREIGN KEY(idSemestreAcademico) REFERENCES semestre_academico(idSemestreAcademico),
	FOREIGN KEY (idCurso) REFERENCES curso(idCurso)
);

CREATE TABLE registro_notas
(
	idRegistroNotas SERIAL PRIMARY KEY NOT NULL,
	idMateriasCursar INT NOT NULL,
	calificacion NUMERIC,
	idAsignatura INT NOT NULL,
	FOREIGN KEY (idMateriasCursar) REFERENCES materias_cursar (idMateriasCursar)
);

ALTER TABLE facultad
ADD CONSTRAINT not_null_empty
CHECK (nombre IS NOT NULL AND CHAR_LENGTH(TRIM(nombre)) > 0)