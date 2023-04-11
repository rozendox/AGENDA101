create table QUARTA
(
    id       INTEGER
        primary key autoincrement,
    HORARIO1 INTEGER not null,
    MATERIA1 TEXT    not null,
    HORARIO2 INTEGER not null,
    MATERIA2 TEXT    not null
);

create table QUINTA
(
    id       INTEGER
        primary key autoincrement,
    HORARIO1 INTEGER not null,
    MATERIA1 TEXT    not null,
    HORARIO2 INTEGER not null,
    MATERIA2 TEXT    not null
);

create table SABADO
(
    id       INTEGER
        primary key autoincrement,
    HORARIO  INTEGER not null,
    MATERIA1 TEXT    not null,
    HORARIO2 INTEGER not null,
    MATERIA2 TEXT    not null
);

create table SEGUNDA
(
    id       INTEGER
        primary key autoincrement,
    HORARIO1 INT  not null,
    MATERIA1 TEXT not null,
    HORARIO2 INT  not null,
    MATERIA2 TEXT not null
);

create table NOTA_SEGUNDA
(
    ID_nota INTEGER not null
        constraint NOTA_SEGUNDA_pk
            primary key autoincrement
        constraint NOTA_SEGUNDA_SEGUNDA_id_fk
            references SEGUNDA,
    afazer  TEXT    not null
);

create table SEXTA
(
    id       INTEGER
        primary key autoincrement,
    HORARIO1 INTEGER not null,
    MATERIA1 TEXT    not null,
    HORARIO2 INTEGER not null,
    MATERIA2 TEXT    not null
);

create table TERCA
(
    id       INTEGER
        primary key autoincrement,
    HORARIO1 INT  not null,
    MATERIA1 TEXT not null,
    HORARIO2 INT  not null,
    MATERIA2 TEXT
);

create table sqlite_master
(
    type     TEXT,
    name     TEXT,
    tbl_name TEXT,
    rootpage INT,
    sql      TEXT
);

create table sqlite_sequence
(
    name,
    seq
);

create table terça
(
    id       INTEGER
        primary key autoincrement,
    NOME     TEXT not null,
    CONTEUDO TEXT not null
);

