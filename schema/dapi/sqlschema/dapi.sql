

CREATE TABLE "Address" (
	street TEXT, 
	city TEXT, 
	postal_code TEXT, 
	PRIMARY KEY (street, city, postal_code)
);

CREATE TABLE "Concept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Event" (
	start_date DATE, 
	end_date DATE, 
	duration FLOAT, 
	is_current BOOLEAN, 
	PRIMARY KEY (start_date, end_date, duration, is_current)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Place" (
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Product" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	url TEXT, 
	start_date DATE, 
	end_date DATE, 
	is_current BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE "Project" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	url TEXT, 
	start_date DATE, 
	end_date DATE, 
	is_current BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE "Relationship" (
	start_date DATE, 
	end_date DATE, 
	related_to TEXT, 
	type TEXT, 
	PRIMARY KEY (start_date, end_date, related_to, type)
);

CREATE TABLE "Organization" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	url TEXT, 
	legal_form TEXT, 
	address TEXT, 
	mission_statement TEXT, 
	founding_date TEXT, 
	founding_location TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(founding_location) REFERENCES "Place" (id)
);
