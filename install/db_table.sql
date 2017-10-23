-- Create DB
CREATE DATABASE warhammer;

-- Clean
DROP TABLE IF EXISTS unit_weapon CASCADE;
DROP TABLE IF EXISTS squad_ability CASCADE;
DROP TABLE IF EXISTS ref_unit_type CASCADE;
DROP TABLE IF EXISTS ref_codex CASCADE;
DROP TABLE IF EXISTS weapons CASCADE;
DROP TABLE IF EXISTS squads CASCADE;
DROP TABLE IF EXISTS units CASCADE;
DROP TABLE IF EXISTS abilities CASCADE;
DROP TABLE IF EXISTS army_list CASCADE;

-- Unit type ref table (Troops, Elite etc....)
CREATE TABLE ref_unit_type(
	unit_type_id serial primary key
	,unit_type_name VARCHAR(20)
);
-- Codex ref table
CREATE TABLE ref_codex(
	codex_id serial primary key
	,codex_name VARCHAR(40)
);
-- Army list
CREATE TABLE army_list(
	list_id serial primary key
	,list_name VARCHAR(30)
);
-- Squad is compsed by one or many units
CREATE TABLE squads(
	squad_id serial primary key
	,squad_name VARCHAR(30)
);
-- Abilities of every units
CREATE TABLE abilities(
	ability_id serial primary key
	,ability_name VARCHAR(20)
	,ability_description VARCHAR(100)
);
-- Weapons list
CREATE TABLE weapons(
	weapon_id serial primary key
	,weapon_name VARCHAR(30)
	,RANGE INTEGER
	,weapon_type VARCHAR(15)
	,S INTEGER
	,AP VARCHAR(3)
	,D VARCHAR(4)
	,ABILITIES VARCHAR(75)
	,cost INTEGER
);
-- Warhammer units list sigle entry
CREATE TABLE units(
	unit_id serial primary key
	,unit_name VARCHAR(30)
	,squad_id INT REFERENCES squads(squad_id)
	,unit_type INT REFERENCES ref_unit_type(unit_type_id)
	,unit_codex INT REFERENCES ref_codex(codex_id)
	,M INTEGER
	,WS INTEGER
	,BS INTEGER
	,S INTEGER
	,T INTEGER
	,A INTEGER
	,W INTEGER
	,Ld INTEGER
	,Sg INTEGER
	,cost_point INTEGER
	,cost_power INTEGER
);

-- Special abilities of a unit = allowed abilities
CREATE TABLE squad_ability(
	squad_id INT REFERENCES squads(squad_id)
	,ability_id INT REFERENCES abilities(ability_id)
);
-- Weapons available for a unit
CREATE TABLE unit_weapon(
	unit_id INT REFERENCES units(unit_id)
	,weapon_id INT REFERENCES weapons(weapon_id)
);

-- Units in a battel list
CREATE TABLE unit_list(
	unit_list_id serial primary key
	,list_id INT REFERENCES army_list(list_id)
	,squad_id INT REFERENCES squads(squad_id)
	,squad_size INTEGER
);

-- Weapon carry by a unit in a list
CREATE TABLE unit_stuff(
	unit_list_id INT REFERENCES unit_list(unit_list_id)
	,weapon_id INT REFERENCES weapons(weapon_id)
	,weapon_quantity INTEGER
);



