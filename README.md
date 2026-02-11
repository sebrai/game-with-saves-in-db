# Prosjektbeskrivelse – IT-utviklingsprosjekt (2IMI)

##  game saves projekt
**game saves**

---

## Deltakere
- Sebastian – backend/database
- Oscar – game programer
 

---

## 1. Prosjektidé og problemstilling

### Beskrivelse
vi lager et spill der progresjonen din blir lagret i en db, det er inspirert av Slay the Spire


### Målgruppe
er laget for de som har lyst til og spille et lite spill og ha det gåy mer enn en gang

---

## 2. Funksjoner

### systemet kan gjøre det følgende

1. *lar deg logge in*
2. *logge ut*
3. *se alle runns som du har startet*
4. *lar deg spille alle sammen*
5. *kan lagre progresjonen din i databasen*
6. *en 404 side som viser deg linker til det du kan trenge*



---

## 3. Teknologivalg

### Programmeringsspråk
 Python / JavaScript / HTML / CSS

### Rammeverk / Plattform / Spillmotor
 Flask 

### Database
- MariaDB

### Verktøy
- GitHub
- VSCode live share

---

## 4. Datamodell

### Oversikt over tabeller

**Tabell 1:**
- Navn: *users*
- Beskrivelse:*holder info om alle brukere*

**Tabell 2:**
- Navn: *runs*
- Beskrivelse: *holder info om hver spill som har blitt startet*

*(Minst 2–4 tabeller)*

### Eksempel på tabellstruktur


**users:**

``` sql
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(255) | NO   |     | NULL    |                |
| email | varchar(255) | NO   |     | NULL    |                |
| pword | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+

```



**runs:**
```sql
+---------+------------+------+-----+---------+----------------+
| Field   | Type       | Null | Key | Default | Extra          |
+---------+------------+------+-----+---------+----------------+
| id      | int(11)    | NO   | PRI | NULL    | auto_increment |
| hp      | int(11)    | NO   |     | NULL    |                |
| e_hp    | int(11)    | NO   |     | NULL    |                |
| user_id | int(11)    | YES  | MUL | NULL    |                |
| done    | tinyint(1) | YES  |     | 0       |                |
+---------+------------+------+-----+---------+----------------+
```