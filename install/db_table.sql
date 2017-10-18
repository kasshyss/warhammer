-- Create DB
CREATE DATABASE warhammer;
-- Codex
CREATE TABLE codex(
	codex_id serial primary key
	,codex_name VARCHAR(20)
);
-- Warhammer units list
CREATE TABLE units(
	unit_id serial primary key
	,unit_name VARCHAR(30)
	,unit_codex INT REFERENCES codex(codex_id)
	,M INTEGER
	,WS INTEGER
	,BS INTEGER
	,S INTEGER
	,T INTEGER
	,A INTEGER
	,Ld INTEGER
	,Sg INTEGER
	,cost_point INTEGER
	,cost_power INTEGER
);
-- Abilities of every units
CREATE TABLE abilities(
	ability_id serial primary key
	,ability_name VARCHAR(20)
	,ability_description VARCHAR(100)
);
-- Codex units
CREATE TABLE codex_unit(
	unit_id INT REFERENCES units(unit_id)
	,codex_id REFERENCES codex(codex_id)
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
-- Special abilities of a unit
CREATE TABLE unit_ability(
	unit_id INT REFERENCES units(unit_id)
	,ability_id INT REFERENCES abilities(ability_id)
);
-- Army list
CREATE TABLE army_list(
	list_id serial primary key
	,list_name VARCHAR(30)
);
-- Weapons available for a unit
CREATE TABLE unit_weapon(
	unit_id INT REFERENCES units(unit_id)
	,weapon_id INT REFERENCES weapons(weapon_id)
);
-- Units in a battel list
CREATE TABLE unit_list(
	list INT REFERENCES army_list(list_id)
	,unit_id INT REFERENCES units(unit_id)
	,unit_quantity INTEGER
);
-- Weapon carry by a unit in a list
CREATE TABLE unit_stuff(
	unit_id INT REFERENCES units(unit_id)
	,weapon_id INT REFERENCES weapons(weapon_id)
	,list
	,weapon_quantity INTEGER
);
